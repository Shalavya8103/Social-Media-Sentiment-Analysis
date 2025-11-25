import os
import sys
import json
import pandas as pd
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

from config import *
from preprocessing import preprocess_dataframe, MLterm_counts
from sentiment import add_sentiment,sentiment_term
from database import save_to_database
from forecasting import forecast_term, forecast_sentiment, forecast_summary

#Loading Data
print("Loading data")
data_submission = []
for file in os.listdir(DATA_PATH_SUBMISSION):
    file_path = os.path.join(DATA_PATH_SUBMISSION, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        d = json.load(f)
        data_submission.extend(d)
data_comments = []
for file in os.listdir(DATA_PATH_COMMENT):
    file_path = os.path.join(DATA_PATH_COMMENT, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        d = json.load(f)
        data_comments.extend(d)
df_submission = pd.DataFrame(data_submission)
df_comment = pd.DataFrame(data_comments)
print("Loaded Submissions rows", len(df_submission))
print("Loaded Comments rows", len(df_comment))

#Formatting and Cleaning the Data
print("Formatting and Cleaning")
df_submission["created_utc"] = df_submission["created_utc"].apply(datetime.fromtimestamp)
df_comment["created_utc"] = df_comment["created_utc"].apply(datetime.fromtimestamp)

df_submission.drop(["created"], axis=1, inplace=True)
df_comment.drop(["created", "total_awards_received"], axis=1, inplace=True, errors='ignore')

df_submission = df_submission[df_submission["selftext"] != "[removed]"]
df_submission = df_submission[df_submission["selftext"] != "[deleted]"]
df_comment = df_comment[df_comment["body"] != "[removed]"]
df_comment = df_comment[df_comment["body"] != "[deleted]"]

df_submission['selftext'] = df_submission['selftext'].fillna('')
df_submission['combined_text'] = df_submission['title'] + ' ' + df_submission['selftext']

print("After cleaning Submissions:",len(df_submission))
print("After cleaning Comments:", len(df_comment))

#Counting the ML Terms
df_submission = preprocess_dataframe(df_submission, 'combined_text', is_submission=True)
df_comment = preprocess_dataframe(df_comment, 'body', is_submission=False)
df_submission = MLterm_counts(df_submission, ml_terms)
df_comment = MLterm_counts(df_comment, ml_terms)

#Performing Sentiment Analysis
print("Performing sentiment analysis")
df_submission = add_sentiment(df_submission)
df_comment = add_sentiment(df_comment)

#DataBase
print("Saving to database")
save_to_database(df_submission, df_comment)

#Forcasting
print("Generating forecasts")
term_year = df_submission.groupby('year')[list(ml_terms.keys())].sum()
term_month = df_submission.groupby('year_month')[list(ml_terms.keys())].sum()
sentiment_monthly = df_submission.groupby('year_month')['sentiment'].mean()
top = term_year.sum().sort_values(ascending=False).head(3).index

for term in top:
    print(" Forecasting ",term)
    df_hist, forecast = forecast_term(term, term_month[term])
    summary = forecast_summary(df_hist, forecast)
    print("Current:", summary['current'], "/month")
    print("Forecast:",summary['forecast'], "/month")
    print("Growth:", summary['growth_pct'], "%")

print(" Forecasting Sentiment")
df_hist, forecast = forecast_sentiment(sentiment_monthly)

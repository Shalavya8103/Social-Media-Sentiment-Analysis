import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config import SENTIMENT_BINS, SENTIMENT_LABELS

analyzer = SentimentIntensityAnalyzer()

def get_vader_score(text):
    if not text or pd.isna(text):
        return 0.0
    return analyzer.polarity_scores(str(text))['compound']


def add_sentiment(df):
    df['sentiment'] = df['cleaned_text'].apply(get_vader_score)
    df['sentiment_category'] = pd.cut(
        df['sentiment'], 
        bins=SENTIMENT_BINS, 
        labels=SENTIMENT_LABELS)
    print(df['sentiment_category'].value_counts())
    return df


def sentiment_term(df, ml_terms, top_n=10):
    top_terms = df[list(ml_terms.keys())].sum().sort_values(ascending=False).head(top_n).index
    results = []
    for term in top_terms:
        with_term = df[df[term] > 0]['sentiment'].mean()
        without_term = df[df[term] == 0]['sentiment'].mean()
        results.append({
            'term': term,
            'sentiment_with': with_term,
            'sentiment_without': without_term,
            'difference': with_term - without_term
        })
    return pd.DataFrame(results)
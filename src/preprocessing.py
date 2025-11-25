import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

try:
    stop_words = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

try:
    lemmatizer = WordNetLemmatizer()
    word_tokenize("test")
except:
    nltk.download('punkt')
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\[discussion\]|\[d\]|\[news\]|\[n\]|\[research\]|\[r\]|\[project\]|\[p\]', 
                  '', text, flags=re.IGNORECASE)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    return text


def tokenize_lemmatize(text):
    if not text:
        return []
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens 
              if word not in stop_words and len(word) > 2]
    return tokens


def count_ml_terms(tokens, terms_dict):
    text = ' '.join(str(token) for token in tokens)
    term_counts = {}
    for term_name, vars in terms_dict.items():
        count = 0
        for v in vars:
            count += text.count(v.lower())
        term_counts[term_name] = count
    return term_counts


def preprocess_dataframe(df, text_column, is_submission=True):
    df['cleaned_text'] = df[text_column].apply(clean_text)
    df['tokens'] = df['cleaned_text'].apply(tokenize_lemmatize)
    df['year'] = df['created_utc'].dt.year
    df['month'] = df['created_utc'].dt.month
    df['year_month'] = df['created_utc'].dt.to_period('M')
    df['date'] = df['created_utc'].dt.date
    return df


def MLterm_counts(df, ml_terms):
    term_list = []
    for tokens in enumerate(df['tokens']):
        counts = count_ml_terms(tokens, ml_terms)
        term_list.append(counts)
    
    term_df = pd.DataFrame(term_list)
    df = pd.concat([df, term_df], axis=1)
    return df
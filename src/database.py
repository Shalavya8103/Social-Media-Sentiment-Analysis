import sqlite3
import pandas as pd
from config import OUTPUT_DB

def save_to_database(df_submission, df_comment):
    df_sub_sql = df_submission.drop(['tokens', 'year_month'], axis=1, errors='ignore').copy()
    df_com_sql = df_comment.drop(['tokens', 'year_month'], axis=1, errors='ignore').copy()
    
    df_sub_sql['created_utc'] = df_sub_sql['created_utc'].astype(str)
    df_sub_sql['date'] = df_sub_sql['date'].astype(str)
    df_sub_sql['sentiment_category'] = df_sub_sql['sentiment_category'].astype(str)
    
    df_com_sql['created_utc'] = df_com_sql['created_utc'].astype(str)
    df_com_sql['date'] = df_com_sql['date'].astype(str)
    df_com_sql['sentiment_category'] = df_com_sql['sentiment_category'].astype(str)
    

    conn = sqlite3.connect(OUTPUT_DB)
    df_sub_sql.to_sql('submissions', conn, if_exists='replace', index=False)
    df_com_sql.to_sql('comments', conn, if_exists='replace', index=False)
    conn.close()

def query_database(query):
    conn = sqlite3.connect(OUTPUT_DB)
    result = pd.read_sql(query, conn)
    conn.close()
    return result
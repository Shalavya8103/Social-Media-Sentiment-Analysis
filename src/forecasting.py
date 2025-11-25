import pandas as pd
from prophet import Prophet
from config import FORECAST_PERIODS, FORECAST_FREQ

def forecast_term(term_name, monthly_data, periods=FORECAST_PERIODS):
    df = pd.DataFrame({'ds': monthly_data.index.to_timestamp(),'y': monthly_data.values})
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False)
    model.fit(df)
    future = model.make_future_dataframe(periods=periods, freq=FORECAST_FREQ)
    forecast = model.predict(future)
    return df, forecast

def forecast_sentiment(sentiment_monthly, periods=FORECAST_PERIODS):
    df = pd.DataFrame({'ds': sentiment_monthly.index.to_timestamp(),'y': sentiment_monthly.values})
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False)
    model.fit(df)
    future = model.make_future_dataframe(periods=periods, freq=FORECAST_FREQ)
    forecast = model.predict(future)
    return df, forecast

def forecast_summary(df_historical, forecast):
    current_avg = df_historical['y'].tail(12).mean()
    future_avg = forecast[forecast['ds'] > df_historical['ds'].max()]['yhat'].mean()
    growth = ((future_avg / current_avg) - 1) * 100
    return {'current': current_avg,'forecast': future_avg,'growth_pct': growth}
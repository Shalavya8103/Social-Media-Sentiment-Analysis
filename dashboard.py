import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3
import pickle


st.set_page_config(
    page_title="ML Subreddit Analysis",
    layout="wide"
)

@st.cache_data
def load_data():
    """Load processed data from pickle files"""
    try:
        df_submission = pd.read_pickle('processed_submissions.pkl')
        df_comment = pd.read_pickle('processed_comments.pkl')
        return df_submission, df_comment
    except:
        st.error("Make  processed_submissions.pkl and processed_comments.pkl exist.")
        return None, None

# Load data
df_submission, df_comment = load_data()

if df_submission is None:
    st.stop()

# ML terms list
ml_terms = {
    "SVM": ["support vector machine", "svm", "support vector"],
    "RNN": ["rnn", "recurrent neural network"],
    "LSTM": ["lstm", "long short term memory"],
    "GRU": ["gru", "gated recurrent unit"],
    "CNN": ["cnn", "convolutional neural network", "convnet"],
    "Neural Network": ["neural network", "neural net", "ann"],
    "Deep Learning": ["deep learning"],
    "Random Forest": ["random forest"],
    "Decision Tree": ["decision tree"],
    "XGBoost": ["xgboost", "xgb"],
    "Naive Bayes": ["naive bayes"],
    "KNN": ["knn", "k nearest neighbor"],
    "Linear Regression": ["linear regression"],
    "Logistic Regression": ["logistic regression"],
    "Transformer": ["transformer"],
    "BERT": ["bert"],
    "GPT": ["gpt"],
    "ResNet": ["resnet"],
    "GAN": ["gan", "generative adversarial"],
    "VAE": ["vae", "variational autoencoder"],
    "Autoencoder": ["autoencoder"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch", "torch"],
    "Keras": ["keras"],
    "Scikit-learn": ["scikit learn", "sklearn"],
    "ReLU": ["relu"],
    "Sigmoid": ["sigmoid"],
    "Softmax": ["softmax"],
    "Adam": ["adam"],
    "SGD": ["sgd", "stochastic gradient descent"],
    "RMSprop": ["rmsprop"],
    "Dropout": ["dropout"],
    "Batch Normalization": ["batch normalization", "batch norm"],
    "Transfer Learning": ["transfer learning"],
    "Data Augmentation": ["data augmentation"],
    "Regularization": ["regularization"],
    "NLP": ["nlp", "natural language processing"],
    "Computer Vision": ["computer vision"],
    "Reinforcement Learning": ["reinforcement learning"],
    "Classification": ["classification"],
    "Regression": ["regression"],
    "Clustering": ["clustering"],
}



st.title("🤖 MachineLearning Subreddit Analysis (2009-2020)")
st.markdown("### Tracking the Evolution of ML Discourse and Community Growth")
st.sidebar.header("Filters")

# Year range filter
min_year = int(df_submission['year'].min())
max_year = int(df_submission['year'].max())
year_range = st.sidebar.slider(
    "Select Year Range",
    min_year, max_year,
    (min_year, max_year)
)

# Filter data by year
df_sub_filtered = df_submission[
    (df_submission['year'] >= year_range[0]) & 
    (df_submission['year'] <= year_range[1])
]
df_com_filtered = df_comment[
    (df_comment['year'] >= year_range[0]) & 
    (df_comment['year'] <= year_range[1])
]

st.header("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Submissions",
        f"{len(df_sub_filtered):,}",
        f"{len(df_sub_filtered) - len(df_submission):,}" if year_range != (min_year, max_year) else None
    )

with col2:
    st.metric(
        "Total Comments",
        f"{len(df_com_filtered):,}",
        f"{len(df_com_filtered) - len(df_comment):,}" if year_range != (min_year, max_year) else None
    )

with col3:
    st.metric(
        "Avg Sentiment",
        f"{df_sub_filtered['sentiment'].mean():.3f}",
        f"{df_sub_filtered['sentiment'].mean() - df_submission['sentiment'].mean():.3f}" if year_range != (min_year, max_year) else None
    )

with col4:
    st.metric(
        "Avg Score",
        f"{df_sub_filtered['score'].mean():.1f}",
        f"{df_sub_filtered['score'].mean() - df_submission['score'].mean():.1f}" if year_range != (min_year, max_year) else None
    )


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "ML Topics", 
    "Sentiment", 
    "Community", 
    "Forecasts",
    "Data Explorer"
])


with tab1:
    st.header("ML Topic Trends")

    st.subheader("Top 10 Most Mentioned ML Terms")
    
    top_10_terms = df_sub_filtered[list(ml_terms.keys())].sum().sort_values(ascending=False).head(10)
    
    fig = px.bar(
        x=top_10_terms.values,
        y=top_10_terms.index,
        orientation='h',
        labels={'x': 'Frequency', 'y': 'ML Term'},
        title="Top 10 ML Terms (Filtered Period)"
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Interactive term selection
    st.subheader("Term Trends Over Time")
    
    selected_terms = st.multiselect(
        "Select ML terms to visualize",
        list(ml_terms.keys()),
        default=['Deep Learning', 'Neural Network', 'SVM', 'CNN']
    )
    
    if selected_terms:
        # Aggregate by year
        term_yearly = df_submission.groupby('year')[selected_terms].sum()
        
        fig = go.Figure()
        for term in selected_terms:
            fig.add_trace(go.Scatter(
                x=term_yearly.index,
                y=term_yearly[term],
                mode='lines+markers',
                name=term,
                line=dict(width=2)
            ))
        
        fig.update_layout(
            title="ML Term Trends (2009-2020)",
            xaxis_title="Year",
            yaxis_title="Frequency",
            height=500,
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Framework comparison
    st.subheader("Framework Popularity")
    
    frameworks = ['TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn']
    framework_yearly = df_submission.groupby('year')[frameworks].sum()
    
    fig = go.Figure()
    for fw in frameworks:
        fig.add_trace(go.Scatter(
            x=framework_yearly.index,
            y=framework_yearly[fw],
            mode='lines+markers',
            name=fw,
            line=dict(width=2.5)
        ))
    
    fig.update_layout(
        title="Framework Adoption Over Time",
        xaxis_title="Year",
        yaxis_title="Mentions",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Heatmap
    st.subheader("ML Terms Heatmap (Top 15)")
    
    top_15_terms = df_submission[list(ml_terms.keys())].sum().sort_values(ascending=False).head(15).index
    heatmap_data = df_submission.groupby('year')[top_15_terms].sum()
    
    fig = px.imshow(
        heatmap_data.T,
        labels=dict(x="Year", y="ML Term", color="Frequency"),
        aspect="auto",
        color_continuous_scale='YlOrRd'
    )
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)


with tab2:
    st.header("Sentiment Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sentiment Distribution - Submissions")
        
        fig = px.histogram(
            df_sub_filtered,
            x='sentiment',
            nbins=50,
            title="Sentiment Score Distribution",
            labels={'sentiment': 'Sentiment Score', 'count': 'Frequency'}
        )
        fig.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Neutral")
        fig.add_vline(x=df_sub_filtered['sentiment'].mean(), line_dash="dash", 
                     line_color="green", annotation_text="Mean")
        st.plotly_chart(fig, use_container_width=True)
        
        # Category counts
        sentiment_counts = df_sub_filtered['sentiment_category'].value_counts()
        fig = px.bar(
            x=sentiment_counts.index,
            y=sentiment_counts.values,
            labels={'x': 'Category', 'y': 'Count'},
            title="Sentiment Categories",
            color=sentiment_counts.index,
            color_discrete_map={'Positive': '#6BCF7F', 'Neutral': '#FFD93D', 'Negative': '#FF6B6B'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Sentiment Distribution - Comments")
        
        fig = px.histogram(
            df_com_filtered,
            x='sentiment',
            nbins=50,
            title="Sentiment Score Distribution",
            labels={'sentiment': 'Sentiment Score', 'count': 'Frequency'}
        )
        fig.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Neutral")
        fig.add_vline(x=df_com_filtered['sentiment'].mean(), line_dash="dash", 
                     line_color="green", annotation_text="Mean")
        st.plotly_chart(fig, use_container_width=True)
        
        # Category counts
        sentiment_counts = df_com_filtered['sentiment_category'].value_counts()
        fig = px.bar(
            x=sentiment_counts.index,
            y=sentiment_counts.values,
            labels={'x': 'Category', 'y': 'Count'},
            title="Sentiment Categories",
            color=sentiment_counts.index,
            color_discrete_map={'Positive': '#6BCF7F', 'Neutral': '#FFD93D', 'Negative': '#FF6B6B'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Sentiment over time
    st.subheader("Sentiment Trends Over Time")
    
    sentiment_yearly_sub = df_submission.groupby('year')['sentiment'].mean()
    sentiment_yearly_com = df_comment.groupby('year')['sentiment'].mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=sentiment_yearly_sub.index,
        y=sentiment_yearly_sub.values,
        mode='lines+markers',
        name='Submissions',
        line=dict(width=3)
    ))
    fig.add_trace(go.Scatter(
        x=sentiment_yearly_com.index,
        y=sentiment_yearly_com.values,
        mode='lines+markers',
        name='Comments',
        line=dict(width=3)
    ))
    fig.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Neutral")
    
    fig.update_layout(
        title="Average Sentiment by Year",
        xaxis_title="Year",
        yaxis_title="Mean Sentiment",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Sentiment by ML term
    st.subheader("Sentiment by ML Term")
    
    top_10 = df_submission[list(ml_terms.keys())].sum().sort_values(ascending=False).head(10).index
    
    sentiment_by_term = []
    for term in top_10:
        avg_sent = df_submission[df_submission[term] > 0]['sentiment'].mean()
        count = (df_submission[term] > 0).sum()
        sentiment_by_term.append({'Term': term, 'Avg Sentiment': avg_sent, 'Count': count})
    
    sentiment_df = pd.DataFrame(sentiment_by_term).sort_values('Avg Sentiment')
    
    fig = px.bar(
        sentiment_df,
        x='Avg Sentiment',
        y='Term',
        orientation='h',
        title="Average Sentiment for Posts Mentioning Each Term",
        color='Avg Sentiment',
        color_continuous_scale='RdYlGn',
        range_color=[-0.1, 0.3]
    )
    fig.add_vline(x=df_submission['sentiment'].mean(), line_dash="dash", 
                 annotation_text="Overall Mean")
    st.plotly_chart(fig, use_container_width=True)



with tab3:
    st.header("Community Growth & Engagement")
    
    # Activity over time
    st.subheader("Community Activity Over Time")
    
    activity_yearly_sub = df_submission.groupby('year').size()
    activity_yearly_com = df_comment.groupby('year').size()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=activity_yearly_sub.index,
        y=activity_yearly_sub.values,
        name='Submissions',
        marker_color='dodgerblue'
    ))
    fig.add_trace(go.Bar(
        x=activity_yearly_com.index,
        y=activity_yearly_com.values,
        name='Comments',
        marker_color='orangered'
    ))
    
    fig.update_layout(
        title="Posts and Comments per Year",
        xaxis_title="Year",
        yaxis_title="Count",
        barmode='group',
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Engagement metrics
    st.subheader("Engagement Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        engagement_yearly = df_submission.groupby('year').agg({
            'score': 'mean',
            'num_comments': 'mean'
        })
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=engagement_yearly.index,
            y=engagement_yearly['score'],
            mode='lines+markers',
            name='Avg Score',
            line=dict(width=3, color='purple')
        ))
        
        fig.update_layout(
            title="Average Score Over Time",
            xaxis_title="Year",
            yaxis_title="Average Score",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=engagement_yearly.index,
            y=engagement_yearly['num_comments'],
            mode='lines+markers',
            name='Avg Comments',
            line=dict(width=3, color='orange')
        ))
        
        fig.update_layout(
            title="Average Comments per Post Over Time",
            xaxis_title="Year",
            yaxis_title="Average Comments",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Score distribution
    st.subheader("Score Distribution")
    
    fig = px.histogram(
        df_sub_filtered,
        x='score',
        nbins=50,
        title="Submission Score Distribution",
        labels={'score': 'Score', 'count': 'Frequency'}
    )
    fig.update_xaxes(range=[0, df_sub_filtered['score'].quantile(0.95)])
    st.plotly_chart(fig, use_container_width=True)
    
    # Top authors
    st.subheader("Top 10 Most Active Authors")
    
    col1, col2 = st.columns(2)
    
    with col1:
        top_authors_sub = df_sub_filtered['author'].value_counts().head(10)
        fig = px.bar(
            x=top_authors_sub.values,
            y=top_authors_sub.index,
            orientation='h',
            title="By Submissions",
            labels={'x': 'Submissions', 'y': 'Author'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        top_authors_com = df_com_filtered['author'].value_counts().head(10)
        fig = px.bar(
            x=top_authors_com.values,
            y=top_authors_com.index,
            orientation='h',
            title="By Comments",
            labels={'x': 'Comments', 'y': 'Author'},
            color_discrete_sequence=['coral']
        )
        st.plotly_chart(fig, use_container_width=True)



with tab4:
    st.header("Time-Series Forecasts (2020-2022)")
    st.info("Forecasts are based on historical data from 2009-2020 using Facebook Prophet")
    
    # Import Prophet
    try:
        from prophet import Prophet
        
        # Prepare monthly data - DROP NaN FIRSTxs
        df_sub_clean = df_submission.dropna(subset=['year', 'month']).copy()
        
        df_sub_clean['year_month_dt'] = pd.to_datetime(
            df_sub_clean['year'].astype(int).astype(str) + '-' + 
            df_sub_clean['month'].astype(int).astype(str) + '-01'
        )
        
        term_monthly = df_sub_clean.groupby('year_month_dt')[list(ml_terms.keys())].sum()
        
        # Select term to forecast
        st.subheader("Forecast ML Term")
        
        selected_forecast_term = st.selectbox(
            "Select ML term to forecast",
            list(ml_terms.keys()),
            index=list(ml_terms.keys()).index('Deep Learning')
        )
        
        if st.button("Generate Forecast"):
            with st.spinner(f'Forecasting {selected_forecast_term}...'):
                # Prepare data
                data = pd.DataFrame({
                    'ds': term_monthly.index,
                    'y': term_monthly[selected_forecast_term].values
                })
                
                # Train model
                model = Prophet(yearly_seasonality=True, weekly_seasonality=False, 
                               daily_seasonality=False)
                model.fit(data)
                
                # Forecast
                future = model.make_future_dataframe(periods=24, freq='MS')
                forecast = model.predict(future)
                
                # Plot
                fig = go.Figure()
                
                # Historical
                fig.add_trace(go.Scatter(
                    x=data['ds'],
                    y=data['y'],
                    mode='markers',
                    name='Historical',
                    marker=dict(color='cyan', size=4)
                ))
                
                # Forecast
                forecast_only = forecast[forecast['ds'] > data['ds'].max()]
                fig.add_trace(go.Scatter(
                    x=forecast_only['ds'],
                    y=forecast_only['yhat'],
                    mode='lines',
                    name='Forecast',
                    line=dict(color='red', width=3)
                ))
                
                # Confidence interval
                fig.add_trace(go.Scatter(
                    x=forecast_only['ds'],
                    y=forecast_only['yhat_upper'],
                    mode='lines',
                    line=dict(width=0),
                    showlegend=False
                ))
                fig.add_trace(go.Scatter(
                    x=forecast_only['ds'],
                    y=forecast_only['yhat_lower'],
                    mode='lines',
                    fill='tonexty',
                    line=dict(width=0),
                    name='Confidence Interval',
                    fillcolor='rgba(255,0,0,0.2)'
                ))
                
                fig.update_layout(
                    title=f"{selected_forecast_term}: 24-Month Forecast",
                    xaxis_title="Date",
                    yaxis_title="Mentions per Month",
                    height=500
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Show metrics
                current_avg = data['y'].tail(12).mean()
                future_avg = forecast_only['yhat'].mean()
                growth = ((future_avg / current_avg) - 1) * 100
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Current (12-mo avg)", f"{current_avg:.1f}/month")
                col2.metric("Forecast (24-mo avg)", f"{future_avg:.1f}/month")
                col3.metric("Predicted Growth", f"{growth:+.1f}%")
    
    except ImportError:
        st.error("Prophet not installed. Run: pip install prophet")


with tab5:
    st.header("Data Explorer")
    
    # Choose dataset
    dataset_choice = st.radio("Select dataset", ["Submissions", "Comments"])
    
    if dataset_choice == "Submissions":
        st.subheader("Submissions Data")
        
        # Show sample
        st.write(f"Showing {len(df_sub_filtered):,} submissions")
        
        # Column selector
        columns_to_show = st.multiselect(
            "Select columns to display",
            df_sub_filtered.columns.tolist(),
            default=['title', 'author', 'score', 'num_comments', 'year', 'sentiment']
        )
        
        if columns_to_show:
            st.dataframe(df_sub_filtered[columns_to_show].head(100), use_container_width=True)
        
        # Download button
        csv = df_sub_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download Filtered Data (CSV)",
            csv,
            "filtered_submissions.csv",
            "text/csv",
            key='download-submissions'
        )
    
    else:
        st.subheader("Comments Data")
        
        st.write(f"Showing {len(df_com_filtered):,} comments")
        
        columns_to_show = st.multiselect(
            "Select columns to display",
            df_com_filtered.columns.tolist(),
            default=['body', 'author', 'score', 'year', 'sentiment']
        )
        
        if columns_to_show:
            st.dataframe(df_com_filtered[columns_to_show].head(100), use_container_width=True)
        
        # Download button
        csv = df_com_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download Filtered Data (CSV)",
            csv,
            "filtered_comments.csv",
            "text/csv",
            key='download-comments'
        )
    
    # Summary statistics
    st.subheader("Summary Statistics")
    
    if dataset_choice == "Submissions":
        st.write(df_sub_filtered.describe())
    else:
        st.write(df_com_filtered.describe())


st.markdown("---")
st.markdown("""**Sentiment Analysis of MachineLearning Reddit data**  
DS5110 - Data Science | 2025
""")
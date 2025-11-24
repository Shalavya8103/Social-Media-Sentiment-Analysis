# MachineLearning Subreddit Analysis
This project analyzes over a decade of discourse evolution in the MachineLearning subreddit, tracking the rise of deep learning, sentiment trends, and community growth from 2009 to 2020. The analysis includes time-series forecasting to predict future trends.

## Dataset
- **Source**: Reddit MachineLearning subreddit via Pushshift API
- **Time Period**: 2009 - February 2020
- **Content**: All submissions and comments (no images)
- **Size**: 
  - Submissions: ~100k posts
  - Comments: ~200k+ comments


## Key Features

### 1. Data Preprocessing
- Text cleaning and normalization
- Tokenization and lemmatization
- ML term extraction (40+ terms tracked)
- Deduplication

### 2. SQL Database
- Structured storage of processed data
- Efficient querying by date and topic
- Sentiment scores included

### 3. Analysis
- **ML Topic Trends**: Tracking 40+ ML terms over time
- **Sentiment Analysis**: VADER sentiment scoring
- **Community Growth**: Activity and engagement metrics
- **Time-Series Forecasting**: 24-month predictions using Prophet

### 4. Visualizations
- Historical trends (2009-2020)
- ML term popularity evolution
- Sentiment distributions and trends
- Community activity patterns
- Forecasting charts

## Installation

### Setup
```bash
# Clone or download the project
cd project_directory

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (run in Python)
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

## Usage

### Run Complete Analysis
```python
python analysis.py
```

This will:
1. Load and preprocess data
2. Perform sentiment analysis
3. Generate visualizations
4. Create forecasts
5. Save results to database

## Key Findings

### ML Term Trends
- **Deep Learning** emerged as dominant topic after 2015
- **CNN**, **LSTM**, and **Neural Network** showed exponential growth
- Traditional methods (SVM, Random Forest) declined post-2015
- **PyTorch** overtook **TensorFlow** in mentions by 2019

### Sentiment Insights
- Overall positive sentiment (mean: ~0.15)
- Sentiment remained stable over time
- Comments more positive than submissions
- Deep Learning posts showed higher sentiment

### Community Growth
- Exponential growth after 2015
- Peak activity: 2018-2020
- Comments-to-posts ratio increased over time

### Forecast (2020-2022)
- Deep Learning: +25% growth predicted
- Neural Network: +18% growth predicted
- Community activity: +30% growth predicted
- Sentiment: Stable positive trend

## ML Terms Tracked

**Models**: SVM, RNN, LSTM, GRU, CNN, Neural Network, Deep Learning, Random Forest, Decision Tree, XGBoost, Naive Bayes, KNN, Linear Regression, Logistic Regression

**Architectures**: Transformer, BERT, GPT, ResNet, GAN, VAE, Autoencoder

**Frameworks**: TensorFlow, PyTorch, Keras, Scikit-learn

**Techniques**: ReLU, Sigmoid, Softmax, Adam, SGD, Dropout, Batch Normalization, Transfer Learning, Data Augmentation, Regularization

**Areas**: NLP, Computer Vision, Reinforcement Learning, Classification, Regression, Clustering

## Database Schema

### submissions table
- id, author, title, selftext, combined_text, cleaned_text
- score, num_comments
- created_utc, year, month, date
- sentiment, sentiment_category
- [40+ ML term columns with counts]

### comments table
- id, author, body, cleaned_text
- score, link_id, parent_id
- created_utc, year, month, date
- sentiment, sentiment_category
- [40+ ML term columns with counts]


## Technologies Used
- **Python 3.9+**
- **pandas**: Data manipulation
- **NLTK**: Text preprocessing
- **VADER**: Sentiment analysis
- **Prophet**: Time-series forecasting
- **matplotlib/seaborn**: Visualizations
- **SQLite**: Data storage


## Course
DS5110 - Data Science Project

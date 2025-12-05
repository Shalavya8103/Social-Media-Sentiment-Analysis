# Applied NLP Techniques for Sentiment Analysis of Social Media Data
This project analyzes over a decade of discourse evolution in the MachineLearning subreddit, tracking the rise of deep learning, sentiment trends, and community growth from 2009 to 2020. The analysis includes time-series forecasting to predict future trends.

## Project Goal
The primary goal is to document and analyze the "Deep Learning revolution" in the machine learning community by:
- Tracking the adoption of 42 ML terms across models, frameworks, architectures, and techniques
- Analyzing sentiment trends and community growth patterns
- Identifying key inflection points (e.g., AlexNet in 2012)
- Forecasting future trends in ML technology adoption
- Providing an interactive dashboard for exploring the findings

## Dataset
- **Source**: Reddit MachineLearning subreddit via Pushshift API
- **Time Period**: 2009 - February 2020
- **Content**: All submissions and comments (no images)
- **Size**: 
  - Submissions: ~100k posts
  - Comments: ~200k+ comments

## Project Structure
The project follows a modular pipeline architecture for maintainability and reproducibility:
```
project_directory/
├── src/
│   ├── preprocessing.py      # Text cleaning, tokenization, ML term extraction
│   ├── sentiment_analysis.py # VADER sentiment scoring
│   ├── database.py           # SQLite database operations
│   ├── visualization.py      # Chart generation and plotting
│   ├── forecasting.py        # Prophet time-series forecasting
│   └── pipeline.py           # Main analysis pipeline orchestration
├── main.py                   # Entry point - runs full pipeline
├── dashboard.py              # Interactive Streamlit dashboard
├── data/                     # Raw and processed data
├── outputs/                  # Generated visualizations and results
│   ├── forecasts/           # Prophet forecasting charts
│   └── *.png                # Analysis visualizations
├── requirements.txt
├── README.md
└── REPRODUCIBILITY.md        # Detailed reproducibility guide
```

### Module Overview

**`preprocessing.py`**: Handles all text preprocessing including cleaning, normalization, tokenization, lemmatization, and ML term extraction for 42 tracked terms.

**`sentiment_analysis.py`**: Implements VADER sentiment analysis with accuracy validation (82% on test set).

**`database.py`**: Manages SQLite database operations for efficient data storage and retrieval.

**`visualization.py`**: Generates all charts including trend analysis, sentiment distributions, and forecasting plots.

**`forecasting.py`**: Implements Facebook Prophet models for 24-month predictions of ML term trends and community growth.

**`pipeline.py`**: Orchestrates the entire analysis workflow as a modular sklearn-style pipeline.

## Key Features
### 1. Data Preprocessing
- Text cleaning and normalization
- Tokenization and lemmatization
- ML term extraction (42 terms tracked)
- Deduplication

### 2. SQL Database
- Structured storage of processed data
- Efficient querying by date and topic
- Sentiment scores included

### 3. Analysis
- **ML Topic Trends**: Tracking 42 ML terms over time
- **Sentiment Analysis**: VADER sentiment scoring
- **Community Growth**: Activity and engagement metrics
- **Time-Series Forecasting**: 24-month predictions using Prophet

### 4. Visualizations
- Historical trends (2009-2020)
- ML term popularity evolution
- Sentiment distributions and trends
- Community activity patterns
- Forecasting charts

## Methodology
Our analysis follows a systematic end-to-end data science approach:

1. **Data Collection**: Retrieved 11 years of Reddit data (2009-2020) via Pushshift API, encompassing over 300,000 posts and comments

2. **Preprocessing Pipeline**: 
   - Text cleaning (URL removal, markdown cleanup, special character handling)
   - Tokenization and lemmatization using NLTK
   - Stopword removal and normalization

3. **Feature Engineering**: 
   - Extracted 42 ML terms across 5 categories (models, architectures, frameworks, techniques, areas)
   - Implemented three-tier term selection strategy (core ML, emerging tech, traditional methods)
   - Generated term frequency counts per post/comment

4. **Sentiment Analysis**: 
   - Applied VADER sentiment analyzer optimized for social media text
   - Validated with 82% accuracy on manually labeled test set
   - Categorized sentiment as positive, neutral, or negative

5. **Time-Series Analysis**: 
   - Aggregated data by month for trend analysis
   - Tracked term frequencies and sentiment over time
   - Identified key inflection points and adoption patterns

6. **Forecasting**: 
   - Trained Facebook Prophet models on historical trends
   - Generated 24-month predictions with confidence intervals
   - Cross-validated models for accuracy

7. **Validation**: 
   - Tested sentiment analyzer on labeled dataset
   - Validated forecasting models with historical holdout data
   - Documented all findings with statistical evidence

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

### Option 1: Run Complete Pipeline (Recommended)
```bash
python main.py
```

This executes the full analysis pipeline:
1. Load and preprocess data
2. Perform sentiment analysis
3. Extract ML term frequencies
4. Store results in database
5. Generate visualizations
6. Create 24-month forecasts
7. Save all outputs

### Option 2: Use Individual Modules
You can also import and use specific modules for custom analysis:
```python
from src.preprocessing import TextPreprocessor
from src.sentiment_analysis import SentimentAnalyzer
from src.forecasting import TimeSeriesForecaster

# Initialize components
preprocessor = TextPreprocessor()
sentiment_analyzer = SentimentAnalyzer()
forecaster = TimeSeriesForecaster()

# Use modules independently
cleaned_text = preprocessor.clean_text(raw_text)
sentiment_score = sentiment_analyzer.analyze(cleaned_text)
forecast = forecaster.predict(time_series_data, periods=24)
```

### Option 3: Custom Pipeline
Build your own pipeline using specific components:
```python
from src.pipeline import AnalysisPipeline

# Create custom pipeline with selected components
pipeline = AnalysisPipeline(
    steps=['preprocessing', 'sentiment', 'visualization']
)
pipeline.fit_transform(data)
```

## Outputs and Demo

### Interactive Dashboard
Explore the analysis through our interactive Streamlit dashboard:
```bash
streamlit run dashboard.py
```

The dashboard includes seven sections:
- **Overview**: Project summary and key statistics
- **Data Exploration**: Interactive data filters and exploration tools
- **ML Terms Analysis**: Time-series visualizations of all 42 tracked terms
- **Sentiment Analysis**: Sentiment distributions and trend analysis
- **Community Growth**: Subreddit activity and engagement metrics
- **Forecasting**: Prophet predictions with confidence intervals
- **Methodology**: Detailed explanation of our approach

### Generated Outputs
All visualizations and results are saved to the `outputs/` directory:
- `ml_terms_trends.png` - Historical trends of top ML terms
- `framework_comparison.png` - PyTorch vs TensorFlow adoption
- `sentiment_analysis.png` - Sentiment distribution and trends over time
- `community_growth.png` - Subreddit activity evolution
- `deep_learning_revolution.png` - Key inflection point visualization
- `forecasts/` - Prophet forecasting charts for each tracked term
- `ml_reddit_analysis.db` - SQLite database with all processed data

### Sample Visualizations
![ML Terms Trends Over Time](outputs/ml_terms_trends.png)
*Tracking the evolution of major ML terms from 2009-2020, showing the clear dominance of Deep Learning post-2015*

![Framework Adoption](outputs/framework_comparison.png)
*PyTorch overtaking TensorFlow in community discussions by 2019*

![Sentiment Analysis](outputs/sentiment_analysis.png)
*Community sentiment remains consistently positive (72% positive, mean: 0.15) across the 11-year period*

## Reproducibility
For detailed instructions on reproducing this analysis, including environment setup, data acquisition, and step-by-step execution, please see **[REPRODUCIBILITY.md](REPRODUCIBILITY.md)**.

The reproducibility guide includes:
- Complete environment specifications
- Data download and preprocessing steps
- Platform-specific execution scripts (Windows, Mac/Linux)
- Validation procedures
- Expected outputs and timings

## Key Findings
### ML Term Trends
- **Deep Learning** emerged as dominant topic after 2015, with 2000% increase in mentions
- **CNN**, **LSTM**, and **Neural Network** showed exponential growth
- **Transformer** architecture showed 2000% growth between 2017-2020
- Traditional methods (SVM, Random Forest) declined significantly post-2015
- **PyTorch** overtook **TensorFlow** in community mentions by 2019

### Framework Adoption
- **TensorFlow**: Dominated 2015-2018, now showing 5% growth rate
- **PyTorch**: Rapid adoption from 2017, 35% acceleration predicted
- **Keras**: Steady growth as high-level API
- **Scikit-learn**: Consistent presence for traditional ML

### Sentiment Insights
- Overall positive sentiment (mean: ~0.15)
- 72% of posts show positive sentiment
- Sentiment remained stable over time despite community growth
- Comments slightly more positive than submissions
- Deep Learning-related posts showed higher sentiment scores

### Community Growth
- Exponential growth after 2015 (AlexNet moment)
- Peak activity: 2018-2020
- Comments-to-posts ratio increased from 1.5 to 3.2
- Active discussions increased 400% between 2015-2020

### Forecast (2020-2022)
- **Deep Learning**: +25% growth predicted
- **Transformer**: Continued exponential growth trajectory
- **Neural Network**: +18% growth predicted
- **PyTorch**: +35% acceleration vs +5% for TensorFlow
- **Community activity**: +30% growth predicted
- **Sentiment**: Stable positive trend maintained

## ML Terms Tracked (42 Total)
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
- [42 ML term columns with counts]

### comments table
- id, author, body, cleaned_text
- score, link_id, parent_id
- created_utc, year, month, date
- sentiment, sentiment_category
- [42 ML term columns with counts]

## Technologies Used
- **Python 3.9+**
- **pandas**: Data manipulation and analysis
- **NLTK**: Text preprocessing and tokenization
- **VADER**: Sentiment analysis (82% accuracy)
- **Prophet**: Time-series forecasting
- **matplotlib/seaborn/plotly**: Static and interactive visualizations
- **Streamlit**: Interactive dashboard framework
- **SQLite**: Lightweight data storage
- **scikit-learn**: Pipeline architecture and ML utilities

## Course
DS5110 - Data Science Project

## Authors
[Your Name/Team Names]

## License
[Your License Choice]

## Acknowledgments
- Data sourced from Reddit via Pushshift API
- VADER sentiment analysis tool
- Facebook Prophet forecasting library

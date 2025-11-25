# Data Dictionary


## Database Schema

### Table: submissions

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| id | TEXT | Unique Reddit submission ID | "2jgeao" |
| author | TEXT | Username of post author | "vkhuc" |
| title | TEXT | Submission title | "Vowpal Wabbit comparison" |
| selftext | TEXT | Submission body text (original) | "[Discussion] What do you think..." |
| combined_text | TEXT | title + selftext concatenated | Full text for analysis |
| cleaned_text | TEXT | Preprocessed text (lowercase, no URLs, etc.) | Cleaned version for analysis |
| score | INTEGER | Reddit upvotes (upvotes - downvotes) | 26 |
| num_comments | INTEGER | Number of comments on submission | 8 |
| created_utc | TEXT | Creation timestamp (ISO format) | "2014-10-16 19:23:17" |
| year | INTEGER | Year extracted from timestamp | 2014 |
| month | INTEGER | Month (1-12) | 10 |
| date | TEXT | Date (YYYY-MM-DD) | "2014-10-16" |
| sentiment | FLOAT | VADER sentiment score (-1 to +1) | 0.152 |
| sentiment_category | TEXT | Sentiment category | "Positive" |
| SVM | INTEGER | Count of SVM mentions | 2 |
| RNN | INTEGER | Count of RNN mentions | 0 |
| LSTM | INTEGER | Count of LSTM mentions | 1 |
| ... | INTEGER | (40+ ML term columns) | ... |

**Total Columns**: ~55 (base columns + 40 ML terms)

---

### Table: comments

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| id | TEXT | Unique Reddit comment ID | "c0binbf" |
| author | TEXT | Username of comment author | "lanthus" |
| body | TEXT | Comment text (original) | "If possible, try several..." |
| cleaned_text | TEXT | Preprocessed comment text | Cleaned version |
| score | INTEGER | Comment upvotes | 2 |
| link_id | TEXT | Parent submission ID (with prefix) | "t3_95q7p" |
| parent_id | TEXT | Parent comment/post ID | "t1_c0bih0e" |
| created_utc | TEXT | Creation timestamp | "2009-07-29 18:27:58" |
| year | INTEGER | Year | 2009 |
| month | INTEGER | Month (1-12) | 7 |
| date | TEXT | Date (YYYY-MM-DD) | "2009-07-29" |
| sentiment | FLOAT | VADER sentiment score | 0.089 |
| sentiment_category | TEXT | Sentiment category | "Neutral" |
| SVM | INTEGER | Count of SVM mentions | 0 |
| RNN | INTEGER | Count of RNN mentions | 0 |
| ... | INTEGER | (40+ ML term columns) | ... |

**Total Columns**: ~53 (base columns + 40 ML terms)

---

## ML Terms Dictionary

### Models (14 terms)
| Term | Variations Tracked |
|------|-------------------|
| SVM | "support vector machine", "svm", "support vector" |
| RNN | "rnn", "recurrent neural network" |
| LSTM | "lstm", "long short term memory" |
| GRU | "gru", "gated recurrent unit" |
| CNN | "cnn", "convolutional neural network", "convnet" |
| Neural Network | "neural network", "neural net", "ann" |
| Deep Learning | "deep learning" |
| Random Forest | "random forest" |
| Decision Tree | "decision tree" |
| XGBoost | "xgboost", "xgb" |
| Naive Bayes | "naive bayes" |
| KNN | "knn", "k nearest neighbor" |
| Linear Regression | "linear regression" |
| Logistic Regression | "logistic regression" |

### Architectures (7 terms)
| Term | Variations Tracked |
|------|-------------------|
| Transformer | "transformer" |
| BERT | "bert" |
| GPT | "gpt" |
| ResNet | "resnet" |
| GAN | "gan", "generative adversarial" |
| VAE | "vae", "variational autoencoder" |
| Autoencoder | "autoencoder" |

### Frameworks (4 terms)
| Term | Variations Tracked |
|------|-------------------|
| TensorFlow | "tensorflow" |
| PyTorch | "pytorch", "torch" |
| Keras | "keras" |
| Scikit-learn | "scikit learn", "sklearn" |

### Activation Functions (3 terms)
| Term | Variations Tracked |
|------|-------------------|
| ReLU | "relu" |
| Sigmoid | "sigmoid" |
| Softmax | "softmax" |

### Optimizers (3 terms)
| Term | Variations Tracked |
|------|-------------------|
| Adam | "adam" |
| SGD | "sgd", "stochastic gradient descent" |
| RMSprop | "rmsprop" |

### Techniques (5 terms)
| Term | Variations Tracked |
|------|-------------------|
| Dropout | "dropout" |
| Batch Normalization | "batch normalization", "batch norm" |
| Transfer Learning | "transfer learning" |
| Data Augmentation | "data augmentation" |
| Regularization | "regularization" |

### Application Areas (6 terms)
| Term | Variations Tracked |
|------|-------------------|
| NLP | "nlp", "natural language processing" |
| Computer Vision | "computer vision" |
| Reinforcement Learning | "reinforcement learning" |
| Classification | "classification" |
| Regression | "regression" |
| Clustering | "clustering" |

**Total Terms Tracked**: 42

---

## Data Types & Formats

### Timestamps
- **Format**: ISO 8601 string "YYYY-MM-DD HH:MM:SS"
- **Timezone**: UTC
- **Example**: "2014-10-16 19:23:17"

### Sentiment Scores
- **Range**: -1.0 (most negative) to +1.0 (most positive)
- **Method**: VADER (Valence Aware Dictionary and sEntiment Reasoner)
- **Neutral Range**: -0.05 to +0.05
- **Interpretation**:
  - < -0.05: Negative
  - -0.05 to +0.05: Neutral
  - > +0.05: Positive

### ML Term Counts
- **Type**: Integer (0 or greater)
- **Method**: Case-insensitive string matching on lemmatized tokens
- **Note**: Same term can be counted multiple times per text

### Reddit IDs
- **Submission IDs**: 6-7 character alphanumeric
- **Comment IDs**: 7 character alphanumeric
- **Prefixes**: 
  - "t3_" = submission link
  - "t1_" = comment
- **Example**: "t3_2jgeao", "t1_c0binbf"

---

## Text Preprocessing Pipeline

### 1. Cleaning Steps
1. Convert to lowercase
2. Remove URLs (http://, https://, www.)
3. Remove Reddit tags ([Discussion], [R], [P], etc.)
4. Remove special characters (keep only letters, numbers, spaces)
5. Remove extra whitespace

### 2. Tokenization
- Method: NLTK word_tokenize
- Stop words removed (English)
- Words < 3 characters removed

### 3. Lemmatization
- Method: NLTK WordNetLemmatizer
- Applied to all tokens

### 4. Term Counting
- Match lemmatized tokens against term variations
- Count all occurrences (including repeated mentions)

---

## Data Quality Notes

### Missing Data
- Some submissions have empty selftext (title-only posts)
- Handled as empty string ""

### Removed Content
- Posts/comments marked "[deleted]" or "[removed]" were filtered out
- This removes ~1-3% of original data

### Duplicates
- Exact duplicate titles (submissions) removed
- Exact duplicate bodies (comments) removed
- ~2-5% of data deduplicated

### Sentiment Edge Cases
- Empty text returns sentiment = 0.0
- Very short text may have unreliable sentiment

---

## Terminology

| Term | Definition |
|------|------------|
| **Submission** | Top-level Reddit post (also called "post") |
| **Comment** | Reply to a submission or another comment |
| **Score** | Net upvotes (upvotes - downvotes) |
| **Selftext** | Body text of a submission |
| **Link_id** | ID of parent submission |
| **Parent_id** | ID of immediate parent (submission or comment) |
| **Compound Score** | VADER's overall sentiment score |
| **Lemmatization** | Reducing words to base form (e.g., "running" → "run") |
| **Token** | Individual word after preprocessing |

---

## Version Information
- **Data Version**: Pushshift API snapshot (February 2020)
- **Schema Version**: 1.0
- **Last Updated**: 2024
import os

DATA_PATH_SUBMISSION = "Dataset/json/submission"
DATA_PATH_COMMENT = "Dataset/json/comment"

OUTPUT_DB = "reddit_ml.db"
OUTPUT_SUBMISSIONS_CSV = "processed_submissions.csv"
OUTPUT_COMMENTS_CSV = "processed_comments.csv"
OUTPUT_SUBMISSIONS_PKL = "processed_submissions.pkl"
OUTPUT_COMMENTS_PKL = "processed_comments.pkl"

ml_terms = {
    # Models
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
    
    # Architectures
    "Transformer": ["transformer"],
    "BERT": ["bert"],
    "GPT": ["gpt"],
    "ResNet": ["resnet"],
    "GAN": ["gan", "generative adversarial"],
    "VAE": ["vae", "variational autoencoder"],
    "Autoencoder": ["autoencoder"],
    
    # Frameworks
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch", "torch"],
    "Keras": ["keras"],
    "Scikit-learn": ["scikit learn", "sklearn"],
    
    # Activations
    "ReLU": ["relu"],
    "Sigmoid": ["sigmoid"],
    "Softmax": ["softmax"],
    
    # Optimizers
    "Adam": ["adam"],
    "SGD": ["sgd", "stochastic gradient descent"],
    "RMSprop": ["rmsprop"],
    
    # Techniques
    "Dropout": ["dropout"],
    "Batch Normalization": ["batch normalization", "batch norm"],
    "Transfer Learning": ["transfer learning"],
    "Data Augmentation": ["data augmentation"],
    "Regularization": ["regularization"],
    
    # Areas
    "NLP": ["nlp", "natural language processing"],
    "Computer Vision": ["computer vision"],
    "Reinforcement Learning": ["reinforcement learning"],
    "Classification": ["classification"],
    "Regression": ["regression"],
    "Clustering": ["clustering"],
}


# Sentiment thresholds
SENTIMENT_BINS = [-1, -0.05, 0.05, 1]
SENTIMENT_LABELS = ['Negative', 'Neutral', 'Positive']

# Forecasting
FORECAST_PERIODS = 24  # months
FORECAST_FREQ = "MS"  # month start

# Visualization
PLOT_DPI = 300
PLOT_STYLE = "whitegrid"
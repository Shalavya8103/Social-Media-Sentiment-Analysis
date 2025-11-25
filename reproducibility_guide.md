# Reproducibility Guide

## Prerequisites
- Python 3.9 or higher
- 8GB RAM minimum (16GB recommended)
- 2GB free disk space
- Internet connection for package installation

## Step-by-Step Instructions

### 1. Environment Setup

#### Option A: Using venv (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option B: Using conda
```bash
conda create -n reddit_ml python=3.9
conda activate reddit_ml
pip install -r requirements.txt
```

### 2. Download NLTK Data
```python
# Run in Python interpreter
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
```

### 3. Data Preparation
Ensure your data is organized as:
```
Dataset/
├── json/
    ├── submission/
    │   ├── 2009-7-29.json
    │   ├── 2009-8-1.json
    │   └── ...
    └── comment/
        ├── 2009-8-1.json
        ├── 2009-8-2.json
        └── ...
```

### 4. Run Analysis

#### Full Pipeline
```bash
python analysis.py
```

### 5. Verify Outputs

Check that these files are created:
- `reddit_ml.db` (SQLite database)
- `processed_submissions.csv`
- `processed_comments.csv`
- Multiple `.png` visualization files

### 6. Query Database (Optional)
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('reddit_ml.db')

# Example queries
submissions = pd.read_sql("SELECT * FROM submissions LIMIT 5", conn)
deep_learning = pd.read_sql(
    "SELECT year, AVG(sentiment) as avg_sentiment FROM submissions WHERE [Deep Learning] > 0 GROUP BY year",
    conn
)

conn.close()
```


## Troubleshooting

### Issue: NLTK download fails
**Solution**: 
```python
import nltk
nltk.download('all')  # Downloads everything
```

## System Requirements

### Minimum
- CPU: Dual-core processor
- RAM: 8GB
- Storage: 2GB free
- OS: Windows 10, macOS 10.14, or Linux

### Recommended
- CPU: Quad-core processor or better
- RAM: 16GB
- Storage: 5GB free (for outputs)
- SSD for faster data loading

## Validation

To ensure reproducibility:

1. **Check data counts**:
```python
   import pandas as pd
   sub = pd.read_csv('processed_submissions.csv')
   print(f"Submissions: {len(sub)}")
   # Should match your dataset size
```

2. **Verify sentiment distribution**:
   - Neutral should be highest category
   - Mean sentiment around 0.15

3. **Check forecast outputs**:
   - Deep Learning should show growth
   - Sentiment should remain stable

## Notes
- First run takes longer due to NLTK downloads
- Subsequent runs faster (cached data)
- Prophet may show convergence warnings (normal)
- Some ML terms may have zero counts (expected)
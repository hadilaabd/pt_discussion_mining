import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def clean_text(text):
    # Remove HTML tags
    text = re.sub('<.*?>', '', text)
    # Remove non-alphanumeric characters and convert to lowercase
    text = re.sub('[^0-9a-zA-Z]+', ' ', text).lower()
    # Remove stopwords and stem remaining words
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    words = [ps.stem(w) for w in text.split() if w not in stop_words]
    return ' '.join(words)


# Load CSV file
df = pd.read_csv('data/limited_posts.csv')

# Drop rows with missing values
df.dropna(subset=['Title', 'Body'], inplace=True)

# Clean text in 'Title' and 'Body' columns
df['Title'] = df['Title'].apply(clean_text)
df['Body'] = df['Body'].apply(clean_text)

# Save cleaned data to new CSV file
df.to_csv('data/limited_cleaned_posts.csv', index=False)
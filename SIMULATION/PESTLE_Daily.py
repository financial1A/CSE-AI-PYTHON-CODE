import requests
from bs4 import BeautifulSoup
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import re

# Download NLTK stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# Define PESTLE categories
PESTLE_CATEGORIES = ['Political', 'Economic', 'Social', 'Technological', 'Legal', 'Environmental']

# 1. Web Scraping: Get the body text from dailymirror.lk
def get_dailymirror_text():
    url = "https://www.dailymirror.lk"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract body text, depending on the structure of the website.
    body_text = ' '.join([p.get_text() for p in soup.find_all('p')])  # Get all paragraphs
    return body_text

# 2. Text Preprocessing: Clean and preprocess the text
def clean_text(text):
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub(r'\W+', ' ', text).lower()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text

# 3. Create a simple PESTLE classifier (using keywords or a Naive Bayes classifier)
def classify_pestle(text):
    # Example keyword-based classification (can be replaced with a trained ML model)
    pestle_keywords = {
        'Political': ['government', 'policy', 'election', 'regulation', 'political'],
        'Economic': ['economy', 'market', 'inflation', 'gdp', 'employment'],
        'Social': ['society', 'culture', 'education', 'health', 'population'],
        'Technological': ['technology', 'innovation', 'automation', 'internet', 'digital'],
        'Legal': ['law', 'legislation', 'legal', 'court', 'compliance'],
        'Environmental': ['environment', 'climate', 'sustainability', 'pollution', 'green']
    }
    
    category_counts = {category: 0 for category in PESTLE_CATEGORIES}
    words = text.split()
    
    # Count occurrences of keywords in each category
    for word in words:
        for category, keywords in pestle_keywords.items():
            if word in keywords:
                category_counts[category] += 1
    
    # Total words matching any PESTLE keyword
    total_pestle_words = sum(category_counts.values())
    
    # Calculate percentage for each PESTLE category
    category_percentage = {category: (count / total_pestle_words * 100) if total_pestle_words > 0 else 0
                           for category, count in category_counts.items()}
    
    return category_percentage

# 4. Main execution flow
if __name__ == "__main__":
    # Get the raw text from Daily Mirror website
    raw_text = get_dailymirror_text()
    
    # Clean the raw text
    cleaned_text = clean_text(raw_text)
    
    # Classify the text based on PESTLE categories
    pestle_percentages = classify_pestle(cleaned_text)
    
    # Display the results
    for category, percentage in pestle_percentages.items():
        print(f"{category}: {percentage:.2f}%")

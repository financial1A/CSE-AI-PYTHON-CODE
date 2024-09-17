from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
# Define your text
text = "This is a sample text with stop words like and, is, the, in, etc."

# Remove punctuation using regex
text = re.sub(r'[^\w\s]', '', text)

# Tokenize the text
word_tokens = word_tokenize(text)

# Load stop words (assuming they are already downloaded)
stop_words = set(stopwords.words('english'))

# Filter out stop words
filtered_text = [word for word in word_tokens if word.lower() not in stop_words]

# Join the filtered words back into a string
filtered_text = ' '.join(filtered_text)

print('\n',f'Original text: {text}','\n',f'Filtered text: {filtered_text}','\n')
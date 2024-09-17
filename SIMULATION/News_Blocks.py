import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.dailymirror.lk/'

# Fetch the page content
response = requests.get(url)

# Ensure the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all div elements with the class "news_block"
    news_blocks = soup.find_all('div', class_='news_block')

    # Iterate through each news block and extract text
    for index, block in enumerate(news_blocks):
        # Extract and print the text content of the news block
        print(f"News Block {index + 1}:")
        print(block.get_text(strip=True))
        print('-' * 80)

    with open('news_blocks.txt', 'w', encoding='utf-8') as file:
        for index, block in enumerate(news_blocks):
            # Extract the text content of the news block
            block_text = block.get_text(strip=True)
            
            # Write to the text file
            file.write(f"News Block {index + 1}:\n")
            file.write(block_text + "\n")
            file.write('-' * 80 + "\n")
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")

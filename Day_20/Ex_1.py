import requests, re
from collections import Counter

def get_top_words_from_url(url, top_n=10):
    response = requests.get(url)
    text = response.text.lower()
    words = re.findall(r'\b\w+\b', text)
    return Counter(words).most_common(top_n)

# Exemple :
romeo_url = 'https://www.gutenberg.org/files/1112/1112.txt'
print(get_top_words_from_url(romeo_url, 10))

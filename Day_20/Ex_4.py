from bs4 import BeautifulSoup

def get_uci_datasets():
    url = 'https://archive.ics.uci.edu/ml/datasets.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    datasets = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'datasets/' in href:
            datasets.append(link.text.strip())

    return datasets[:20]  # Exemple : les 20 premiers

# Exemple :
print(get_uci_datasets())

import requests
from bs4 import BeautifulSoup
import time

# Function to search for a reference in DBLP and retrieve its BibTeX entry
def search_dblp(reference):
    search_url = f"https://dblp.org/search?q={reference.replace(' ', '%20')}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    bibtex_entry = ""
    for link in soup.find_all('a', href=True):
        if "bibtex" in link['href']:
            bibtex_url = link['href']
            bibtex_response = requests.get(bibtex_url)
            bibtex_soup = BeautifulSoup(bibtex_response.text, 'html.parser')
            pre_tag = bibtex_soup.find('pre')
            if pre_tag:
                bibtex_entry = pre_tag.text
                break
    return bibtex_entry

# Example references to search
references = [
    "Composable core-sets for diversity and coverage maximization",
    "Approximating extent measures of points.",
    "New frameworks for offline and streaming coreset constructions.",
    "Ten years after the rise of adversarial machine learning.",
    "On hierarchical routing in doubling metrics.",
    "A unified framework for approximating and clustering data.",
    "Epsilon-coresets for clustering (with outliers) in doubling metrics.",
    "On coresets for k-means and k-median clustering.",
    "Improved bounds on the sample complexity of learning.",
    "On coresets for logistic regression.",
    "Robust Regression and Outlier Detection.",
    "Coresets and streaming algorithms for the k-means problem and related clustering objectives.",
]

# Search for each reference and collect BibTeX entries
bibtex_entries = []
for ref in references:
    bibtex_entry = search_dblp(ref)
    if bibtex_entry:
        bibtex_entries.append(bibtex_entry)
    else:
        print(f"BibTeX entry not found for reference: {ref}")
    # Adding a delay to avoid overwhelming the server
    time.sleep(2)

# Save the BibTeX entries to a file
bibtex_file_content = "\n\n".join(bibtex_entries)
bibtex_file_path = "references.bib"
with open(bibtex_file_path, 'w') as file:
    file.write(bibtex_file_content)

print(f"BibTeX entries saved to {bibtex_file_path}")

import requests
from bs4 import BeautifulSoup
import spacy

# Load your NLP model (make sure it's compatible with your summarizer)
nlp = spacy.load("en_core_web_sm")

def summarize_text(text):
    """
    Summarize the provided text using a simple approach.
    You can replace this with more advanced logic as needed.
    """
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    # For simplicity, let's just return the first few sentences
    summary = ' '.join(sentences[:min(5, len(sentences))])
    return summary

def fetch_text_from_url(url):
    """
    Fetch and extract text from the given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ' '.join(p.get_text() for p in paragraphs)
        
        # You might want to do additional cleaning or processing here
        return article_text
    
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching the URL: {str(e)}")

from textblob import TextBlob
import wikipedia


def search_wiki(name):
    """Search for wikipedia for a given name"""
    print("Searching for {name}")
    return wikipedia.search(name)


def summarize_wiki(name):
    """Summrize wikipedia"""
    print("Summarising for {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Getting text blob"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia names and return back phrases"""

    text = summarize_wiki(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases

    return phrases

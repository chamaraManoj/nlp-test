from nlplogic.corenlp import search_wiki, summarize_wiki, get_text_blob, get_phrases

def test_get_phrases():
    assert "sri lanka" in get_phrases("Sri Lanka")

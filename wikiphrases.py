#!/usr/bin/env python
import fire
from nlplogic.corenlp import get_phrases, search_wiki

if __name__ == "__main__":
    fire.Fire(get_phrases)

from typing import List

symbols = '.,;:!?'

def normalize_word(word: str) -> str:
    return word.lower().replace('ё', 'е')

def normalize_text(text: str) -> List[str]:
    for symbol in symbols:
        text = text.replace(symbol, '')
    split_text = text.split()
    for i in range(len(split_text)):
        split_text[i] = normalize_word(split_text[i])
    return split_text
from loader import load_dict
from normalizer import normalize_text

def lemmatize(text: str, dict_map: dict) -> str:
    split_text = normalize_text(text)
    new_text = ''

    for word in split_text:
        answer = dict_map[word]
        lemma = answer[0][0]
        pos = answer[0][1]
        new_text += f'{word}{{{lemma}={pos}}} '

    return new_text


print('load dict...')
dict_map = load_dict('dict.opcorpora.xml')
print('dict loaded')

flag = True
while flag:
    text = input('input_text (q for end):\n')
    if text == 'q':
        flag = False
        break

    new_text = lemmatize(text, dict_map)
    print('Output:', new_text)
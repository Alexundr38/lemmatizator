from typing import Tuple

from database.crud import lemmatize_word
from database.database import is_table_empty
from src.loader import load_dict
from src.normalizer import normalize_text
from src.saver import save_data


def lemmatize(text: str) -> Tuple[str, float]:
    split_text = normalize_text(text)
    new_text = ''

    sum_acc = 0
    count_acc = 0

    for word in split_text:
        answer = lemmatize_word(word)
        lemma = answer[0].lemma
        pos = answer[0].pos
        acc = answer[1]

        sum_acc += acc
        count_acc += 1

        new_text += f'{word}{{{lemma}={pos}, acc={acc}}} '

    return (new_text, sum_acc/count_acc)


if is_table_empty():
    print('load dict...')
    dict_map = load_dict('dict.opcorpora.xml')
    print('dict loaded')
    save_data(dict_map)
print('data in database')

flag = True
while flag:
    text = input('input_text (q for end):\n')
    if text == 'q':
        flag = False
        break

    new_text, acc = lemmatize(text)
    print('Output:\n', new_text)
    print('acc:', acc)
    print('\n')
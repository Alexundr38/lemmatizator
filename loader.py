import xml.etree.ElementTree as ET
from normalizer import normalize_word

def load_dict(filename: str) -> dict:
    dict_map = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    lemmata = root.find('lemmata')
    for lemma in lemmata.findall('lemma'):
        element = lemma.find('l')
        if element is None:
            continue

        lemma_text = element.get('t')
        norm_lemma_text = normalize_word(lemma_text)

        base_grammemes = [g.get('v') for g in element.findall('g')]
        if not base_grammemes:
            continue

        pos = base_grammemes[0]

        for form in lemma.findall('f'):
            current_form = form.get('t')
            # grammemes = [g.get('v') for g in form.findall('g')]
            # if not grammemes:
            #     continue

            norm_current_form = normalize_word(current_form)

            dict_map.setdefault(norm_current_form, []).append(
                (norm_lemma_text, map_pos(pos))
            )
    return dict_map

def map_pos(pos: str) -> str:
    if pos == 'VERB' or pos == 'INFN':
        return 'V'
    if pos == 'ADJF' or pos == 'ADJS':
        return 'A'
    if pos == 'CONJ':
        return 'CONJ'
    if pos == 'NOUN':
        return 'S'
    if pos == 'PREP':
        return 'PR'
    if pos == 'NRPO':
        return 'NI'
    if pos == 'ADVB':
        return 'ADV'
    return pos

from database.database import get_db
from database.models import Lemma


def save_data(data: dict):
    with get_db() as db:

        for word, tuples_list in data.items():
            for lemma, pos, lemma_id in tuples_list:
                lemma_element = Lemma(
                    word=word,
                    lemma=lemma,
                    pos=pos,
                    lemma_id=lemma_id
                )
                db.add(lemma_element)
        db.commit()

        print('data saved to db')
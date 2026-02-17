from typing import Tuple

from sqlalchemy import select, or_

from database.database import get_db
from database.models import Lemma

import Levenshtein


def lemmatize_verb(word: Lemma, lemma_id: int):
    with get_db() as db:

        for i in range(0, 10):
            db_word = db.execute(
                select(Lemma.lemma_id, Lemma.lemma, Lemma.pos).\
                where(
                    Lemma.lemma_id.in_([lemma_id - i, lemma_id + i]),
                    or_(
                        Lemma.lemma.like('%ть'),
                        Lemma.lemma.like('%тся'),
                        Lemma.lemma.like('%ти')
                    )
                ).\
                group_by(Lemma.lemma_id, Lemma.lemma, Lemma.pos).\
                limit(1)
            ).one_or_none()

            if db_word is None:
                continue
            else:
                return (db_word, 1)
        return (word, 0)


def lemmatize_word(word: str) -> Tuple[Lemma, float]:
    with get_db() as db:

        db_word = db.execute(
            select(Lemma).\
            where(Lemma.word == word).\
            limit(1)
        ).scalar_one_or_none()

        if db_word is None:
            return find_closest_word_hybrid(word)

        if db_word.pos == 'V':
            return lemmatize_verb(db_word, db_word.lemma_id)

        return (db_word, 1)


def find_closest_word_hybrid(word: str) -> Tuple[Lemma, float]:
    with get_db() as db:

        candidates = db.execute(
            select(Lemma).where(
                Lemma.lemma.op('%')(word)
            )
        ).scalars().all()

        best_word = None
        best_dist = float('inf')
        for lemma in candidates:
            dist = Levenshtein.distance(word, lemma.lemma)
            if dist < best_dist:
                best_dist = dist
                best_word = lemma

        if best_word is None:
            return (Lemma(
                word=word,
                lemma_id = 0,
                pos = '?',
                lemma=word,
            ), 0)

        return (
            best_word,
            Levenshtein.ratio(word, best_word.lemma)
        )
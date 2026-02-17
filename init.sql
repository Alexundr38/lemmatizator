\c lemmatizator_db;
CREATE TABLE lemma (
    id SERIAL PRIMARY KEY,
    lemma_id INTEGER NOT NULL,
    word VARCHAR(255) NOT NULL,
    lemma VARCHAR(255) NOT NULL,
    pos VARCHAR(255) NOT NULL
);

GRANT ALL PRIVILEGES ON TABLE lemma TO lemmatizator_user;

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
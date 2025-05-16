CREATE TABLE player (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL
);

CREATE TABLE map (
    id SERIAL PRIMARY KEY,
    zone TEXT NOT NULL
);

CREATE TABLE objects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
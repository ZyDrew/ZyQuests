-- Supprimer les tables dans le bon ordre à cause des clés étrangères
DROP TABLE IF EXISTS quest_player CASCADE;
DROP TABLE IF EXISTS inventory CASCADE;
DROP TABLE IF EXISTS game CASCADE;
DROP TABLE IF EXISTS quest CASCADE;
DROP TABLE IF EXISTS map CASCADE;
DROP TABLE IF EXISTS monster CASCADE;
DROP TABLE IF EXISTS item CASCADE;
DROP TABLE IF EXISTS player CASCADE;

-- Table du joueur
CREATE TABLE player (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    class VARCHAR(20) NOT NULL,
    level INT,
    health INT,
    mana INT,
    power INT
);

-- Table des monstres
CREATE TABLE monster (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    health INT,
    power INT,
    type VARCHAR(20) NOT NULL
);

-- Table zone jouable
CREATE TABLE map (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) UNIQUE NOT NULL,
    type VARCHAR(20) UNIQUE NOT NULL
);

-- Table objet
CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    effect VARCHAR(20) NOT NULL,
    category VARCHAR(20) NOT NULL
);

-- Table des quêtes
CREATE TABLE quest (
    id SERIAL PRIMARY KEY,
    description VARCHAR(200) NOT NULL
);

-- Table de la partie
CREATE TABLE game (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    last_save TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location INT REFERENCES map(id) ON DELETE CASCADE,
    quest INT REFERENCES quest(id) ON DELETE CASCADE
);

-- Table inventaire (liaison player-item)
CREATE TABLE inventory (
    player INT REFERENCES player(id) ON DELETE CASCADE,
    item INT REFERENCES item(id) ON DELETE CASCADE
);

-- Table liaison quest-player
CREATE TABLE quest_player (
    player INT REFERENCES player(id) ON DELETE CASCADE,
    quest INT REFERENCES quest(id) ON DELETE CASCADE,
    status BOOLEAN,
    PRIMARY KEY (player, quest)
);
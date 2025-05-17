--Alimenter la table des monstres
INSERT INTO monster(name, health, power, type) VALUES ('Snake', 10, 5, 'Animal');
INSERT INTO monster(name, health, power, type) VALUES ('Ghoul', 20, 8, 'Undead');
INSERT INTO monster(name, health, power, type) VALUES ('Drake', 30, 10, 'Mythic');

--Alimenter la table des zones
INSERT INTO map(name, type) VALUES ('Valiant', 'Village');
INSERT INTO map(name, type) VALUES ('Eden Wood', 'Forest');
INSERT INTO map(name, type) VALUES ('Ancient Cave', 'Cave');

--Alimenter la table des objets
INSERT INTO item(name, effect, category) VALUES ('Short Bow', 'power+3', 'Weapon');
INSERT INTO item(name, effect, category) VALUES ('Light plate', 'health+10', 'Armor');
INSERT INTO item(name, effect, category) VALUES ('Elixir of life', 'health+5', 'Consumable');

--Alimenter la table des quêtes
INSERT INTO quest(description) VALUES ('Kill the red drake "Rubayera The Evil" that destroyed your village');

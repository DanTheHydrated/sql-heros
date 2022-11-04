CREATE TABLE IF NOT EXISTS heroes(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(256) UNIQUE NOT NULL,
    about_me varchar(512) NOT null,
    biography varchar(2048) NOT NULL,
    image_url VARCHAR(64)
);

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Apu Apustaja',
        'A fren who will always help.',
        'A Finish frog who loves helping. He helps but dont take him for a dummy or you will get no tenddies or help.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Beta Pepe',
        'He is tired of this, and it will no longer be accepted.',
        'He has been a beta all his life and now it is time for his uprising! He and his other beta friends are coming and they are donw with playing nice.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Pepe',
        'He came from nothing and started it all.',
        'He started in the lowest miost decrepped place imaginable, and ascendied to be a god. ALL PRAISE PEPE!'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Devil Pepe',
        'He has brocken out of his domain to reak havic.',
        'He has no good will twards anyone, he is evil! he is also pretty dumb... so most times things dont go the way he wants but that does not matter to him as long as long as he gets to try.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'RRRRRRREEEEEEEEEEEEEEE',
        'CCCCCHHHICCCKKKKKEEEEEEENNNNNN NNNUUUGGGGIIIIIIIEEEEESSSSSSSSSSS!',
        'HOW COULD THIS HAPPEN?!?!?! HE DROPPED HIS CHICKEN NUGGIES!!!!!!!!!!!!!!!! he is now on a rightus crusade against all people who still have nuggies.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Professors Apustaja',
        'He is smorter than the average boi and gorl.',
        'He is so smort that the reality itself falls apart around him. He can think so fast and hard that he can predict what you are about to say as long as you say! If you dont say what he thinks you are about to say then he hits you really hard with his ruler and makes you cry (he knew you would cry!). He can also run faster than the speed of light but thats not really that special ya know?'
    );

INSERT INTO
heroes (name, about_me, biography)
VALUES
    (
        'Wizard Apustaja',
        'Your a Wizard apu!',
        'He can cast spells and incantations but that doesnt stop him from helping a fren . He can also fly but he doesnt because he would have to drop the cool stick he found and he would rather not so he just walks everywhere.'
    );


CREATE TABLE relationship_types (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(64) UNIQUE NOT NULL
);

INSERT INTO
    relationship_types (name)
VALUES
    ('Friend');

INSERT INTO
    relationship_types (name)
VALUES
    ('Enemy');

CREATE TABLE relationships (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    hero1_id INTEGER NOT NULL,
    FOREIGN KEY (hero1_id) REFERENCES heroes (id) ON DELETE CASCADE,
    hero2_id INTEGER NOT NULL,
    FOREIGN KEY (hero2_id) REFERENCES heroes (id) ON DELETE CASCADE,
    relationship_type_id INTEGER NOT NULL,
    FOREIGN KEY (relationship_type_id) REFERENCES relationship_types (id) ON DELETE CASCADE
);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (1, 5, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (5, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (5, 3, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 1, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 5, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 3, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 2, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (3, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (3, 5, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (3, 2, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (2, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (2, 3, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (6, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (6, 5, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (6, 2, 1);

CREATE TABLE ability_types (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(64)
);

INSERT INTO
    ability_types (name)
VALUES
    ('Helping');

INSERT INTO
    ability_types (name)
VALUES
    ('Extreme Violence');

INSERT INTO
    ability_types (name)
VALUES
    ('All Powerful');

INSERT INTO
    ability_types (name)
VALUES
    ('Dastarldy Deeds');

INSERT INTO
    ability_types (name)
VALUES
    ('Pure Rage');

INSERT INTO
    ability_types (name)
VALUES
    ('Super Smort');

INSERT INTO
    ability_types (name)
VALUES
    ('Wizard');

-- SQLINES LICENSE FOR EVALUATION USE ONLY
-- CREATE SEQUENCE abilities_seq;

CREATE TABLE abilities (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    hero_id INTEGER NOT NULL,
    FOREIGN KEY (hero_id) REFERENCES heroes (id) ON DELETE CASCADE,
    ability_type_id INTEGER NOT NULL,
    FOREIGN KEY (ability_type_id) REFERENCES ability_types (id) ON DELETE CASCADE
);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (1, 1);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (2, 2);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (3, 3);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (4 ,4);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (5, 5);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (6, 6);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (7, 7);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (6, 7);
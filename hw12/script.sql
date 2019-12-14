CREATE TABLE movies(
    id serial NOT NULL PRIMARY KEY,
    name text NOT NULL,
    release_date date NOT NULL,
    budget integer NOT NULL
);

CREATE TABLE directors(
    id serial NOT NULL PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);

CREATE TABLE actors(
    id serial NOT NULL PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);

CREATE TABLE directors_movies(
    movie_id serial,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    director_id serial,
    FOREIGN KEY(director_id) REFERENCES directors(id)
);

CREATE TABLE actors_movies(
    movie_id serial,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    actor_id serial,
    FOREIGN KEY (actor_id) REFERENCES actors(id)
);
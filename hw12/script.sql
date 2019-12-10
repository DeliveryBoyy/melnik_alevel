CREATE TABLE movies(
    id integer NOT NULL PRIMARY KEY,
    name text NOT NULL,
    release_date date NOT NULL,
    budget integer NOT NULL
);

CREATE TABLE directors(
    id integer NOT NULL PRIMARY KEY,
    name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);

CREATE TABLE actors(
    id integer NOT NULL PRIMARY KEY,
    name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);

CREATE TABLE directors_movies(
    movie_id integer,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    director_id integer,
    FOREIGN KEY(director_id) REFERENCES directors(id)
);

CREATE TABLE actors_movies(
    movie_id integer,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    actor_id integer,
    FOREIGN KEY (actor_id) REFERENCES actors(id)
);
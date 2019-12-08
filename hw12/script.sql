CREATE TABLE movies(
    movie_id integer NOT NULL PRIMARY KEY,
    name text NOT NULL,
    release_date date NOT NULL,
    budget integer NOT NULL
);

CREATE TABLE directors(
    director_id integer NOT NULL PRIMARY KEY,
    name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);

CREATE TABLE actors(
    actor_id integer NOT NULL PRIMARY KEY,
    name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);

CREATE TABLE movies_directors_actors(
    movie_id integer,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    director_id integer,
    FOREIGN KEY(director_id) REFERENCES directors(director_id),
    actor_id integer,
    FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
)
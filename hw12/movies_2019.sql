--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors_movies (
    movie_id integer,
    actor_id integer
);


ALTER TABLE public.actors_movies OWNER TO postgres;

--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    id integer NOT NULL,
    name text NOT NULL,
    born_date date NOT NULL,
    total_movies smallint NOT NULL
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: directors_movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors_movies (
    movie_id integer,
    director_id integer
);


ALTER TABLE public.directors_movies OWNER TO postgres;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    name text NOT NULL,
    release_date date NOT NULL,
    budget integer NOT NULL
);


ALTER TABLE public.movies OWNER TO postgres;

--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, name, born_date, total_movies) FROM stdin;
\.


--
-- Data for Name: actors_movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors_movies (movie_id, actor_id) FROM stdin;
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (id, name, born_date, total_movies) FROM stdin;
\.


--
-- Data for Name: directors_movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors_movies (movie_id, director_id) FROM stdin;
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.movies (id, name, release_date, budget) FROM stdin;
\.


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: directors directors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_pkey PRIMARY KEY (id);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: actors_movies actors_movies_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(id);


--
-- Name: actors_movies actors_movies_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- Name: directors_movies directors_movies_director_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors_movies
    ADD CONSTRAINT directors_movies_director_id_fkey FOREIGN KEY (director_id) REFERENCES public.directors(id);


--
-- Name: directors_movies directors_movies_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors_movies
    ADD CONSTRAINT directors_movies_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- PostgreSQL database dump complete
--


--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2024-08-07 15:52:28

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
-- TOC entry 215 (class 1259 OID 148897)
-- Name: class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.class (
    id integer NOT NULL,
    day_week character varying NOT NULL,
    subject character varying NOT NULL,
    start_hour time without time zone,
    finish_hour time without time zone
);


ALTER TABLE public.class OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 149154)
-- Name: class_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.class ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.class_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 218 (class 1259 OID 148919)
-- Name: classroom; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classroom (
    id integer NOT NULL,
    name character varying NOT NULL,
    short_name character varying,
    floor integer NOT NULL,
    type character varying NOT NULL,
    professor_user_id integer
);


ALTER TABLE public.classroom OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 148952)
-- Name: occupancy; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.occupancy (
    id integer NOT NULL,
    goal character varying NOT NULL,
    beginning_date_time timestamp without time zone NOT NULL,
    ending_date_time timestamp without time zone,
    semester_name character varying(6) NOT NULL,
    user_id integer NOT NULL,
    classroom_id integer NOT NULL,
    class_id integer
);


ALTER TABLE public.occupancy OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 148951)
-- Name: occupancy_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.occupancy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.occupancy_id_seq OWNER TO postgres;

--
-- TOC entry 3370 (class 0 OID 0)
-- Dependencies: 220
-- Name: occupancy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.occupancy_id_seq OWNED BY public.occupancy.id;


--
-- TOC entry 219 (class 1259 OID 148931)
-- Name: permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permission (
    id integer NOT NULL,
    beginning_date_time timestamp without time zone NOT NULL,
    ending_date_time timestamp without time zone NOT NULL,
    professor_user_id integer NOT NULL,
    user_id integer NOT NULL,
    classroom_id integer NOT NULL
);


ALTER TABLE public.permission OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 149156)
-- Name: permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.permission ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 148909)
-- Name: professor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professor (
    user_id integer NOT NULL
);


ALTER TABLE public.professor OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 148904)
-- Name: semester; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.semester (
    name character varying(6) NOT NULL,
    beginning_date date NOT NULL,
    ending_date date NOT NULL
);


ALTER TABLE public.semester OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 148890)
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    id integer NOT NULL,
    name character varying NOT NULL,
    password character varying NOT NULL,
    ddd integer,
    number integer
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 3199 (class 2604 OID 148955)
-- Name: occupancy id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupancy ALTER COLUMN id SET DEFAULT nextval('public.occupancy_id_seq'::regclass);


--
-- TOC entry 3203 (class 2606 OID 148903)
-- Name: class class_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class
    ADD CONSTRAINT class_pkey PRIMARY KEY (id);


--
-- TOC entry 3209 (class 2606 OID 148925)
-- Name: classroom classroom_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classroom
    ADD CONSTRAINT classroom_pkey PRIMARY KEY (id);


--
-- TOC entry 3213 (class 2606 OID 148959)
-- Name: occupancy occupancy_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupancy
    ADD CONSTRAINT occupancy_pkey PRIMARY KEY (id);


--
-- TOC entry 3211 (class 2606 OID 148935)
-- Name: permission permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permission
    ADD CONSTRAINT permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3207 (class 2606 OID 148913)
-- Name: professor professor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_pkey PRIMARY KEY (user_id);


--
-- TOC entry 3205 (class 2606 OID 148908)
-- Name: semester semester_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.semester
    ADD CONSTRAINT semester_pkey PRIMARY KEY (name);


--
-- TOC entry 3201 (class 2606 OID 148896)
-- Name: usuario user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- TOC entry 3215 (class 2606 OID 148926)
-- Name: classroom classroom_professor_user_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classroom
    ADD CONSTRAINT classroom_professor_user_id_fk FOREIGN KEY (professor_user_id) REFERENCES public.professor(user_id) ON UPDATE CASCADE;


--
-- TOC entry 3219 (class 2606 OID 148975)
-- Name: occupancy occupancy_class_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupancy
    ADD CONSTRAINT occupancy_class_id_fk FOREIGN KEY (class_id) REFERENCES public.class(id) ON UPDATE CASCADE;


--
-- TOC entry 3220 (class 2606 OID 148970)
-- Name: occupancy occupancy_classroom_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupancy
    ADD CONSTRAINT occupancy_classroom_fk FOREIGN KEY (classroom_id) REFERENCES public.classroom(id) ON UPDATE CASCADE;


--
-- TOC entry 3221 (class 2606 OID 148960)
-- Name: occupancy occupancy_semester_name_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupancy
    ADD CONSTRAINT occupancy_semester_name_fk FOREIGN KEY (semester_name) REFERENCES public.semester(name) ON UPDATE CASCADE;


--
-- TOC entry 3222 (class 2606 OID 148965)
-- Name: occupancy occupancy_user_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupancy
    ADD CONSTRAINT occupancy_user_id_fk FOREIGN KEY (user_id) REFERENCES public.usuario(id) ON UPDATE CASCADE;


--
-- TOC entry 3216 (class 2606 OID 148946)
-- Name: permission permission_classroom_id_pk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permission
    ADD CONSTRAINT permission_classroom_id_pk FOREIGN KEY (classroom_id) REFERENCES public.classroom(id) ON UPDATE CASCADE;


--
-- TOC entry 3217 (class 2606 OID 148936)
-- Name: permission permission_professor_user_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permission
    ADD CONSTRAINT permission_professor_user_id_fk FOREIGN KEY (professor_user_id) REFERENCES public.professor(user_id) ON UPDATE CASCADE;


--
-- TOC entry 3218 (class 2606 OID 148941)
-- Name: permission permission_user_id_pk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permission
    ADD CONSTRAINT permission_user_id_pk FOREIGN KEY (user_id) REFERENCES public.usuario(id) ON UPDATE CASCADE;


--
-- TOC entry 3214 (class 2606 OID 148914)
-- Name: professor professor_user_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professor
    ADD CONSTRAINT professor_user_id_fk FOREIGN KEY (user_id) REFERENCES public.usuario(id) ON UPDATE CASCADE;


-- Completed on 2024-08-07 15:52:28

--
-- PostgreSQL database dump complete
--


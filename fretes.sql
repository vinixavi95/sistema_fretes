--
-- PostgreSQL database dump
--

\restrict DpLMNHYAkyzi2rp39UVOThYohrbxRWRpRLsqT16JgKgeYhHya9uOWBXaN3AKnt0

-- Dumped from database version 18.1 (Postgres.app)
-- Dumped by pg_dump version 18.1 (Postgres.app)

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
-- Name: fretes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fretes (
    id integer NOT NULL,
    usuario_id integer,
    cep_origem character varying(8),
    cep_destino character varying(8),
    tipo_entrega character varying(20),
    peso numeric(10,2),
    valor numeric(10,2),
    status character varying(20) DEFAULT 'calculado'::character varying,
    criado_em timestamp without time zone DEFAULT now(),
    distancia numeric(10,2),
    meio_pagamento character varying(20)
);


ALTER TABLE public.fretes OWNER TO postgres;

--
-- Name: fretes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fretes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.fretes_id_seq OWNER TO postgres;

--
-- Name: fretes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fretes_id_seq OWNED BY public.fretes.id;


--
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionarios (
    id integer NOT NULL,
    cargo character varying(20) NOT NULL,
    numero_registro character varying(50) NOT NULL,
    criado_em timestamp without time zone DEFAULT now(),
    id_usuario integer,
    CONSTRAINT funcionarios_cargo_check CHECK (((cargo)::text = ANY ((ARRAY['gerente'::character varying, 'entregador'::character varying])::text[])))
);


ALTER TABLE public.funcionarios OWNER TO postgres;

--
-- Name: funcionarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.funcionarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.funcionarios_id_seq OWNER TO postgres;

--
-- Name: funcionarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.funcionarios_id_seq OWNED BY public.funcionarios.id;


--
-- Name: pontos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pontos (
    id integer NOT NULL,
    usuario_id integer,
    data date NOT NULL,
    entrada timestamp without time zone,
    saida timestamp without time zone,
    criado_em timestamp without time zone DEFAULT now()
);


ALTER TABLE public.pontos OWNER TO postgres;

--
-- Name: pontos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pontos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pontos_id_seq OWNER TO postgres;

--
-- Name: pontos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pontos_id_seq OWNED BY public.pontos.id;


--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    telefone character varying(20),
    email character varying(100) NOT NULL,
    senha character varying(200) NOT NULL,
    criado_em timestamp without time zone DEFAULT now(),
    id_funcionario boolean DEFAULT false,
    eh_funcionario boolean DEFAULT false
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuarios_id_seq OWNER TO postgres;

--
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- Name: fretes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fretes ALTER COLUMN id SET DEFAULT nextval('public.fretes_id_seq'::regclass);


--
-- Name: funcionarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios ALTER COLUMN id SET DEFAULT nextval('public.funcionarios_id_seq'::regclass);


--
-- Name: pontos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pontos ALTER COLUMN id SET DEFAULT nextval('public.pontos_id_seq'::regclass);


--
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- Data for Name: fretes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fretes (id, usuario_id, cep_origem, cep_destino, tipo_entrega, peso, valor, status, criado_em, distancia, meio_pagamento) FROM stdin;
1	5	\N	\N	Normal	10.00	574.00	solicitado	2025-11-17 20:09:42.845022	56.90	\N
2	5	\N	\N	Normal	10.00	574.00	solicitado	2025-11-17 20:15:18.007133	56.90	\N
3	5	89207010	89260860	Sedex	7.00	408.30	enviado	2025-11-17 20:59:06.028314	56.90	debito
4	5	89200000	89000000	Sedex	12.50	350.75	solicitado	2025-11-19 15:40:27.302388	44.20	credito
5	5	89200000	89000000	Sedex	13050.00	378.75	solicitado	2025-11-19 15:41:09.219096	47.20	credito
6	1	89200000	06310400	Sedex	13050.00	356.75	solicitado	2025-11-19 15:42:44.830095	55.20	pix
7	9	78554024	89260860	Normal	255.00	593951.00	enviado	2025-11-20 23:57:56.342375	2329.20	PIX
\.


--
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.funcionarios (id, cargo, numero_registro, criado_em, id_usuario) FROM stdin;
1	gerente	11223344	2025-11-18 18:02:41.530471	7
3	entregador	276273	2025-11-18 18:09:42.149162	7
4	entregador	11222	2025-11-20 00:36:12.300381	8
5	entregador	11122	2025-11-20 00:44:00.027005	8
6	entregador	11332245	2025-11-20 23:25:55.286565	9
\.


--
-- Data for Name: pontos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pontos (id, usuario_id, data, entrada, saida, criado_em) FROM stdin;
1	7	2025-11-19	2025-11-19 16:32:04.716704	2025-11-19 16:32:36.746411	2025-11-19 16:32:04.716704
2	7	2025-11-21	2025-11-21 00:27:04.934613	2025-11-21 00:27:35.70202	2025-11-21 00:27:04.934613
3	9	2025-11-21	2025-11-21 00:31:27.952326	2025-11-21 00:31:35.628901	2025-11-21 00:31:27.952326
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (id, nome, telefone, email, senha, criado_em, id_funcionario, eh_funcionario) FROM stdin;
1	Vinicius Xavier Tobias	11965795858	vinixavi@email.com	123456	2025-11-16 21:00:11.429743	f	f
3	Mateus Freitas Borsatti	54973648833	borsatti@email.com	123456	2025-11-16 21:08:56.958812	f	f
5	Teste da Silva Jr	1196253777	teste2@email.com	$argon2id$v=19$m=65536,t=3,p=4$xFhrjRECgDBmjPEeQ0jpXQ$9u3PbEOvBpgSt64fo8k6E095qWXcxpxkDSsPxVfHfJg	2025-11-17 15:22:25.535574	f	f
7	Teste Novo da Silva Jr	11965792525	testeNovo3@email.com	$argon2id$v=19$m=65536,t=3,p=4$ew/hPKdUaq2V8j7n/P/fmw$y7O7NuDouQBNVGf4TopsqgyyLcasiWk+4mvO/szRfWE	2025-11-18 17:53:38.962459	f	t
8	Administrador	11965795858	admin@email.com	$argon2id$v=19$m=65536,t=3,p=4$7x3DWOs9B0DonXNuTQmh9A$xJ/EblXYE8qaQamJPvKTX5U1kwiRXheE/sBW6O9p47M	2025-11-20 00:12:23.14116	f	t
9	Administrador Local	1198365455	admlocal@email.com	$argon2id$v=19$m=65536,t=3,p=4$dG5t7X0PQWht7T0nROj9Xw$A1dJInVukhpFdZbRYXGB0Bb0ApvkLyLhbStRjsJ9rZM	2025-11-20 23:12:16.624352	f	t
\.


--
-- Name: fretes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fretes_id_seq', 7, true);


--
-- Name: funcionarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.funcionarios_id_seq', 6, true);


--
-- Name: pontos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pontos_id_seq', 3, true);


--
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 9, true);


--
-- Name: fretes fretes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fretes
    ADD CONSTRAINT fretes_pkey PRIMARY KEY (id);


--
-- Name: funcionarios funcionarios_numero_registro_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_numero_registro_key UNIQUE (numero_registro);


--
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (id);


--
-- Name: pontos pontos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pontos
    ADD CONSTRAINT pontos_pkey PRIMARY KEY (id);


--
-- Name: usuarios usuarios_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_email_key UNIQUE (email);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- Name: fretes fretes_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fretes
    ADD CONSTRAINT fretes_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: funcionarios funcionarios_id_usuario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_id_usuario_fkey FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id);


--
-- Name: pontos pontos_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pontos
    ADD CONSTRAINT pontos_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- PostgreSQL database dump complete
--

\unrestrict DpLMNHYAkyzi2rp39UVOThYohrbxRWRpRLsqT16JgKgeYhHya9uOWBXaN3AKnt0


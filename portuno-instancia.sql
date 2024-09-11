--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2024-08-07 15:53:07

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

--
-- TOC entry 3365 (class 0 OID 148897)
-- Dependencies: 215
-- Data for Name: class; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (70, 'SEX', 'SMD0052 - PROGRAMAÇÃO PARA WEB I', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (71, 'TER', 'SMD0056 - DIREÇÃO DE ARTE PARA MULTIMÍDIA', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (72, 'QUI', 'SMD0056 - DIREÇÃO DE ARTE PARA MULTIMÍDIA', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (73, 'SEX', 'SMD0102 - METODOLOGIA DE PESQUISA CIENTÍFICA', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (74, 'SEG', 'SMD0107 - COGNIÇÃO E TECNOLOGIAS DIGITAIS', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (75, 'SEX', 'SMD0107 - COGNIÇÃO E TECNOLOGIAS DIGITAIS', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (76, 'SEX', 'SMD0103 - SEMINÁRIOS EM MULTIMÍDIA', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (77, 'TER', 'SMD0025 - ÉTICA E POLÍTICA AUTORAL', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (78, 'QUI', 'SMD0025 - ÉTICA E POLÍTICA AUTORAL', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (79, 'SEG', 'SMD0039 - CULTURA DE JOGOS', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (80, 'TER', 'SMD0090 - SEMIÓTICA APLICADA', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (81, 'QUI', 'SMD0090 - SEMIÓTICA APLICADA', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (82, 'TER', 'SMD0045 - LINGUAGEM DE PROGRAMAÇÃO SCRIPT', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (83, 'QUI', 'SMD0045 - LINGUAGEM DE PROGRAMAÇÃO SCRIPT', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (84, 'SEG', 'SMD0051 - REDAÇÃO PARA MÍDIAS DIGITAIS', '08:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (85, 'SEG', 'SMD0098 - DESENHO II', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (86, 'QUA', 'SMD0098 - DESENHO II', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (87, 'QUA', 'SMD0093 - NARRATIVAS MULTIMÍDIA', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (88, 'TER', 'SMD0096 - PROGRAMAÇÃO II', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (89, 'QUI', 'SMD0096 - PROGRAMAÇÃO II', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (90, 'SEG', 'SMD0129 - TÉCNICAS DE ANIMAÇÃO 2D', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (91, 'QUA', 'SMD0129 - TÉCNICAS DE ANIMAÇÃO 2D', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (92, 'TER', 'SMD0020 - PROTOTIPAÇAO DE JOGOS TRIDIMENSIONAIS', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (93, 'QUI', 'SMD0020 - PROTOTIPAÇAO DE JOGOS TRIDIMENSIONAIS', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (94, 'TER', 'SMD0030 - ANÁLISE E PROJETO DE SISTEMAS', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (95, 'QUI', 'SMD0030 - ANÁLISE E PROJETO DE SISTEMAS', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (96, 'SEG', 'SMD0033 - ESTRUTURA DE DADOS', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (97, 'QUA', 'SMD0033 - ESTRUTURA DE DADOS', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (98, 'SEX', 'SMD0021 - GESTÃO DE NEGOCIOS EM MULTIMÍDIA', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (99, 'SEG', 'SMD0035 - MATEMÁTICA E FÍSICA PARA JOGOS', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (100, 'QUA', 'SMD0035 - MATEMÁTICA E FÍSICA PARA JOGOS', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (101, 'SEG', 'SMD0037 - REDES DE COMPUTADORES', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (102, 'QUA', 'SMD0037 - REDES DE COMPUTADORES', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (103, 'QUA', 'SMD0083 - EDUCOMUNICAÇÃO', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (104, 'TER', 'SMD0086 - FOTOGRAFIA DIGITAL', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (105, 'QUI', 'SMD0086 - FOTOGRAFIA DIGITAL', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (106, 'TER', 'SMD0084 - EXPERIMENTOS EM TIPOGRAFIA DIGITAL', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (107, 'SEX', 'SMD0084 - EXPERIMENTOS EM TIPOGRAFIA DIGITAL', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (108, 'TER', 'SMD0100 - GESTÃO DE PROJETOS MULTIMÍDIA', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (109, 'QUI', 'SMD0100 - GESTÃO DE PROJETOS MULTIMÍDIA', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (110, 'TER', 'SMD0112 - INSTALAÇÕES MULTIMÍDIA', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (111, 'QUI', 'SMD0112 - INSTALAÇÕES MULTIMÍDIA', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (112, 'SEG', 'SMD0105 - COMUNICAÇÃO VISUAL I', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (113, 'SEX', 'SMD0105 - COMUNICAÇÃO VISUAL I', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (114, 'TER', 'SMD0106 - MATEMÁTICA APLICADA À MULTIMÍDIA I', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (115, 'QUI', 'SMD0106 - MATEMÁTICA APLICADA À MULTIMÍDIA I', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (116, 'SEG', 'SMD0117 - INTERAÇÃO HUMANO-COMPUTADOR II', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (117, 'QUA', 'SMD0117 - INTERAÇÃO HUMANO-COMPUTADOR II', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (118, 'SEG', 'SMD0119 - TÓPICOS AVANÇADOS EM DESIGN DE INTERFACES GRÁFICAS', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (119, 'SEX', 'SMD0119 - TÓPICOS AVANÇADOS EM DESIGN DE INTERFACES GRÁFICAS', '10:00:00', '12:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (120, 'SEG', 'SMD0122 - PROGRAMAÇÃO PARA DISPOSITIVOS MÓVEIS', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (121, 'QUA', 'SMD0122 - PROGRAMAÇÃO PARA DISPOSITIVOS MÓVEIS', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (122, 'SEG', 'SMD0107 - COGNIÇÃO E TECNOLOGIAS DIGITAIS', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (123, 'SEX', 'SMD0107 - COGNIÇÃO E TECNOLOGIAS DIGITAIS', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (124, 'SEX', 'SMD0102 - METODOLOGIA DE PESQUISA CIENTÍFICA', '14:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (125, 'TER', 'SMD0025 - ÉTICA E POLÍTICA AUTORAL', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (126, 'QUI', 'SMD0025 - ÉTICA E POLÍTICA AUTORAL', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (127, 'SEG', 'SMD0105 - COMUNICAÇÃO VISUAL I', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (128, 'SEX', 'SMD0105 - COMUNICAÇÃO VISUAL I', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (129, 'TER', 'SMD0100 - GESTÃO DE PROJETOS MULTIMÍDIA', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (130, 'QUI', 'SMD0100 - GESTÃO DE PROJETOS MULTIMÍDIA', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (131, 'TER', 'SMD0086 - FOTOGRAFIA DIGITAL', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (132, 'QUI', 'SMD0086 - FOTOGRAFIA DIGITAL', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (133, 'TER', 'SMD0106 - MATEMÁTICA APLICADA À MULTIMÍDIA I', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (134, 'QUI', 'SMD0106 - MATEMÁTICA APLICADA À MULTIMÍDIA I', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (135, 'TER', 'SMD0096 - PROGRAMAÇÃO II', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (136, 'QUI', 'SMD0096 - PROGRAMAÇÃO II', '14:00:00', '16:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (137, 'SEG', 'SMD0030 - ANÁLISE E PROJETO DE SISTEMAS', '16:00:00', '18:00:00');
INSERT INTO public.class (id, day_week, subject, start_hour, finish_hour) OVERRIDING SYSTEM VALUE VALUES (138, 'QUA', 'SMD0030 - ANÁLISE E PROJETO DE SISTEMAS', '16:00:00', '18:00:00');


--
-- TOC entry 3364 (class 0 OID 148890)
-- Dependencies: 214
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (527898, 'João Freitas', '7810s4', 85, 986655890);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (508007, 'Raquel Fernandes', 'sE0724', 85, 987560857);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (577823, 'Lucas Costa', 'glk27234', 88, 996335660);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (590089, 'Maria Nunes', 'aSjE4dI71', 85, 997430089);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (522333, 'João Ferreira', '7810s4', 85, 986655890);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (589117, 'Mariana Queiroz', 'dFD22347', 88, 923344701);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (578144, 'Pedro Santos', 'sK2LnM81', 88, 997412223);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (556891, 'Alice Santos', 'E48a1A7', 85, 999477120);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (578994, 'Pedro Fernandes', 'sndAAA', 85, 977673450);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (566690, 'Luana Ferreira', 'JJJADBA', 85, 992230577);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (589696, 'João Farias', 'dFD22347', 85, 923344701);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (550723, 'Talia Silva', 'cD2dfe', 85, 997722310);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (593347, 'Marcos Farias', 'ejJs01', 85, 991288365);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (504717, 'Lucas Costa', '1234', 88, 923344701);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (98765, 'George Gomes', 'george123', 85, 1111111111);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (574238, 'Alice Silva Oiticica', '123474', 85, 933560078);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (111111, 'Admin', 'Jv123', 11, 111111111);
INSERT INTO public.usuario (id, name, password, ddd, number) VALUES (509697, 'João Victor Alves', 'Jv123', 88, 992136000);


--
-- TOC entry 3367 (class 0 OID 148909)
-- Dependencies: 217
-- Data for Name: professor; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.professor (user_id) VALUES (556891);
INSERT INTO public.professor (user_id) VALUES (527898);
INSERT INTO public.professor (user_id) VALUES (593347);
INSERT INTO public.professor (user_id) VALUES (578994);
INSERT INTO public.professor (user_id) VALUES (550723);


--
-- TOC entry 3368 (class 0 OID 148919)
-- Dependencies: 218
-- Data for Name: classroom; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (1, 'Laboratório de Fablearn', 'Fablearn', 0, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (2, 'Sala 01', 'Sala 01', 0, 'sala de aula', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (3, 'Sala 02', 'Sala 02', 0, 'sala de aula', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (5, 'Sala 03', 'Sala 03', 0, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (6, 'Sala 05', 'Sala 05', 0, 'sala de aula', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (7, 'Sala 04', 'Sala 04', 0, 'sala de aula', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (8, 'Laboratório de Tecnodocência', 'Tecnodoc.', 0, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (9, 'Laboratório de Usabilidade', 'Usab.', 0, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (10, 'Laboratório 01', 'Lab. 01', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (11, 'Laboratório 04', 'Lab. 04', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (12, 'Laboratório 02', 'Lab. 02', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (13, 'Laboratório 05', 'Lab. 05', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (14, 'Laboratório 03', 'Lab. 03', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (15, 'Laboratório 06', 'Lab. 06', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (16, 'Laboratório de Jogos', 'Lab. Jogos', 1, 'laboratório temático', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (17, 'Laboratório de Produção e Desenvolvimento 1', 'P&D 1', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (18, 'Laboratório de Computação física', 'Comp. Fís', 1, 'laboratório temático', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (19, 'Laboratório de Produção e Desenvolvimento 2', 'P&D 2', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (20, 'Sala da Pós Graduação', 'Pós Grad.', 1, 'sala de aula', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (21, 'Laboratório de Sistemas', 'Lab. Sist', 1, 'laboratório de informática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (22, 'Sala de Reuniões', 'Reuniões', 2, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (23, 'Sala de Audivisual', 'Audivisual', 2, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (24, 'Sala dos Professores', 'Professores', 2, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (25, 'Laboratório de visualizações interativas e simulações', 'LabVis', 2, 'sala temática', NULL);
INSERT INTO public.classroom (id, name, short_name, floor, type, professor_user_id) VALUES (4, 'Ateliê', 'Ateliê', 0, 'sala temática', 527898);


--
-- TOC entry 3366 (class 0 OID 148904)
-- Dependencies: 216
-- Data for Name: semester; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.semester (name, beginning_date, ending_date) VALUES ('2023.1', '2023-08-03', '2023-06-13');
INSERT INTO public.semester (name, beginning_date, ending_date) VALUES ('2023.2', '2023-08-14', '2023-12-13');


--
-- TOC entry 3371 (class 0 OID 148952)
-- Dependencies: 221
-- Data for Name: occupancy; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (27, 'Estudar', '2023-06-29 22:29:40', '2023-06-29 23:23:37', '2023.1', 509697, 2, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (28, 'Estudar', '2023-06-29 22:46:01', '2023-06-29 23:30:45', '2023.1', 508007, 1, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (30, 'Estudar', '2023-06-29 23:33:17', NULL, '2023.1', 522333, 23, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (29, 'Estudar', '2023-06-29 23:32:06', '2023-06-30 00:10:18', '2023.1', 509697, 4, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (31, 'Estudar', '2023-06-30 00:18:40', '2023-06-30 00:19:25', '2023.1', 509697, 24, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (32, 'Estudar', '2023-06-30 10:42:58', '2023-06-30 10:49:17', '2023.1', 509697, 25, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (33, 'Estudar', '2023-06-30 16:14:55', '2023-06-30 17:52:28', '2023.1', 509697, 2, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (34, 'Estudar', '2023-06-30 17:55:49', '2023-06-30 17:58:30', '2023.1', 509697, 25, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (35, 'Estudar', '2023-07-06 00:13:02', '2023-07-06 00:19:34', '2023.1', 509697, 3, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (36, 'Estudar', '2023-07-06 00:30:00', '2023-07-06 00:30:19', '2023.1', 98765, 12, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (37, 'Estudar', '2023-07-06 00:33:29', '2023-07-06 00:34:28', '2023.1', 509697, 4, NULL);
INSERT INTO public.occupancy (id, goal, beginning_date_time, ending_date_time, semester_name, user_id, classroom_id, class_id) VALUES (38, 'Estudar', '2023-07-06 01:07:52', NULL, '2023.1', 509697, 2, NULL);


--
-- TOC entry 3369 (class 0 OID 148931)
-- Dependencies: 219
-- Data for Name: permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.permission (id, beginning_date_time, ending_date_time, professor_user_id, user_id, classroom_id) OVERRIDING SYSTEM VALUE VALUES (8, '2023-07-04 00:00:00', '2023-07-31 00:00:00', 527898, 509697, 4);
INSERT INTO public.permission (id, beginning_date_time, ending_date_time, professor_user_id, user_id, classroom_id) OVERRIDING SYSTEM VALUE VALUES (12, '2023-08-01 00:00:00', '2023-08-02 00:00:00', 527898, 98765, 4);


--
-- TOC entry 3379 (class 0 OID 0)
-- Dependencies: 222
-- Name: class_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.class_id_seq', 138, true);


--
-- TOC entry 3380 (class 0 OID 0)
-- Dependencies: 220
-- Name: occupancy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.occupancy_id_seq', 38, true);


--
-- TOC entry 3381 (class 0 OID 0)
-- Dependencies: 223
-- Name: permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.permission_id_seq', 12, true);


-- Completed on 2024-08-07 15:53:07

--
-- PostgreSQL database dump complete
--


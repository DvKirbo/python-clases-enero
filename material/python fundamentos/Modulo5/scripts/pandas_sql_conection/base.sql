CREATE SEQUENCE public.alumno_id_seq;

CREATE TABLE public.alumno (
                id BIGINT NOT NULL DEFAULT nextval('public.alumno_id_seq'),
                codigo VARCHAR(10) NOT NULL,
                nombres VARCHAR(30) NOT NULL,
                apellidos VARCHAR(30) NOT NULL,
                direccion VARCHAR(50) NOT NULL,
                CONSTRAINT alumno_pk PRIMARY KEY (id)
);

ALTER SEQUENCE public.alumno_id_seq OWNED BY public.alumno.id;

INSERT INTO public.alumno (codigo, nombres, apellidos, direccion) VALUES('0502020001', 'MIGUEL ANGEL', 'TIMANA PAZ', 'LIMA');
INSERT INTO public.alumno (codigo, nombres, apellidos, direccion) VALUES('0502020002', 'LUIS', 'PANTA PANTA', 'LIMA');
INSERT INTO public.alumno (codigo, nombres, apellidos, direccion) VALUES('0502020003', 'CARLOS', 'SANCHEZ CASTRO', 'LIMA');
INSERT INTO public.alumno (codigo, nombres, apellidos, direccion) VALUES('0502020004', 'LEONEL', 'ARENAS CASTRO', 'LIMA');
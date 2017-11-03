DROP TABLE IF EXISTS estudiante;

CREATE TABLE estudiante (

	codigo VARCHAR(20) NOT NULL,
	nombre VARCHAR(50) NOT NULL,	

	CONSTRAINT estudiante_pk PRIMARY KEY (codigo)
	
);


INSERT INTO estudiante VALUES ('0', 'Pepito Perez');
INSERT INTO estudiante VALUES ('1', 'Jorge Llanos');
INSERT INTO estudiante VALUES ('2', 'Luisa Torres');
INSERT INTO estudiante VALUES ('3', 'Maria Mendez');
INSERT INTO estudiante VALUES ('4', 'Camilo Cepeda');
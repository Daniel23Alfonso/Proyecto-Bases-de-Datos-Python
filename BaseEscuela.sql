CREATE DATABASE BaseEscuela;

CREATE TABLE Curso(
id_Curso integer,
numCurso integer,
anoLectivo integer,
paralelo varchar(2),
cedula char(10),
PRIMARY KEY (id_Curso)
);


CREATE TABLE Materia(
id_Materia integer,
Nombre varChar(20),
PRIMARY KEY (id_Materia)
);


CREATE TABLE Quimestre(
id_Quimestre integer,
numQuimestre integer,
notaQuimestre double,
id_MatEstQui integer,
PRIMARY KEY (id_Quimestre)
);

CREATE TABLE Parcial(
id_Parcial integer,
numParcial integer,
notaParcial double,
id_Quimestre integer,
PRIMARY KEY (id_Parcial)
);


CREATE TABLE Actividad(
id_Actividad integer,
notaActividad double,
tipoActividad varChar(20),
id_Parcial integer,
PRIMARY KEY (id_Actividad)
);

CREATE TABLE CursoEstudiante(
id_Curso integer,
Cedula varChar(10),
PRIMARY KEY (id_Curso,Cedula)
);


CREATE TABLE CursoMateriaProfesor(
id_Relacion integer,
id_Curso integer,
id_Materia integer,
Cedula varChar(10),
PRIMARY KEY (id_Relacion)
);


CREATE TABLE MateriaExamenEstudiante(
id_Relacion integer,
Cedula varChar(10),
id_Examen integer,
PRIMARY KEY (id_Relacion)
);


CREATE TABLE Deuda(
id_Deuda integer,
descripcion varChar(50),
valor double,
id_Factura integer,
cedula varChar(10),
PRIMARY KEY (id_Deuda)
);



CREATE TABLE Persona
(cedula char (10),
nombres varchar(100),
apellidos varchar(100),
sexo varchar(10),
fechaNacimiento date,
estadoCivil varchar (25),
ocupacion varchar (25),
lugarTrabajo varchar (100),
telefono char (6),
direccion varchar (100),
PRIMARY KEY (cedula));

CREATE TABLE Estudiante
(cedula char (10),
nombres varchar(100),
apellidos varchar(100),
sexo varchar(10),
estadoCivil varchar (25),
origen varchar (30),
Etnia varchar (20),
fechaNacimiento date,
PRIMARY KEY (cedula));

CREATE TABLE Profesor
(cedula char (10),
nombres varchar(100),
apellidos varchar(100),
usuario varchar (10),
contrasenia varchar (16),
PRIMARY KEY (cedula));

CREATE TABLE MateriaEstudianteQuimestre
(id_MatEsQui int,
id_relaion int,
CedulaEstudiante char(10),
PRIMARY KEY (id_MatEsQui),
FOREIGN KEY (CedulaEstudiante) REFERENCES Estudiante(cedula));


CREATE TABLE PersonaEstudiante
(cedulaPersona char (10),
CedulaEstudiante char(10),
FOREIGN KEY (CedulaEstudiante) REFERENCES Estudiante(cedula),
FOREIGN KEY (CedulaPersona) REFERENCES Persona(cedula));


CREATE TABLE PersonaFactura
(cedula char (10),
nombre varchar (100),
apellido varchar (100),
telefono char (6),
Direccion varchar (50),
PRIMARY KEY (cedula));



CREATE TABLE Factura
(id_Factura int,
cedula char (10),
fecha date,
valor float(2),
PRIMARY KEY (id_Factura),
FOREIGN KEY (cedula) REFERENCES PersonaFactura(cedula));


CREATE TABLE Administrativo
(id_administrativo char (10),
nombres varchar(100),
apellidos varchar(100),
usuario varchar (10),
contrasenia varchar (16),
PRIMARY KEY (id_administrativo));




create table Movie(mID int, title varchar(50), year int, director varchar(50),UNIQUE (mID),UNIQUE (title,year)
					,CONSTRAINT movRest1 CHECK(year > 1900)
					,CONSTRAINT movRest2 CHECK(year < 1990 AND director = 'Steven Spielberg')
					,CONSTRAINT movRest3 CHECK(year > 1990 AND director = 'James Cameron')
					);

create table Reviewer(rID int, name varchar(50) NOT NULL,PRIMARY KEY(rID));
create table Rating(rID int, mID int, stars int NOT NULL, ratingDate date,UNIQUE(rID,mID,ratingDate)
					,CONSTRAINT ratRest1 CHECK (ratingDate >2000 AND stars in (1,2,3,4,5)) 
					,CONSTRAINT ratingReviewr FOREIGN KEY(rID)REFERENCES Reviewer(rID) ON UPDATE CASCADE ON DELETE SET NULL
					,CONSTRAINT ratingMovie FOREIGN KEY(mID)REFERENCES Movie(mID) ON DELETE CASCADE ON UPDATE NO ACTION
);
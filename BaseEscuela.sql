Create DataBase BaseEscuela;
use BaseEscuela;

CREATE TABLE Profesor
(cedula char (10),
nombres varchar(100),
apellidos varchar(100),
usuario varchar (10),
contrasenia varchar (16),
CONSTRAINT CHECK(sexo in ('Masculino','Femenino')),
PRIMARY KEY (cedula)
);

CREATE TABLE Curso(
id_Curso integer,
numCurso integer,
anoLectivo varChar(10),
paralelo varchar(2),
cedulaProfesor char(10),
PRIMARY KEY (id_Curso),
FOREIGN KEY (cedulaProfesor) REFERENCES Profesor(cedula) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Estudiante
(numMatricula integer,
cedula char (10),
nombres varchar(100),
apellidos varchar(100),
sexo varchar(10),
estadoCivil varchar (25),
origen varchar (30),
Etnia varchar (20),
fechaNacimiento date,
CONSTRAINT CHECK(sexo in ('Masculino','Femenino')),
PRIMARY KEY (numMatricula),
UNIQUE (cedula)
);


CREATE TABLE CursoEstudiante(
id_Curso integer,
numMatricula integer,
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (id_Curso) REFERENCES Curso(id_Curso) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Materia(
id_Materia integer,
Nombre varChar(20),
PRIMARY KEY (id_Materia),
UNIQUE (Nombre)
);


CREATE TABLE CursoMateriaProfesor(
id_Relacion integer,
id_Curso integer,
id_Materia integer,
CedulaProfesor varChar(10),
PRIMARY KEY (id_Relacion),
FOREIGN KEY (id_Curso) REFERENCES Curso(id_Curso) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (id_Materia) REFERENCES Materia(id_Materia) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (CedulaProfesor) REFERENCES Profesor(cedula) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE MateriaEstudianteQuimestre
(id_MatEsQui integer,
id_relacion integer,
numMatricula integer,
PRIMARY KEY (id_MatEsQui),
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula)ON DELETE CASCADE ON UPDATE CASCADE
#FOREIGN KEY (id_relacion) REFERENCES CursoMateriaProfesor(id_Relacion) ON DELETE CASCADE ON UPDATE CASCADE
);



CREATE TABLE Quimestre(
id_Quimestre integer AUTO_INCREMENT,
numQuimestre integer,
notaQuimestre numeric(4,2),
id_MatEstQui integer,
CONSTRAINT c_notas CHECK (notaQuimestre>= 0.00 and notaQuimestre <= 10.00),
PRIMARY KEY (id_Quimestre),
FOREIGN KEY (id_MatEstQui) REFERENCES MateriaEstudianteQuimestre(id_MatEsQui) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Parcial(
id_Parcial integer AUTO_INCREMENT,
numParcial integer,
notaParcial numeric(4,2),
id_Quimestre integer,
PRIMARY KEY (id_Parcial),
FOREIGN KEY (id_Quimestre) REFERENCES Quimestre(id_Quimestre) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Actividad(
id_Actividad integer AUTO_INCREMENT,
notaActividad numeric(4,2),
tipoActividad varChar(20),
id_Parcial integer,
CONSTRAINT c_notas CHECK (notaActividad>= 0.00 and notaActividad <= 10.00),
PRIMARY KEY (id_Actividad),
FOREIGN KEY (id_Parcial) REFERENCES Parcial(id_Parcial) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Examen (
id_Examen integer,
notaExamen numeric(4,2),
tipoExamen varchar(30),
CONSTRAINT c_notas CHECK (notaExamen>= 0.00 and notaExamen <= 10.00),
PRIMARY KEY  (id_Examen)
);

CREATE TABLE MateriaExamenEstudiante(
id_Relacion integer,
numMatricula integer,
id_Examen integer,
FOREIGN KEY (id_relacion) REFERENCES CursoMateriaProfesor(id_Relacion) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula)ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (id_Examen) REFERENCES Examen(id_Examen) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Administrativo
(id_administrativo char (10),
nombres varchar(100),
apellidos varchar(100),
usuario varchar (10),
contrasenia varchar (16),
PRIMARY KEY (id_administrativo)
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
CONSTRAINT CHECK(sexo in ('Masculino','Femenino')),
PRIMARY KEY (cedula)
);

CREATE TABLE PersonaEstudiante
(cedulaPersona char (10),
numMatricula integer,
tipoPersona varchar(20),
CONSTRAINT CHECK(tipoPersona in ('Padre','Madre','Representante')),
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula),
FOREIGN KEY (CedulaPersona) REFERENCES Persona(cedula)
);


CREATE TABLE PersonaFactura
(cedula char (10),
nombre varchar (100),
apellido varchar (100),
telefono char (6),
Direccion varchar (50),
CONSTRAINT CHECK(sexo in ('Masculino','Femenino')),
PRIMARY KEY (cedula)
);

CREATE TABLE Factura
(id_Factura int,
cedula char (10),
fecha date,
valor float(2),
PRIMARY KEY (id_Factura),
FOREIGN KEY (cedula) REFERENCES PersonaFactura(cedula)
);

CREATE TABLE Deuda(
id_Deuda integer,
descripcion varChar(50),
valor double,
id_Factura integer,
numMatricula integer,
PRIMARY KEY (id_Deuda),
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (id_Factura) REFERENCES Factura(id_Factura) ON UPDATE CASCADE ON DELETE CASCADE
);


DELIMITER $$
CREATE TRIGGER crearQuimestresAutomaticamente 
    AFTER INSERT ON MateriaEstudianteQuimestre
    FOR EACH ROW BEGIN
	INSERT INTO Quimestre(numQuimestre,notaQuimestre,id_MatEstQui)
	VALUES (1,0.00,new.id_MatEsQui);
	INSERT INTO Quimestre(numQuimestre,notaQuimestre,id_MatEstQui)
	VALUES (2,0.00,new.id_MatEsQui);

END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER crearParcialesAutomaticamente 
    AFTER INSERT ON Quimestre
    FOR EACH ROW BEGIN
	INSERT INTO Parcial(numParcial,notaParcial,id_Quimestre) 
	VALUES (1,0.00,new.id_Quimestre);
	INSERT INTO Parcial(numParcial,notaParcial,id_Quimestre) 
	VALUES (2,0.00,new.id_Quimestre);
	INSERT INTO Parcial(numParcial,notaParcial,id_Quimestre) 
	VALUES (3,0.00,new.id_Quimestre);
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER crearActividadesPorParcial
    AFTER INSERT ON Parcial
    FOR EACH ROW BEGIN
	INSERT INTO Actividad VALUES(1,0.00,"En Grupo",id_parcial);
	INSERT INTO Actividad VALUES(2,0.00,"Individual ",id_parcial);
	INSERT INTO Actividad VALUES(3,0.00,"En Clase",id_parcial);
	INSERT INTO Actividad VALUES(4,0.00,"Leccion",id_parcial);
	INSERT INTO Actividad VALUES(5,0.00,"Examen",id_parcial);
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER crearEstudiante
    AFTER INSERT ON Estudiante
    FOR EACH ROW BEGIN
	INSERT INTO PersonaEstudiante VALUES(NULL,new.numMatricula,'Padre');
	INSERT INTO PersonaEstudiante VALUES(NULL,new.numMatricula,'Madre');
	INSERT INTO PersonaEstudiante VALUES(NULL,new.numMatricula,'Representante');

END$$
DELIMITER ;


DELIMITER //
CREATE PROCEDURE crearActividad(nota double, tipo varchar(20),qui integer)
BEGIN
	Insert Into Actividad(id_Actividad,notaActividad,tipoActividad,id_Quimestre) 
	values(nota,tipo,qui);
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE actualizarActividad(id integer,nota double, tipo varchar(20),qui integer)
BEGIN
	update Actividad 
	set notaActividad=nota,tipoActividad=tipo,id_Quimestre=qui 
	where id_Actividad=id;
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE eliminarActividad(id integer)
BEGIN
	delete from Actividad
	where id_Actividad=id;
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE crearParcial(num integer,nota double,id_q integer)
BEGIN
	
	Insert Into Parcial(id_Parcial,numParcial,notaParcial,id_Quimestre) 
	values(num,nota,id_q);
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE actualizarParcial(id integer,num integer,nota double,id_q integer)
BEGIN
	
	update Parcial 
	set numParcial=num,notaParcial=nota,id_Quimestre=id_q 
	where id_Parcial=id;
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE eliminarParcial(id integer)
BEGIN
	delete from Parcial
	where id_Parcial=id;
  
END //
DELIMITER ;




DELIMITER //
CREATE PROCEDURE consultarEstudiante()
BEGIN
	SELECT * FROM Estudiante;
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE consultarEstudiante2()
BEGIN
	SELECT numMatricula,cedula,nombres,apellidos FROM Estudiante;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE consultarPersonas()
BEGIN
	SELECT * FROM Persona;
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE consultarCursos()
BEGIN
	SELECT * FROM Curso;
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE consultarProfesor()
BEGIN
	SELECT cedula,nombres,apellidos FROM Profesor;
  
END //
DELIMITER ;


DELIMITER $$
CREATE TRIGGER validacionProfesor
    BEFORE INSERT ON Profesor
    FOR EACH ROW BEGIN
	declare msg varChar(20);
	declare flagCedula boolean;
	CALL validarCedula(new.cedula,@flagCedula);
    if (select @flagCedula=false ) then
		set msg = concat('Cedula Invalida');
        signal sqlstate '45000' set message_text = msg;
    end if;
END$$
DELIMITER ;

DELIMITER //
CREATE PROCEDURE validarCedula(IN cedula char(10),OUT flag boolean)
BEGIN
    if ( length(cedula)=10 ) then
		set flag=true;
	else
		set flag=false;
    end if;
END //
DELIMITER ;

DELIMITER $$
CREATE TRIGGER validacionEstudiante
    BEFORE INSERT ON Estudiante
    FOR EACH ROW BEGIN
	declare msg varChar(20);
	declare flagCedula boolean;
	CALL validarCedula(new.cedula,@flagCedula);
    if (select @flagCedula=false ) then
		set msg = concat('Cedula Invalida');
        signal sqlstate '45000' set message_text = msg;
    end if;
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER validacionPersona
    BEFORE INSERT ON Persona
    FOR EACH ROW BEGIN
	declare msg varChar(20);
	declare flagCedula boolean;
	CALL validarCedula(new.cedula,@flagCedula);
    if (select @flagCedula=false ) then
		set msg = concat('Cedula Invalida');
        signal sqlstate '45000' set message_text = msg;
    end if;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER validacionPersonaFactura
    BEFORE INSERT ON PersonaFactura
    FOR EACH ROW BEGIN
	declare msg varChar(20);
	declare flagCedula boolean;
	CALL validarCedula(new.cedula,@flagCedula);
    if (select @flagCedula=false ) then
		set msg = concat('Cedula Invalida');
        signal sqlstate '45000' set message_text = msg;
    end if;
END$$
DELIMITER ;

DELIMITER //
CREATE PROCEDURE consultarCursosDelProfesor(IN usuarioProfesor char(10))
BEGIN
	SELECT numCurso,anoLectivo,paralelo FROM Profesor,Curso WHERE Curso.cedulaProfesor=Profesor.cedula and usuario=usuarioProfesor;
END //
DELIMITER ;


CREATE VIEW Lista As(Select Estudiante.nombres, Estudiante.apellidos,Curso.numCurso,
Curso.anoLectivo,Curso.paralelo
From Estudiante,Curso,CursoEstudiante
Where Estudiante.numMatricula=CursoEstudiante.numMatricula 
and Curso.id_Curso=CursoEstudiante.id_Curso);


CREATE VIEW PromedioMateria
As (Select E.nombres,E.apellidos,C.numCurso,C.anoLectivo,
C.paralelo,M.nombre as materia, avg(Q.notaQuimestre) as promedio
From Estudiante as E, MateriaEstudianteQuimestre as MEQ, 
Quimestre as Q, CursoMateriaProfesor as CM,Curso as C,
Materia as M 
Where E.numMatricula=MEQ.numMatricula and MEQ.id_MatEsQui=Q.id_MatEstQui
and MEQ.id_relacion=CM.id_relacion and CM.id_Curso=C.id_Curso
and M.id_Materia=CM.id_Materia
Group By (MEQ.id_MatEsQui)
);

CREATE VIEW notaParcial
As (Select E.nombres,E.apellidos,C.numCurso,C.anoLectivo,
C.paralelo,M.nombre as materia,Q.numQuimestre as Quimestre ,
P.numParcial as Parcial, P.notaParcial as nota 
From Estudiante as E, MateriaEstudianteQuimestre as MEQ, 
Quimestre as Q, CursoMateriaProfesor as CM,Curso as C,
Materia as M, Parcial as P
Where E.numMatricula=MEQ.numMatricula and MEQ.id_MatEsQui=Q.id_MatEstQui
and MEQ.id_relacion=CM.id_relacion and CM.id_Curso=C.id_Curso
and M.id_Materia=CM.id_Materia and P.id_Quimestre=Q.id_Quimestre
);



#Procedimientos acerca de Estudiantes
DELIMITER //
CREATE PROCEDURE consultarEstudiante()
BEGIN
	SELECT * FROM Estudiante;
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertarEstudiante(in cedula char(10),in nombres varchar(100),
in apellidos varchar(100), in sexo varchar(10), in estadoCivil varchar(25),
in origen varchar(30), in Etnia varchar(20),in fechaNacimiento date )
BEGIN
	
INSERT INTO Estudiante (cedula, nombres,apellidos, sexo, estadoCivil,origen
,Etnia, fechaNacimiento) VALUES(cedula, nombres, apellidos,
sexo, estadoCivil,origen, Etnia, fechaNacimiento);
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE editarEstudiante(in numMatricula int, in cedula char(10),in nombres varchar(100),
in apellidos varchar(100), in sexo varchar(10), in estadoCivil varchar(25),
in origen varchar(30), in Etnia varchar(20),in fechaNacimiento date )
BEGIN
	
UPDATE Estudiante SET cedula = cedula, nombres= nombres,apellidos= apellidos
, sexo= sexo, estadoCivil= estadoCivil,origen= origen
,Etnia= Etnia, fechaNacimiento= fechaNacimiento where (Estudiante.numMatricula= numMatricula);
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE eliminarEstudiante(in numMatricula int)
BEGIN
	
DELETE FROM Estudiante WHERE(Estudiante.numMatricula= numMatricula);
  
END //
DELIMITER ;


#Procedimientos acerca de las Personas
DELIMITER //
CREATE PROCEDURE consultarPersonas()
BEGIN
	SELECT * FROM Persona;
  
END //
DELIMITER ;







DELIMITER //
CREATE PROCEDURE InsertarProfesor(in cedula char(10),in nombres varchar(100),
in apellidos varchar(100), in usuario varchar(10), in clave varchar(16))
BEGIN
	
INSERT INTO Profesor VALUES(cedula, nombres, apellidos,usuario,clave);
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE editarProfesor(in cedula char(10),in nombres varchar(100),
in apellidos varchar(100), in usuario varchar(10), in clave varchar(16))
BEGIN
	
UPDATE Profesor SET cedula= cedula, nombres= nombres, apellidos= apellidos,
usuario= usuario, contrasenia = clave WHERE (Profesor.cedula= cedula);
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE eliminarProfesor(in cedula char(10))
BEGIN
	
DELETE FROM Profesor WHERE (Profesor.cedula= cedula);
  
END //
DELIMITER ;


#Prosedimientos para las personas de las facturas

DELIMITER //
CREATE PROCEDURE consultarPersonaFactura()
BEGIN
	
select * from PersonaFactura;
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertarPersonaFactura(in cedula char(10),in nombre varchar(100),
in apellido varchar(100), in telefono char(6), in Direccion varchar(50))
BEGIN
	
INSERT INTO PersonaFactura VALUES(cedula, nombre, apellido,telefono,Direccion);
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE EditarPersonaFactura(in cedula char(10),in nombre varchar(100),
in apellido varchar(100), in telefono char(6), in Direccion varchar(50))
BEGIN
	
UPDATE PersonaFactura SET cedula= cedula, nombre=nombre, apellido=apellido,
telefono= telefono, Direccion= Direccion WHERE (PersonaFactura.cedula = cedula);
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE eliminarPersonaFactura(in cedula char(10))
BEGIN
	
Delete from PersonaFactura where cedula= cedula;
  
END //
DELIMITER ;
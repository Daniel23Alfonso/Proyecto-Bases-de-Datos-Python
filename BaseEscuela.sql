Create DataBase BaseEscuela;
use BaseEscuela;


CREATE TABLE PersonaFactura
(cedula char (10),
nombre varchar (100),
apellido varchar (100),
telefono char (10),
Direccion varchar (50),
CONSTRAINT CHECK(sexo in ('Masculino','Femenino')),
PRIMARY KEY (cedula)
);

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
id_Curso integer AUTO_INCREMENT,
numCurso enum('Kinder','Primero','Segundo','Tercero','Cuarto','Quinto','Sexto','Septimo'),
anoLectivo varChar(10),
paralelo varchar(2),
cedulaProfesor char(10),
PRIMARY KEY (id_Curso),
FOREIGN KEY (cedulaProfesor) REFERENCES Profesor(cedula) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Estudiante
(numMatricula integer AUTO_INCREMENT,
cedula char (10),
nombres varchar(100),
apellidos varchar(100),
sexo varchar(10),
estadoCivil varchar (25),
origen varchar (30),
Etnia varchar (20),
fechaNacimiento date,
cedulaFactura char(10),
CONSTRAINT CHECK(sexo in ('Masculino','Femenino')),
PRIMARY KEY (numMatricula),
FOREIGN KEY (cedulaFactura) REFERENCES PersonaFactura(cedula) ON DELETE CASCADE ON UPDATE CASCADE,
UNIQUE (cedula)
);


CREATE TABLE Materia(
id_Materia integer,
Nombre varChar(20),
PRIMARY KEY (id_Materia),
UNIQUE (Nombre)
);


CREATE TABLE CursoMateriaProfesor(
id_Relacion integer AUTO_INCREMENT ,
id_Curso integer,
id_Materia integer,
CedulaProfesor varChar(10),
PRIMARY KEY (id_Relacion),
FOREIGN KEY (id_Curso) REFERENCES Curso(id_Curso) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (id_Materia) REFERENCES Materia(id_Materia) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (CedulaProfesor) REFERENCES Profesor(cedula) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE MateriaEstudianteQuimestre
(id_MatEsQui integer AUTO_INCREMENT,
id_relacion integer,
numMatricula integer,
PRIMARY KEY (id_MatEsQui),
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula)ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (id_relacion) REFERENCES CursoMateriaProfesor(id_Relacion) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Quimestre(
id_Quimestre integer AUTO_INCREMENT,
numQuimestre integer,
notaQuimestre numeric(4,2),
notaExamen numeric(4,2),
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

CREATE TABLE MateriaExamenEstudiante(
id_MatExamenEst integer AUTO_INCREMENT,
id_Relacion integer,
numMatricula integer,
PRIMARY KEY (id_MatExamenEst),
FOREIGN KEY (id_relacion) REFERENCES CursoMateriaProfesor(id_Relacion) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula)ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Examen (
id_Examen integer AUTO_INCREMENT,
notaExamen numeric(4,2),
tipoExamen varchar(30),
id_MatExamenEst integer,
CONSTRAINT c_notas CHECK (notaExamen>= 0.00 and notaExamen <= 10.00),
PRIMARY KEY  (id_Examen),
FOREIGN KEY (id_MatExamenEst) REFERENCES MateriaExamenEstudiante(id_MatExamenEst)ON DELETE CASCADE ON UPDATE CASCADE
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
PRIMARY KEY (cedula),
CONSTRAINT CHECK(sexo in ('Masculino','Femenino'))
);

CREATE TABLE CursoEstudiante(
id_Curso integer,
numMatricula integer,
PRIMARY KEY(id_Curso,numMatricula),
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (id_Curso) REFERENCES Curso(id_Curso) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PersonaEstudiante
(cedulaPersona char (10),
numMatricula integer,
tipoPersona enum ('Padre','Madre','Representante'),
PRIMARY KEY (cedulaPersona , numMatricula),
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (cedulaPersona) REFERENCES Persona(cedula) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Factura
(id_Factura integer AUTO_INCREMENT,
fecha date,
valor float(2),
PRIMARY KEY (id_Factura)
);

CREATE TABLE Deuda(
id_Deuda integer AUTO_INCREMENT,
descripcion enum('Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','Enero','Febrero'),
valor double,
id_Factura integer,
numMatricula integer,
PRIMARY KEY (id_Deuda),
FOREIGN KEY (numMatricula) REFERENCES Estudiante(numMatricula) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (id_Factura) REFERENCES Factura(id_Factura) ON UPDATE CASCADE ON DELETE CASCADE
);


#--------------------------------------------------------------------------#

#TRIGGERS

DELIMITER $$
CREATE TRIGGER crearMateriasDeUnCurso
    AFTER INSERT ON Curso
    FOR EACH ROW BEGIN
		call insertarMateriasPorCurso(new.id_Curso,new.numCurso);
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER crearQuimestresAutomaticamente 
    AFTER INSERT ON MateriaEstudianteQuimestre
    FOR EACH ROW BEGIN
	call crearQuimestre(1,0.00,0.00,new.id_MatEsQui);
	call crearQuimestre(2,0.00,0.00,new.id_MatEsQui);

END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER crearExamenesAutomaticamente 
    AFTER INSERT ON MateriaExamenEstudiante
    FOR EACH ROW BEGIN
	call crearExamen(new.id_MatExamenEst,0.00,"Supletorio");
	call crearExamen(new.id_MatExamenEst,0.00,"Remedial");
	call crearExamen(new.id_MatExamenEst,0.00,"De Gracia");
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER crearParcialesAutomaticamente 
    AFTER INSERT ON Quimestre
    FOR EACH ROW BEGIN
	call crearParcial(1, 0.00, new.id_Quimestre );
	call crearParcial(2,0.00,new.id_Quimestre );
	call crearParcial(3,0.00,new.id_Quimestre );
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER validarNotaQuimestre
    AFTER UPDATE ON Quimestre
    FOR EACH ROW BEGIN
	declare msg varChar(20);
	declare flag boolean;
	call validarNotas(new.notaExamen,@flag);
    if (select @flag=false) then
		set msg = concat('Nota Invalida');
        signal sqlstate '45000' set message_text = msg;
    end if;
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER crearActividadesPorParcial
    AFTER INSERT ON Parcial
    FOR EACH ROW BEGIN
	call crearActividad(0.00,"En Grupo",new.id_Parcial);
	call crearActividad(0.00,"Individual ",new.id_Parcial);
	call crearActividad(0.00,"En Clase",new.id_Parcial);
	call crearActividad(0.00,"Leccion",new.id_Parcial);
	call crearActividad(0.00,"Examen",new.id_Parcial);

END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER validarNotaActividad
    BEFORE UPDATE ON Actividad
    FOR EACH ROW BEGIN
	declare msg varChar(20);
	declare flag boolean;
	call validarNotas(new.notaActividad,@flag);
    if (select @flag=false) then
		set msg = concat('Nota Invalida');
        signal sqlstate '45000' set message_text = msg;
    end if;
END$$
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

DELIMITER $$
CREATE TRIGGER ligarEstudianteQuimestre
    AFTER INSERT ON CursoEstudiante
    FOR EACH ROW BEGIN
		call insertarMateriaEstudianteQuimestre(new.id_Curso,new.numMatricula);
		call insertarMateriaExamenEstudiante(new.id_Curso,new.numMatricula);
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER generarDeudas
	AFTER INSERT ON Estudiante
	FOR EACH ROW BEGIN
	
	call crearDeuda(1,30.00,new.numMatricula);
	call crearDeuda(2,30.00,new.numMatricula);
	call crearDeuda(3,30.00,new.numMatricula);
	call crearDeuda(4,30.00,new.numMatricula);
	call crearDeuda(5,30.00,new.numMatricula);
	call crearDeuda(6,30.00,new.numMatricula);
	call crearDeuda(7,30.00,new.numMatricula);
	call crearDeuda(8,30.00,new.numMatricula);
	call crearDeuda(9,30.00,new.numMatricula);
	call crearDeuda(10,30.00,new.numMatricula);
	
END $$
DELIMITER ;


#--------------------------------------------------------------------------------#
#VISTAS

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


CREATE VIEW cursosDeEstudiantes AS(
SELECT Curso.id_Curso,Estudiante.numMatricula,Estudiante.apellidos,Estudiante.nombres,
Materia.id_Materia,Materia.Nombre as materia,
Quimestre.id_Quimestre,Quimestre.numQuimestre,Quimestre.notaQuimestre,Quimestre.notaExamen as examenQuimestre,
Parcial.id_Parcial,Parcial.numParcial,Parcial.notaParcial,
Actividad.tipoActividad,Actividad.notaActividad
FROM CursoMateriaProfesor,Curso,Estudiante,MateriaEstudianteQuimestre,Materia,Quimestre,Parcial,Actividad
WHERE CursoMateriaProfesor.id_Relacion=MateriaEstudianteQuimestre.id_relacion
and CursoMateriaProfesor.id_Materia=Materia.id_Materia
and CursoMateriaProfesor.id_Curso=Curso.id_Curso
and MateriaEstudianteQuimestre.numMatricula=Estudiante.numMatricula
and MateriaEstudianteQuimestre.id_MatEsQui=Quimestre.id_MatEstQui
and Quimestre.id_Quimestre=Parcial.id_Quimestre
and Parcial.id_Parcial=Actividad.id_Parcial
order by Curso.id_Curso,Estudiante.apellidos, Materia.Nombre
);

#--------------------------------------------------------------------#

#PROCEDIMIENTOS

#procedimientos actividades
DELIMITER //
CREATE PROCEDURE crearActividad(in nota numeric(4,2),in tipo varchar(20), in id_Parcial integer)
BEGIN
	Insert Into Actividad(notaActividad,tipoActividad,id_Parcial) 
	values(nota,tipo,id_Parcial);
  
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

#procedimientos parciales


DELIMITER //
CREATE PROCEDURE crearParcial(in numParcial integer, in notaParcial numeric(4,2), in id_Quimestre integer)
BEGIN
	INSERT INTO Parcial(numParcial, notaParcial, id_Quimestre)
	VALUES (numParcial, notaParcial, id_Quimestre);
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


#Procedimientos de los Cursos

DELIMITER //
CREATE PROCEDURE consultarCursos()
BEGIN
	SELECT * FROM Curso;
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE consultarCursosDelProfesor(IN usuarioProfesor char(10))
BEGIN
SELECT Materia.Nombre,Curso.id_curso,Curso.numCurso,Curso.paralelo,Curso.anoLectivo 
FROM CursoMateriaProfesor,Profesor,Curso,Materia WHERE usuarioProfesor=Profesor.usuario 
and Profesor.cedula=CursoMateriaProfesor.cedulaProfesor 
and CursoMateriaProfesor.id_Curso=Curso.id_Curso 
and CursoMateriaProfesor.id_Materia=Materia.id_Materia;
END //
DELIMITER ;

#Procedimientos acerca de Estudiantes
DELIMITER //
CREATE PROCEDURE consultarEstudiante()
BEGIN
	SELECT numMatricula, cedula, nombres, apellidos, sexo, estadoCivil, origen, Etnia, fechaNacimiento  
	FROM Estudiante;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE consultarEstudiante2()
BEGIN
	SELECT numMatricula,cedula,nombres,apellidos FROM Estudiante;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insertarMateriaEstudianteQuimestre(in id_curso integer,in numMatricula integer)
BEGIN
	Insert Into MateriaEstudianteQuimestre(id_Relacion,numMatricula) 
	SELECT id_Relacion,numMatricula 
	FROM CursoMateriaProfesor,CursoEstudiante 
	WHERE CursoMateriaProfesor.id_Curso=CursoEstudiante.id_Curso 
	and CursoEstudiante.id_Curso=id_curso 
	and CursoEstudiante.numMatricula=numMatricula;		
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insertarMateriaExamenEstudiante(in id_curso integer,in numMatricula integer)
BEGIN
	Insert Into MateriaExamenEstudiante(id_Relacion,numMatricula)
	SELECT id_Relacion,numMatricula 
	FROM CursoMateriaProfesor,CursoEstudiante 
	WHERE CursoMateriaProfesor.id_Curso=CursoEstudiante.id_Curso 
	and CursoEstudiante.id_Curso=id_curso 
	and CursoEstudiante.numMatricula=numMatricula;
END //
DELIMITER ;
#procedimiento para consultar las notas de los examenes de un curso (supletorio,remedial,gracia)
DELIMITER //
CREATE PROCEDURE consultarExamenesPorCurso(in id_curso integer,in materia varchar(20))
BEGIN
SELECT Estudiante.numMatricula,Estudiante.apellidos,Estudiante.nombres,Examen.tipoExamen,Examen.notaExamen
FROM MateriaExamenEstudiante,CursoMateriaProfesor,Estudiante,Examen,Materia,Curso
WHERE MateriaExamenEstudiante.id_Relacion=CursoMateriaProfesor.id_Relacion
and CursoMateriaProfesor.id_Materia=Materia.id_Materia
and CursoMateriaProfesor.id_Curso=Curso.id_Curso
and MateriaExamenEstudiante.numMatricula=Estudiante.numMatricula
and MateriaExamenEstudiante.id_MatExamenEst=Examen.id_MatExamenEst 
and Curso.id_Curso=id_curso
and Materia.Nombre=materia
order by Estudiante.apellidos
;
END //
DELIMITER ;

#procedimiento para consultar las notas de las actividades de un curso en un materia de un quimestre y un parcial en particular
DELIMITER //
CREATE PROCEDURE consultarEstudiantesPorMateria(IN id_curso integer,IN materia varchar(20),IN quimestre integer,IN parcial integer)
BEGIN	
	SELECT cursosDeEstudiantes.numMatricula,cursosDeEstudiantes.apellidos,cursosDeEstudiantes.nombres,
	cursosDeEstudiantes.tipoActividad, cursosDeEstudiantes.notaActividad
	FROM cursosDeEstudiantes
	WHERE cursosDeEstudiantes.id_Curso=id_Curso
	and cursosDeEstudiantes.materia=materia
	and cursosDeEstudiantes.numQuimestre=quimestre
	and cursosDeEstudiantes.numParcial=parcial
	order by cursosDeEstudiantes.apellidos, cursosDeEstudiantes.tipoActividad
	;
END //
DELIMITER ;


#actualizar el promedio del parcial

DELIMITER //
CREATE PROCEDURE actualizarNotasParcial(IN id_Curso integer,IN materia varchar(20),
IN quimestre integer,IN parcial integer,IN matricula integer)
BEGIN
SELECT distinct (cursosDeEstudiantes.id_Parcial) INTO@parcial FROM cursosDeEstudiantes 
WHERE cursosDeEstudiantes.id_Curso=id_Curso
and cursosDeEstudiantes.numMatricula=matricula
and cursosDeEstudiantes.numQuimestre=quimestre
and cursosDeEstudiantes.numParcial=parcial
and cursosDeEstudiantes.materia=materia;
call calcularNotaParcial(@parcial);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE calcularNotaParcial(IN id_Parcial integer)
BEGIN
	SELECT sum(Actividad.notaActividad)INTO @nota
	FROM Parcial,Actividad
	WHERE Parcial.id_Parcial=Actividad.id_Parcial
	and Parcial.id_Parcial=id_Parcial
	group by Parcial.id_Parcial;
	UPDATE Parcial SET Parcial.notaParcial=(@nota)/5 WHERE Parcial.id_Parcial=id_Parcial;
END //
DELIMITER ;


#actualizar promedio del quimestre
DELIMITER //
CREATE PROCEDURE actualizarNotaQuimestre(IN id_Curso integer,IN materia varchar(20),
IN quimestre integer,IN matricula integer)
BEGIN
SELECT distinct (cursosDeEstudiantes.id_Quimestre) INTO@idQuimestre FROM cursosDeEstudiantes
WHERE cursosDeEstudiantes.id_Curso=id_Curso
and cursosDeEstudiantes.numMatricula=matricula
and cursosDeEstudiantes.materia=materia
and cursosDeEstudiantes.numQuimestre=quimestre;
call calcularNotaQuimestre(@idQuimestre);
END //
DELIMITER //;

DELIMITER //
CREATE PROCEDURE calcularNotaQuimestre(IN id_Quimestre integer)
BEGIN
SELECT (avg(Parcial.notaParcial)*0.8+(Quimestre.notaExamen)*0.2) INTO@Promedio
FROM Quimestre,Parcial
WHERE Quimestre.id_Quimestre=Parcial.id_Quimestre 
and Quimestre.id_Quimestre=id_Quimestre
group by Quimestre.id_Quimestre;
UPDATE Quimestre SET Quimestre.notaQuimestre=(@Promedio) WHERE Quimestre.id_Quimestre=id_Quimestre;
END //
DELIMITER ;



#procedimiento para actualizar la nota de un estudiante en una actividad de un curso
DELIMITER //
CREATE PROCEDURE actualizarEstudianteActividad
(IN id_curso integer,IN materia varchar(20),IN quimestre integer,
IN parcial integer,IN tipoActividad varchar(20),IN matricula integer,IN nota integer)
BEGIN
UPDATE Actividad SET Actividad.notaActividad=nota WHERE Actividad.id_Actividad in ( Select * FROM(
SELECT Actividad.id_Actividad
FROM MateriaEstudianteQuimestre,Estudiante,CursoMateriaProfesor,Curso,Materia,Quimestre,Parcial,Actividad
WHERE MateriaEstudianteQuimestre.numMatricula=Estudiante.numMatricula and
	MateriaEstudianteQuimestre.id_Relacion=CursoMateriaProfesor.id_Relacion and
	CursoMateriaProfesor.id_Curso=Curso.id_Curso and
	CursoMateriaProfesor.id_Materia=Materia.id_Materia and
	MateriaEstudianteQuimestre.id_MatEsQui=Quimestre.id_MatEstQui and
	Quimestre.id_Quimestre=Parcial.id_Quimestre and
	Parcial.id_Parcial=Actividad.id_Parcial and
	Curso.id_Curso=id_Curso and
	Quimestre.numQuimestre=quimestre and
	Parcial.numParcial=parcial and
	Materia.Nombre=materia and
	Actividad.tipoActividad=tipoActividad and
	Estudiante.numMatricula=matricula
)as result );

END //
DELIMITER ;


#procedimiento para consultar las notas de los examenes del quimestre de los estudiantes de un curso de un materia en un quimestre
DELIMITER //
CREATE PROCEDURE consultarExamenPorQuimestre(IN id_curso integer,IN materia varchar(20),IN quimestre integer)
BEGIN
	SELECT distinct(cursosDeEstudiantes.numMatricula),cursosDeEstudiantes.apellidos,cursosDeEstudiantes.nombres,
	cursosDeEstudiantes.examenQuimestre,cursosDeEstudiantes.notaQuimestre
	FROM cursosDeEstudiantes	
	WHERE cursosDeEstudiantes.id_Curso=id_Curso
	and cursosDeEstudiantes.materia=materia
	and cursosDeEstudiantes.numQuimestre=quimestre
	order by cursosDeEstudiantes.apellidos;
END //
DELIMITER ;

#procedimiento para actualizar la nota del examen de un estudiante
DELIMITER //
CREATE PROCEDURE actualizarExamenPorQuimestre(IN id_curso integer,IN materia varchar(20),IN quimestre integer,IN matricula integer,IN notaExamen integer)
BEGIN
	UPDATE Quimestre SET Quimestre.notaExamen=notaExamen
	WHERE Quimestre.id_Quimestre in(SELECT * FROM(
	SELECT Quimestre.id_Quimestre
	FROM MateriaEstudianteQuimestre,Estudiante,CursoMateriaProfesor,Curso,Materia,Quimestre
	WHERE MateriaEstudianteQuimestre.numMatricula=Estudiante.numMatricula and
	MateriaEstudianteQuimestre.id_Relacion=CursoMateriaProfesor.id_Relacion and
	CursoMateriaProfesor.id_Curso=Curso.id_Curso and
	CursoMateriaProfesor.id_Materia=Materia.id_Materia and
	MateriaEstudianteQuimestre.id_MatEsQui=Quimestre.id_MatEstQui
	and Estudiante.numMatricula=matricula
	and Curso.id_Curso=id_curso
	and Materia.nombre=materia
	and Quimestre.numQuimestre=quimestre
	order by Estudiante.apellidos) as result
);
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE consultarNotasParcial(IN id_Curso integer,IN materia varchar(20),IN quimestre integer)
BEGIN
Select  distinct (notasPrimerParcial.numMatricula),notasPrimerParcial.Apellidos,notasPrimerParcial.nombres,
notasPrimerParcial.notaParcial,notasSegundoParcial.notaParcial,notasTercerParcial.notaParcial
FROM
(select distinct (cursosDeEstudiantes.numMatricula),nombres,apellidos,notaParcial from cursosDeEstudiantes
where cursosDeEstudiantes.numQuimestre=quimestre 
and cursosDeEstudiantes.id_Curso=id_Curso 
and cursosDeEstudiantes.numParcial=1 
and cursosDeEstudiantes.materia=materia)as notasPrimerParcial,
(select distinct (cursosDeEstudiantes.numMatricula),nombres,apellidos,notaParcial from cursosDeEstudiantes
where cursosDeEstudiantes.numQuimestre=quimestre 
and cursosDeEstudiantes.id_Curso=id_Curso 
and cursosDeEstudiantes.numParcial=2
and cursosDeEstudiantes.materia=materia)as notasSegundoParcial,
(select distinct (cursosDeEstudiantes.numMatricula),nombres,apellidos,notaParcial from cursosDeEstudiantes
where cursosDeEstudiantes.numQuimestre=quimestre 
and cursosDeEstudiantes.id_Curso=id_Curso 
and cursosDeEstudiantes.numParcial=3
and cursosDeEstudiantes.materia=materia)as notasTercerParcial
WHERE notasPrimerParcial.numMatricula=notasSegundoParcial.numMatricula and notasSegundoParcial.numMatricula=notasTercerParcial.numMatricula
order by notasPrimerParcial.Apellidos;
END //
DELIMITER ;


Select  distinct (notasPrimerParcial.numMatricula),notasPrimerParcial.Apellidos,notasPrimerParcial.nombres,
notasPrimerParcial.notaParcial,notasSegundoParcial.notaParcial,notasTercerParcial.notaParcial
FROM
(select distinct (numMatricula),nombres,apellidos,notaParcial from cursosDeEstudiantes
where numQuimestre=1 and id_Curso=4 and numParcial=1 and materia="EDUCACION FISICA"
)as notasPrimerParcial,
(select distinct (numMatricula),nombres,apellidos,notaParcial from cursosDeEstudiantes
where numQuimestre=1 and id_Curso=4 and numParcial=2 and materia="EDUCACION FISICA"
)as notasSegundoParcial,
(select distinct (numMatricula),nombres,apellidos,notaParcial from cursosDeEstudiantes
where numQuimestre=1 and id_Curso=4 and numParcial=3 and materia="EDUCACION FISICA"
)as notasTercerParcial
WHERE notasPrimerParcial.numMatricula=notasSegundoParcial.numMatricula
and notasSegundoParcial.numMatricula=notasTercerParcial.numMatricula
order by notasPrimerParcial.Apellidos;



DELIMITER //
CREATE PROCEDURE InsertarEstudiante(in cedula char(10),in nombres varchar(100),
in apellidos varchar(100), in sexo varchar(10), in estadoCivil varchar(25),
in origen varchar(30), in Etnia varchar(20),in fechaNacimiento date,in cedFac char(10) )
BEGIN
	
INSERT INTO Estudiante (cedula, nombres,apellidos, sexo, estadoCivil,origen
,Etnia, fechaNacimiento,cedulaFactura) VALUES(cedula, nombres, apellidos,
sexo, estadoCivil,origen, Etnia, fechaNacimiento,cedFac);
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE editarEstudiante(in numMatricula int, in cedula char(10),in nombres varchar(100),
in apellidos varchar(100), in sexo varchar(10), in estadoCivil varchar(25),
in origen varchar(30), in Etnia varchar(20),in fechaNacimiento date,in cedFac char(10) )
BEGIN
	
UPDATE Estudiante SET cedula = cedula, nombres= nombres,apellidos= apellidos
, sexo= sexo, estadoCivil= estadoCivil,origen= origen
,Etnia= Etnia, fechaNacimiento= fechaNacimiento,cedulaFactura=cedFac
 where (Estudiante.numMatricula= numMatricula);
  
END //
DELIMITER ;


#Este procedimiento sirve para buscar al padre, madre o representante de un estudinate
DELIMITER //
CREATE PROCEDURE EstudianteObtenerPersona(in numMatricula integer, in tipoPersona varchar(20))
BEGIN
	
select p.cedula, p.nombres, p.apellidos, p.sexo, p.fechaNacimiento,
	p.estadoCivil, p.ocupacion, p.lugarTrabajo, p.telefono, p.direccion from Persona p, Estudiante e, PersonaEstudiante pe
	where (e.numMatricula = numMatricula and  e.numMatricula = pe.numMatricula and pe.cedulaPersona = p.cedula and pe.tipoPersona = tipoPersona);
  
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE EstudianteObtenerPersonaFactura(in numMatricula integer)
BEGIN
	
select pf.cedula, pf.nombre, pf.apellido, pf.telefono, pf.Direccion from PersonaFactura pf, Estudiante e
	where (e.numMatricula= numMatricula and e.cedulaFactura = pf.cedula);
  
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
CREATE PROCEDURE crearPersonas(in ced char(10), in nom char(100), in ape char(100),
in sex char(10), in fecha date, in estado char(25),in ocup char(25), in ltrab char(100),
in telf char(6), in dir char(100))
BEGIN
	Insert into Persona VALUES(ced,nom,ape,sex,fecha,estado,ocup,ltrab,telf,dir);
  
END //
DELIMITER ;



DELIMITER //
CREATE PROCEDURE editarPersonas(in ced char(10), in nom char(100), in ape char(100),
in sex char(10), in fecha date, in estado char(25),in ocup char(25), in ltrab char(100),
in telf char(6), in dir char(100))
BEGIN

	UPDATE Persona set nombres= nom, apellidos=ape,sexo=sex,fechaNacimiento=fecha,
	estadoCivil=estado,ocupacion=ocup,lugarTrabajo=ltrab,telefono=telf,direccion=dir
	where Cedula=ced;
  
END //
DELIMITER ;
#Procedimientos acerca de profesores

DELIMITER //
CREATE PROCEDURE consultarProfesor()
BEGIN
	SELECT cedula,nombres,apellidos FROM Profesor;
  
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

DELIMITER //
CREATE PROCEDURE AsignarDirigente(IN cedula char(10),IN Curso integer)
BEGIN
    UPDATE Curso SET cedulaProfesor=cedula
	WHERE id_Curso=Curso;
END //
DELIMITER ;

#Procedimientos para las personas de las facturas

DELIMITER //
CREATE PROCEDURE consultarPersonaFactura()
BEGIN
	
select * from PersonaFactura;
  
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE InsertarPersonaFactura(in cedula char(10),in nombre varchar(100),
in apellido varchar(100), in telefono char(10), in Direccion varchar(50))
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


#Procedimientos Quimestre

DELIMITER //
CREATE PROCEDURE crearQuimestre(in numQuimestre integer, in notaQuimestre numeric(4,2), in notaExamen numeric(4,2), in id_MatEsQui integer)
BEGIN
	INSERT INTO Quimestre(numQuimestre,notaQuimestre,notaExamen,id_MatEstQui)
	VALUES (numQuimestre,notaQuimestre,notaExamen,id_MatEsQui);
END //
DELIMITER ;


#Procedimiento estudiantes curso

DELIMITER //
CREATE PROCEDURE agregarEstudianteEnCurso(in id_Curso integer, in numMatricula integer)
BEGIN
	select COUNT(*) INTO @contador from CursoEstudiante,Curso
	where Curso.id_Curso=CursoEstudiante.id_Curso and Curso.id_Curso=id_Curso
	and CursoEstudiante.numMatricula=numMatricula;
	if(select @contador=0) then
		INSERT INTO CursoEstudiante(id_Curso, numMatricula)
		VALUES (id_Curso, numMatricula);
	end if;
END //
DELIMITER ;

#Procedimientos de los Cursos

DELIMITER //
CREATE PROCEDURE crearCurso(IN num integer,IN anoL varChar(10))
BEGIN
	select count(*) INTO @contador from Curso 
	Where numCurso=num and anoLectivo=anoL;

	INSERT INTO Curso(numCurso, anoLectivo, paralelo,cedulaProfesor)
	VALUES (num, anoL,(select @contador)+1 ,NULL);
END //
DELIMITER ;




DELIMITER //
CREATE PROCEDURE crearExamen(IN id_MatExamenEst integer,in notaExamen numeric(4,2),IN tipoExamen varchar(20))
BEGIN
	INSERT INTO Examen(notaExamen,tipoExamen,id_MatExamenEst)
	VALUES (notaExamen,tipoExamen,id_MatExamenEst);
END //
DELIMITER ;



DELIMITER //
CREATE PROCEDURE actualizarCurso(IN curso integer,IN cedula char(10))
BEGIN
	UPDATE Curso SET cedulaProfesor=cedula WHERE (Curso.id_Curso=curso) ;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE ligarCursoConProfesor(IN Curso integer,IN Materia integer ,IN cedulaProfesor char(10))
BEGIN
	UPDATE CursoMateriaProfesor SET CedulaProfesor=cedulaProfesor	where(CursoMateriaProfesor.id_Curso=Curso and CursoMateriaProfesor.id_Materia=Materia);
END //
DELIMITER ;



DELIMITER //
CREATE PROCEDURE desligarCursoConProfesor(IN Curso integer,IN Materia integer ,IN cedulaProfesor char(10))
BEGIN
	UPDATE CursoMateriaProfesor SET CedulaProfesor=NULL	where(CursoMateriaProfesor.id_Curso=Curso and CursoMateriaProfesor.id_Materia=Materia and CursoMateriaProfesor.cedulaProfesor=cedulaProfesor);
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE crearMaterias()
BEGIN
	INSERT INTO Materia VALUES(0,"LENGUA Y LITERATURA");
	INSERT INTO Materia VALUES(1,"MATEMATICA");
	INSERT INTO Materia VALUES(2,"ENTORNO NATURAL");
	INSERT INTO Materia VALUES(3,"CIENCIAS NATURALES");
	INSERT INTO Materia VALUES(4,"ESTUDIOS SOCIALES");
	INSERT INTO Materia VALUES(5,"EDUCACION FISICA");
	INSERT INTO Materia VALUES(6,"LENGUA EXTRANJERA");	
	INSERT INTO Materia VALUES(7,"CLUBES");		
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE insertarMateriasPorCurso(IN idCurso integer,IN numCurso integer)
BEGIN
	if numCurso=0 then
		call insertMateriasKinder(idCurso);
	elseif numCurso=1 then
		call insertarMateriasPrimero(idCurso);
	elseif (numCurso=2 or numCurso=3) then
		call insertarMateriasSegundo(idCurso);
	else 
		call insertarMateriasMayores(idCurso);
	END IF;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE insertMateriasKinder(IN Curso integer)
BEGIN
	INSERT INTO CursoMateriaProfesor(id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,0,NULL);
	INSERT INTO CursoMateriaProfesor(id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,1,NULL);
	INSERT INTO CursoMateriaProfesor(id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,2,NULL);
	INSERT INTO CursoMateriaProfesor(id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,3,NULL);
	INSERT INTO CursoMateriaProfesor(id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,4,NULL);
	INSERT INTO CursoMateriaProfesor(id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,5,NULL);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insertarMateriasPrimero(IN Curso integer)
BEGIN
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,0,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,1,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,2,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,3,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,4,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,5,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,6,NULL);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insertarMateriasSegundo(IN Curso integer)
BEGIN
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,0,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,1,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,2,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,5,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,6,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,7,NULL);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insertarMateriasMayores(IN Curso integer)
BEGIN
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,0,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,1,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,3,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,4,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,5,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,6,NULL);
	INSERT INTO CursoMateriaProfesor (id_Curso,id_Materia,CedulaProfesor) VALUES(Curso,7,NULL);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerMateriasPorCurso(IN idCurso integer)
BEGIN
	SELECT Materia.id_Materia,Materia.Nombre 
	FROM CursoMateriaProfesor,Materia 
	WHERE  CursoMateriaProfesor.id_Materia=Materia.id_Materia 
	and CursoMateriaProfesor.id_Curso=idCurso 
	and CursoMateriaProfesor.CedulaProfesor IS NULL
	ORDER BY Materia.Nombre;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerMateriaCursoProfesor(IN idCurso integer)
BEGIN
	SELECT Materia.id_Materia,Materia.Nombre,Profesor.cedula,Profesor.Nombres,Profesor.apellidos FROM CursoMateriaProfesor,Materia,Profesor WHERE  CursoMateriaProfesor.CedulaProfesor IS NOT NULL and CursoMateriaProfesor.id_Curso=idCurso and CursoMateriaProfesor.id_Materia=Materia.id_Materia and CursoMateriaProfesor.CedulaProfesor=Profesor.cedula
	ORDER BY Materia.Nombre;
END//
DELIMITER ;


#Otros procedimientos:

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

DELIMITER //
CREATE PROCEDURE validarNotas(IN nota numeric(4,2),OUT flag boolean)
BEGIN
    if ((nota>=0)and(nota<=10)) then
		set flag=true;
	else
		set flag=false;
    end if;
END //
DELIMITER ;

#Procedimientos del profesor
DELIMITER //
CREATE PROCEDURE mostrarInfoProfesor(IN cedula char(10))
BEGIN
    SELECT * FROM Profesor Where Profesor.cedula=cedula;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE existeUsuario(IN user char(10))
BEGIN
    SELECT * FROM Profesor Where Profesor.usuario=user; 
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE existeUsuarioRepetido(IN cedula char(10),In user char(10))
BEGIN
    SELECT * FROM Profesor Where Profesor.cedula<>cedula and Profesor.usuario=user; 
END //
DELIMITER ;


#Procedimiento Factura

DELIMITER //
CREATE PROCEDURE obtenerDeudas(IN matricula integer)
BEGIN
	SELECT * FROM Deuda
	WHERE numMatricula=matricula and  id_Factura IS NULL
	ORDER BY descripcion;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE crearDeuda(in des integer, in val double,in matricula integer)
BEGIN
	INSERT INTO Deuda(descripcion,valor,id_Factura,numMatricula) 
	VALUES(des,val,NULL,matricula);
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE cancelarDeuda(in deuda integer, in factura integer)
BEGIN
	UPDATE Deuda set id_Factura=factura
	WHERE id_Deuda=deuda;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE crearFactura()
BEGIN
	INSERT INTO Factura(fecha,valor) VALUES("1959-3-12",0);
	
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerFacturas()
BEGIN
	SELECT id_Factura FROM Factura
	ORDER BY id_Factura DESC;
	
END //
DELIMITER ;


#logguin
DELIMITER //
CREATE PROCEDURE validarUsuario(in tipo integer,in user varchar(50),in contra varchar(50),out val integer )
BEGIN
	select count(*) into @contador from Administrativo
	where usuario=user and contrasenia=contra;
	if(select @contador=0) then
		set val:= 0;
	else
		set val:= 1;
	end if; 
	
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ligarEstudiantePersona(in cedPers char(10), in matricula integer,in tipo integer)
BEGIN

	Insert Into PersonaEstudiante(cedulaPersona,numMatricula,tipoPersona) 
	Values(cedPers,matricula,tipo);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerMatriculaEstudiante(in ced integer)
BEGIN
	select numMatricula from Estudiante
	where cedula=ced;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE obtenerPersonaFactura(in ced integer)
BEGIN
	select cedulaFactura into @persona from Estudiante
	where cedula=ced;

	select * from PersonaFactura 
	where cedula in (select @persona);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerEstudiantesPorCurso(in id_curso integer)
BEGIN
	select nombres, apellidos  from Estudiante e, Curso c, CursoEstudiante ce
	where c.id_Curso = id_curso and ce.id_curso = c.id_Curso and ce.numMatricula = e.numMatricula;

END //
DELIMITER ;



use BaseEscuela;

INSERT INTO Estudiante  VALUES(1,"0987564295", "Bruno Camilo", "Bonzano Euler",
"Masculino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2008-7-04',NULL);

INSERT INTO Estudiante  VALUES(2,"0914690458", "Karen Lola", "Yambay Castro",
"Femenino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2007-6-12',NULL);

INSERT INTO Estudiante  VALUES(3,"0967850399", "Ricardo Manuel", "De la A Angulo",
"Masculino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2007-4-24',NULL);


INSERT INTO Estudiante  VALUES(4,"0976885544", "Jose Rolando", "Caicedo Mora",
"Masculino", "Soltero","Guayas-Guayaquil", "BLANCO", '2007-6-06',NULL);


INSERT INTO Estudiante  VALUES(5,"0967850396", "Lucía Angélica", "De Jesus Andrade",
"Femenino", "Soltero","Guayas-Guayaquil", "NEGRO", '2007-12-05',NULL);


INSERT INTO Estudiante  VALUES(6,"0977870398", "Jesus Gabriel", "Aumala De Nazaret",
"Masculino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2007-12-25',NULL);

INSERT INTO Estudiante  VALUES(7,"1301910816", "Melissa Carla", "Romero Quinde",
"Femenino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2005-7-04',NULL);

INSERT INTO Estudiante  VALUES(8,"0914720057", "Melannie Lorenley", "Posligua Pasmiño",
"Femenino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2007-6-12',NULL);

INSERT INTO Estudiante  VALUES(9,"0951060185", "Jorge Enrique", "Vergara Palma",
"Masculino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2009-4-30',NULL);

INSERT INTO Estudiante  VALUES(10,"0987654390", "Coronel oswaldo", "Mora Benitez",
"Masculino", "Soltero","Guayas-Guayaquil", "BLANCO", '2002-8-06',NULL);

INSERT INTO Estudiante  VALUES(11,"1311810617", "kimberly Patricia", "De Jesus Valarezo",
"Femenino", "Soltero","Guayas-Guayaquil", "NEGRO", '2003-12-10',NULL);

INSERT INTO Estudiante  VALUES(12,"0915741185", "Cristina Estefania", "Casilla Navaz",
"Femenino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2004-12-25',NULL);

INSERT INTO Estudiante  VALUES(13,"0915742185", "Estefania Fernanda", "Parrales Montero",
"Femenino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2004-12-25',NULL);

INSERT INTO Estudiante  VALUES(14,"0706367890", "Maria Mercedes", "Caicedo Valencia",
"Femenino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2003-10-25',NULL);

INSERT INTO Estudiante  VALUES(15,"0706367850", "Luis Alfredo", "Paredes Martillo",
"Masculino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2004-05-12',NULL);

INSERT INTO Estudiante  VALUES(16,"0706367340", "Cristhian Jose", "Delgado Murillo",
"Masculino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2005-03-15',NULL);

INSERT INTO Estudiante  VALUES(17,"0706467890", "Carlos Javier", "Torres Nieto",
"Masculino", "Soltero","Guayas-Guayaquil", "MESTIZO", '2004-09-17',NULL);


#Profesores
INSERT INTO Profesor  VALUES("0956743399", "Fernando Angel", "Carvajal Guale",
"FernCar", "1234");

INSERT INTO Profesor  VALUES("0956763397", "Yanina Shegia", "Bajaña San Lucas",
"YaniSheg", "gyught");

INSERT INTO Profesor  VALUES("0936755399", "Jénnifer Lauren", "Avilez Moncada",
"JenAv", "clave");

INSERT INTO Profesor  VALUES("0965643377", "Silvia Selena", "Correa Ponce",
"SilvCorr3", "Escuela");

INSERT INTO Profesor  VALUES("0956743356", "Dennisse Jhon", "Maternal Smith",
"DennMat45", "23kill");

INSERT INTO Profesor  VALUES("0946443345", "Ufredo Arturo", "Molina Lainez",
"UfMol43", "BallNeumman");

INSERT INTO Profesor  VALUES("0946863345", "Mario Luigui", "Flores Pazos",
"mario12", "contrasecreta");

INSERT INTO Profesor  VALUES("0723458899", "Vladimir Israel", "Arosemena Martillo",
"vlad345", "vladimir");

INSERT INTO Profesor  VALUES("0746863325", "Gustavo Javier", "Quiñonez Caicedo",
"gusjaqui", "bsccampeon");

INSERT INTO Profesor  VALUES("0706356706", "Martha del Carmen", "Zambrano Meza",
"marthita93", "deberbaseslargo");




#Materias
INSERT INTO Materia  VALUES(11, "Matemáticas");
INSERT INTO Materia  VALUES(21, "Lenguaje");
INSERT INTO Materia  VALUES(33, "Ciencias Naturales");
INSERT INTO Materia  VALUES(41, "Ciencias Sociales");
INSERT INTO Materia  VALUES(54, "Musica");
INSERT INTO Materia  VALUES(61, "Educación Física");
INSERT INTO Materia  VALUES(77, "Recreo");

#Administrativo
INSERT INTO Administrativo VALUES("096743688", "Janeth Rosa", "Romero Saltos", 
"jrrs", "kiko");

INSERT INTO Administrativo VALUES("090043448", "Marcos Manuel", "Millán Santana", 
"mmms34", "telematico");

INSERT INTO Administrativo VALUES("092723684", "Benito Homero", "Juarez Barriga", 
"benHo", "hrut");

INSERT INTO Administrativo VALUES("094333688", "María Antonieta", "De las Nieves", 
"MADN", "chilindrina");

INSERT INTO Administrativo VALUES("096767688", "Pablo Jose", "Cortez Cortez", 
"PJCC", "Rockola");

INSERT INTO Administrativo VALUES("099740088", "Verónica Kerly", "Pumagualle Ortiz", 
"VKPuma", "ert");



#PERSONAS

INSERT INTO Persona VALUES ("0976443388", "Carlos Gonzalo", "Morocho Carbo", 
"Masculino", "1973-9-01","Casado","Abogado de la República", "El centro", "457855", "calle x" );

INSERT INTO Persona VALUES ("0976223382", "Teresa Jessica", "Torres De Hanoí", 
"Femenino", "1969-11-02","Casado","Periodista", "Ecuador TV", "438812", "calle y" );

INSERT INTO Persona VALUES ("0956441332", "Sergio Daniel", "Cedeño Gutierrez", 
"Masculino", "1978-2-04","Casado","Contador", "Empresa A", "467835", "calle z" );

INSERT INTO Persona VALUES ("0977441388", "Ludovico Ernesto", "Espinoza De Los Monteros", 
"Masculino", "1959-6-11","Divorsiado","Director Técnico ", "Equipo", "457123", "av x" );

INSERT INTO Persona VALUES ("0966443345", "Katerine Gioconda", "Córdova De Sucre", 
"Femenino", "1965-8-20","Casado","Contadora", "El Sur", "457812", "av al sur" );

INSERT INTO Persona VALUES ("0966443399", "Behrouz Foruzan", "Carbo Guzman", 
"Masculino", "1965-12-23","Casado","Escritor", "El Norte", "677812", "av al Norte" );

INSERT INTO Persona VALUES ("0966443733", "Narcisa Vanessa", "Chiluisa Bayona", 
"Femenino", "1991-8-20","Casado","Vendedeora", "La calle", "457834", "la calle" );

INSERT INTO Persona VALUES ("0966493322", "Jose Antonio", "Delgado Neumann", 
"Masculino", "1965-8-20","Casado","Musico", "Mi casa", "757232", "calle xy3" );

INSERT INTO Persona VALUES ("0566423345", "Michael Mario", "Jackson Quiñones", 
"Masculino", "1934-2-21","Casado","Piloto", "Aeropuerto", "127849", "av al aeropuerto" );

INSERT INTO Persona VALUES ("0866443313", "Wagner Christian", "Cevallos Arévalo", 
"Masculino", "1966-7-07","Casado","Eléctricista", "Empresa Eléctrica", "677587", "calle u" );

INSERT INTO Persona VALUES ("0166223375", "Alejandra Ana", "Córdova De Sucre", 
"Femenino", "1975-8-13","Casado","Cantante", "Estudio", "128944", "av al sur" );

INSERT INTO Persona VALUES ("0960043340", "Víctor Hugo", "Jimenez Palacios", 
"Masculino", "1968-8-20","Casado","Científico", "Laboratorio", "231155", "av perimetral" );

INSERT INTO Persona  VALUES("0956743459", "Fernando Angel", "Carvajal Guale",
"Maculino", "1968-11-05", "Casado", "Ingeniero", "Empresa z", "235572", "calle 34");

INSERT INTO Persona  VALUES("0645557811", "Yanina Shegia", "Bajaña San Lucas",
"Femenino", "1967-11-05", "Casado", "Cantante", "Calle", "235511", "av vy");

INSERT INTO Persona  VALUES("0936565312", "Jénnifer Lauren", "Avilez Moncada",
"Femenino", "1977-11-04", "Casado", "Pintor", "Estudio de arte", "235589", "av k");

INSERT INTO Persona  VALUES("0665643387", "Silvia Selena", "Correa Ponce",
"Femenino", "1968-10-11", "Casado", "Doctora", "Hospital", "785514", "av h");

INSERT INTO Persona  VALUES("0956743356", "Dennisse Jhon", "Maternal Smith",
"Masculino", "1956-11-12", "Casado", "Profesor", "Celex", "235002", "calle x12");

INSERT INTO Persona  VALUES("0946443345", "Ufredo Arturo", "Molina Lainez",
"Masculino", "1989-9-09", "Casado", "Ingeniero", "Empresa yz", "565599", "av j");

INSERT INTO Persona  VALUES("0946863345", "Mario Luigui", "Flores Pazos",
"Masculino", "1988-8-06", "Casado", "Marinero", "Mar", "235672", "via al mar");

INSERT INTO Persona  VALUES("0723458899", "Vladimir Israel", "Arosemena Martillo",
"Masculino", "1959-3-12", "Casado", "Ingeniero", "Empresa u", "896789", "via u");









call crearMaterias();

call crearCurso(1,"2011-2012",1);

call crearCurso(1,"2012-2014",2);

call crearCurso(1,"2011-2012",3);

call crearCurso(2,"2011-2012",1);

call crearCurso(3,"2011-2012",4);

call crearCurso(4,"2012-2014",2);

call crearCurso(4,"2011-2012",5);

call crearCurso(7,"2011-2012",7);
#INSERT INTO Curso VALUES(7,6,"2014-2015","A","0956763397");
#INSERT INTO Curso VALUES(8,7,"2014-2015","A","0965643377"); 

INSERT INTO MateriaEstudianteQuimestre  values(45,3, 10);
#Select* from MateriaEstudianteQuimestre;
#Select * from Quimestre;
#Select * from Parcial;
#Select * from Actividad;
#INSERT INTO Quimestre(numQuimestre, notaQuimestre, id_MatEstQui) values (1,0.00,45 );
#delete from Parcial;

call agregarEstudianteEnCurso(1,1);

select * from CursoEstudiante;

select * from Materia;
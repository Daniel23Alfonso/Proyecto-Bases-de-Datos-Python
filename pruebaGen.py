# -*- coding: utf-8 -*-
from GeneradorReporte import *

gener = GeneradorReporte()
lista = ["Oswaldo", "Eloy", "Ortega"]
curso = "Primer"
par = "A"
gener.GenerarListaAsistencia(lista, curso, par)

materiasCalificaciones = [["Lenguaje","8.7","OCHO COMA SIETE"],
                          ["Matematicas","9,7","NUEVE COMA SIETE"],
                          ["entorno natural y social","8.7","OCHO COMA SIETE"],
                          ["PROMEDIO GENERAL","8.9","OCHO COMA NUEVE"],
                          ["COMPORTAMIENTO","8","OCHO"]]

gener.GenerarPromocion("OSWALDO ALEJANDRO BAYONA ANDRADE", "TERCER GRADO DE EDUCACION GENERAL BASICA", "2013-2014", materiasCalificaciones,
	u"CUARTO CURSO DE EDUCACION BÁSICA")

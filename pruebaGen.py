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



listaCantDetallesPUnitTotal = [["2","Pencion","$70","$140" ],
								["1","Deuda","$10","$10" ]


								]
gener.GenerarFactura("2456789","Oswaldo Bayona", "33 y San Martin", listaCantDetallesPUnitTotal,"150")


listaCalificaciones = [["10", "10"], ["2", "3"], ["4", "7"], ["9", "10"], ["10", "10"],
                       ["2", "10"], ["10", "9,88"], ["7", "9"], ["8", "9"], ["10", "9"] ]


gener.generarLibreta("Oswaldo",listaCalificaciones, "6to","2014-2015", "YADIRA MEDINA", "Lic. Yule Palma de Vergara")
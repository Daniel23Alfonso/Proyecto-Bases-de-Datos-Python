# -*- coding: utf-8 -*-

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle ,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
import time



class GeneradorReporte:

  def GenerarLista (self,estudiantes,Curso, paralelo):

    namefile = "Lista_%s%s.pdf"%(Curso,paralelo)
    doc = SimpleDocTemplate(namefile, pagesize=letter)
    elements = []
    styleSheet = getSampleStyleSheet()

    titulo = Paragraph('''<b>Escuela Particular Dr. Jaime Aspiazu Seminario </b>''',styleSheet["BodyText"])
    stringCurso = u"<b>Curso: %s año básico, Paralelo: %s</b>"%(Curso,paralelo)
    subtitulo = Paragraph(stringCurso,styleSheet["BodyText"])
    fecha = time.strftime("%d/%m/%y")
    stringfecha = "Fecha: %s"%fecha

    datosHeader = [[titulo],[subtitulo],[stringfecha],[]]
    tablaHeader = Table(datosHeader)
    tablaHeader.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ]))

    #este es la etiqueta de la columna de enumeracion
    N = Paragraph('''<b>N</b><super><font color=black>o</font></super>''', styleSheet["BodyText"])

    datosEstudiante = [[N,u"Nómina Estudiantes", "Firma del Representante"]]
    cont =1
    for e in estudiantes:
      aux = []
      aux.append(str(cont))
      aux.append(e)
      aux.append(" ")
      datosEstudiante.append(aux)
      cont= cont + 1


    tablaEstudiante = Table(datosEstudiante)
    nFila = len(datosEstudiante)
    tablaEstudiante.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND',(0,0),(0,nFila),colors.beige),
                       ('BACKGROUND',(0,0),(3,0),colors.beige)
                       ]))
    tablaEstudiante._argW[0]=0.5*inch
    tablaEstudiante._argW[1]=3*inch
    tablaEstudiante._argW[2]=2.5*inch


    elements.append(tablaHeader)
    elements.append(tablaEstudiante)
    doc.build(elements)




  def GenerarListaAsistencia (self,estudiantes,Curso, paralelo):

    namefile = "ListaAsistencia_%s%s.pdf"%(Curso,paralelo)
    doc = SimpleDocTemplate(namefile, pagesize=letter)
    elements = []
    styleSheet = getSampleStyleSheet()

    titulo = Paragraph('''<b>Escuela Particular Dr. Jaime Aspiazu Seminario </b>''',styleSheet["BodyText"])
    stringCurso = u"<b>Curso: %s año básico, Paralelo: %s</b>"%(Curso,paralelo)
    subtitulo = Paragraph(stringCurso,styleSheet["BodyText"])
    fecha = time.strftime("%d/%m/%y")
    stringfecha = "Fecha: %s"%fecha

    datosHeader = [[titulo],[subtitulo],[stringfecha],[]]
    tablaHeader = Table(datosHeader)
    tablaHeader.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ]))

    #este es la etiqueta de la columna de enumeracion
    N = Paragraph('''<b>N</b><super><font color=black>o</font></super>''', styleSheet["BodyText"])

    datosEstudiante = [[N,u"Nómina Estudiantes", "1","2","3","4","5"]]
    cont =1
    for e in estudiantes:
      aux = []
      aux.append(str(cont))
      aux.append(e)
      aux.append(" ")
      aux.append(" ")
      aux.append(" ")
      aux.append(" ")
      aux.append(" ")
      datosEstudiante.append(aux)
      cont= cont + 1


    tablaEstudiante = Table(datosEstudiante)
    nFila = len(datosEstudiante)
    tablaEstudiante.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND',(0,0),(0,nFila),colors.beige),
                       ('BACKGROUND',(0,0),(6,0),colors.beige)
                       ]))
    tablaEstudiante._argW[0]=0.5*inch
    tablaEstudiante._argW[1]=3*inch
    tablaEstudiante._argW[2]=0.5*inch
    tablaEstudiante._argW[3]=0.5*inch
    tablaEstudiante._argW[4]=0.5*inch
    tablaEstudiante._argW[5]=0.5*inch
    tablaEstudiante._argW[6]=0.5*inch

    elements.append(tablaHeader)
    elements.append(tablaEstudiante)
    doc.build(elements)



  def GenerarPromocion (self,nombreEstudiante,Curso, anioLectivo, MateriasCalificaciones, cursoPromovido):

    namefile = "Promocion_%s_%s.pdf"%(nombreEstudiante,Curso)
    doc = SimpleDocTemplate(namefile, pagesize=letter)
    elements = []
    styleSheet = getSampleStyleSheet()

    titulo = Paragraph('''<DIV align = "right"><b>ESCUELA PARTICULAR MIXTA N <super><font color=black>o</font></super> 851</b></DIV>''',
      styleSheet["BodyText"])

    nombreEscuela = Paragraph('''<b>&quot;DR. JAIME ASPIAZU SEMINARIO&quot;</b>''',styleSheet["BodyText"])
    
    direccion = u"Dirección: calle M entre 25 y 26   Teléfono: 04-3092761"
    stringanioLectivo = u"AÑO LECTIVO %s"%anioLectivo

    


    textol1 = u"De conformidad con lo prescrito en el Art. 197 del Reglamento General de la Ley Orgánica de "
    textol2 = u"Educación Intercultural y demás normativas vigentes, certifica que el/la estudiante " 
    textol3 = u"<b>%s</b> del <b>%s</b>, obtuvo "%(nombreEstudiante,Curso)
    textol4 = u"las siguientes calificaciones, durante el presente año lectivo:"

    StringParrafo = textol1 + textol2 + textol3 + textol4 
    parrafo = Paragraph(StringParrafo, styleSheet["BodyText"])


    datosHeader = [[titulo],[nombreEscuela],[direccion],[stringanioLectivo],[],[],[parrafo],[]]
    tablaHeader = Table(datosHeader)
    tablaHeader.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ]))

    datosTabla = [["ASIGNATURAS\n", "CALIFICACIONES"], ['','NUM', 'LETRAS' ]]
    for mc in MateriasCalificaciones:
      datosTabla.append(mc)

    tablaCalif = Table(datosTabla)
    tablaCalif.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.gray),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black)
                       ]))

    final1 = u"Por lo tanto es promovido/a al <b>%s</b> Para"%cursoPromovido
    final2 = u"certificar suscribe en unidad de acto el Director con la secretaria General del Plantel"

    stringfinal = final1 + final2
    parrafoFinal = Paragraph(stringfinal,styleSheet["BodyText"] )
    datostablaFinal = [[], [parrafoFinal], []]
    tablaFinal = Table(datostablaFinal)

    elements.append(tablaHeader)
    elements.append(tablaCalif)
    elements.append(tablaFinal)
    doc.build(elements)

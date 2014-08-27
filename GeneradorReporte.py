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



  def GenerarFactura (self,telefono,cliente, direccion, listCantDetallePrecio,valorTotal):

    fecha = time.strftime("%d/%m/%y")  

    namefile = "Factura_%s.pdf"%cliente
    doc = SimpleDocTemplate(namefile, pagesize=letter)
    elements = []
    styleSheet = getSampleStyleSheet()

    titulo = Paragraph('''<b>ESCUELA PARTICULAR MIXTA #851</b>''',styleSheet["BodyText"])

    nombreEscuela = Paragraph('''<b>&quot;DR. JAIME ASPIAZU SEMINARIO&quot;</b>''',styleSheet["BodyText"])
    
    dirEscuela = u"Dirección: M S/N entre 26ava. y 25ava.\nTeléfono: 04-3092761"
    telfEscuela = "Telf.: 3092761 Guayaquil - Ecuador"
    ruc = "R.U.C.: 0914720057001"
    FechaAut = "21/Julio/2014"

    FACTURA = Paragraph('''<b>FACTURA</b>''',styleSheet["BodyText"])


    datosHeader = [[titulo],[nombreEscuela],[dirEscuela],[telfEscuela],[ruc],[FACTURA]]
    tablaHeader = Table(datosHeader)
    tablaHeader.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ]))


    Stringfilafechatelf = "FECHA: <u>%s    </u> TELF: <u>%s    </u>"%(fecha,telefono)
    pfecha = Paragraph(Stringfilafechatelf,styleSheet["BodyText"])
    StringCliente = "CLIENTE: <u>%s      </u>"%cliente
    pcliente = Paragraph(StringCliente, styleSheet["BodyText"])
    StrignDireccion = "DIRECCION: <u>%s     </u>"%direccion
    pdireccion = Paragraph(StrignDireccion,styleSheet["BodyText"])

    datosCliente = [[pfecha],[pcliente],[pdireccion],[]]
    tablaCliente = Table(datosCliente)
    tablaHeader.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ]))

    headerFactura  = [["CANT.","DETALLE","P.UNIT", "V.TOTAL"]]
    datosfatura = headerFactura + listCantDetallePrecio
    datosfatura.append(["","", "VALOR TOTAL $", valorTotal])

    tablaDatosFactura = Table(datosfatura)

    tablaDatosFactura.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('BACKGROUND',(0,0),(3,0),colors.gray)
                       ]))

    firmas = [["",""] ,["__________________","______________" ],["Entregado Por", "Recibido Por"]]
    tablafirmas = Table(firmas)
    tablafirmas.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ]))



    elements.append(tablaHeader);
    elements.append(tablaCliente);
    elements.append(tablaDatosFactura)
    elements.append(tablafirmas)
    doc.build(elements)


  def generarLibreta(self, nombreEstudiante, calificaciones, grado, anioLectivo, representante,
    profesor):

    namefile = "Libreta_%s_%s.pdf"%(nombreEstudiante, grado)
    elementos = []
    styleSheet = getSampleStyleSheet()
    doc = SimpleDocTemplate(namefile, pagesize=letter)
    styles = getSampleStyleSheet()
    titulo = Paragraph("""<font size="9">ESCUELA PARTICULAR MIXTA # 851 &quot;Dr. JAIME ASPIAZU SEMINARIO&quot;</font>""", styleSheet["BodyText"])
    stringEstudiante = u"ESTUDIANTE:                    %s"%nombreEstudiante

    strigngradoAnio = u"GRADO:                         %s GRADO                            AÑO LECTIVO %s"%(grado, anioLectivo)

    datosHeader = [[titulo],[stringEstudiante],[strigngradoAnio],[]]
    tablaH = Table(datosHeader)
    tablaH.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black)]))

    tablaH._argW[0]=7*inch

    elementos.append(tablaH)

    m1 = ["Lengua y literatura"]
    m2 = [u"Matemática" ]
    m3 = ["Ciencias Naturales"]
    m4 = ["Estudio Sociales" ]
    m5 = [u"Cultura Estética"]
    m6 =        [u"Cultura Física" ]
    m7 = [u"Inglés"]
    m8 =  ["Optativa"]
    m9 =  ["Suma total"]
    m10 = ["PROMEDIO"]

    materias = []
    i =0
    for f in [m1, m2, m3,m4,m5,m6,m7,m8,m9,m10]:
      materias.append(f + calificaciones[i])
      i = i+1


    headerGrill = [["ASIGNATURA         ","1   ","2   ","3   ","EXA ","Prom", "1   ","2   ","3   ","EXA ",
                  "Prom", "PRO ", "SUP ", "PF  " ]] 




    for f in materias:
      headerGrill.append(f)


    tablaLibreta = Table(headerGrill)
    tablaLibreta.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('FONTSIZE', (1, 1), (-1, -1), 8), 
                       ]))



    elementos.append(tablaLibreta)

    listaFinal = [["REPRESENTANTE ", representante],[u"PROFESOR GUÍA", profesor]]
    tablafinal = Table(listaFinal)
    tablafinal.setStyle(TableStyle([ ('ALIGN',(0,0),(-1,-1),'LEFT'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

    tablafinal._argW[0]=3.49*inch
    tablafinal._argW[1]=3.49*inch

    elementos.append(tablafinal)

    doc.build(elementos)








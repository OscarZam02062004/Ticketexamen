#Librerias
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import random
import qrcode
from PIL import Image
from PIL import Image,ImageOps
#variables
ahora=datetime.now()
fecha=ahora.strftime("%Y-%m-%d %H:%M:%S")
Comprar=True
decremento = 20
inicialX = 100
inicialY = 620
precioX= 300
precioY= 620
canX= 10
canY= 620
totalX=390
totalY=620
incremento = 60
w, h = A4
#Inicio de pdf
ruta="C:/Users/zamor/OneDrive/Escritorio/ReportePythonTicket/"
c = canvas.Canvas(ruta+"ticketprueba.pdf", pagesize=A4)
#Parte de inicial del ticket
c.setFillColorRGB(0,0,128)
c.setFont('Helvetica-Bold',30)
c.drawString(10,800, "Bienvenido a Sams Club")
c.setFont('Helvetica',10)
c.setFillColorRGB(0,0,0)
c.drawString(10,780,f"Fecha del recibo: {fecha} ")
nombre=(input("Ingresa tu nombre de usuario: "))
c.drawString(10,770,f"Nombre del usuario: {nombre}")
c.drawString(10,760,"Expedido en: PACHUCA HIDALGO")
c.drawString(10,750,"Dirección:Col. Felipe Angeles Ampliación C.P 42090")
c.drawString(10,740,"Sucursal:Providencia")
c.drawString(10,730,"-----------------------------------------------------------------")
c.setFont('Helvetica-Bold',25)
#Informacion del ticket
c.setFillColorRGB(0,0,128)
c.drawString(230,690,"Productos")
x = 0 
y = h - 160 
c.line(x, y, x + 800, y)
c.setFillColorRGB(0,128,0)
c.setFont("Helvetica-Bold",13)
c.drawString(50,660,"Cantidad")
c.drawString(150,660,"Nombre del producto")
c.drawString(330,660,"Precio unitario")
c. drawString(520,660,"Total")
x = 0 
y = h - 200 
c.line(x, y, x + 800, y)
#Ingresando productos
lista = []
productos = []
precios=[]
cantidad=[]
while Comprar:
    productos.append(input("¿Que vas a comprar? "))
    cantidad.append(int(input("Cuanto vas a llevar: ")))
    precios.append(float(input("Cuanto cuesta? ")))

    Recomprar= input("¿Desea realizar otra compra? (Si/No): ")
    if Recomprar!= "Si":
        Comprar = False

totalfinal = 0
for i in range(len(productos)):
    total = cantidad[i] * precios[i]
    totalfinal = totalfinal + total

Cambio=0
Iva=totalfinal*.16
TotalconIva=Iva+totalfinal
print(f"El total es : {TotalconIva}")
Cobro=(float(input("Ingresa la cantidad con la que vas a pagar: ")))
Cambio=Cobro-TotalconIva
#--------Cambio de color dependiendo el precio----------
if(TotalconIva>1000):
    c.setFillColorRGB(0,0,128)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(430,240,("Iva del 16%: "+str(Iva)))
    c.drawString(430,280,("Pago en Efectivo:$ "+str(Cobro)))
    c.drawString(430,260,("Cambio:$ "+str(Cambio)))
    c.drawString(430,300,("Total:$ " + str(TotalconIva)))
    for i in range(len(productos)):

        c.drawString(canX + incremento, canY,str(cantidad[i]))
        canY = canY-decremento

        c.drawString(inicialX + incremento, inicialY,str(productos[i]))
        inicialY = inicialY-decremento

        c.drawString(precioX + incremento, precioY,(str(f"${precios[i]}")))
        precioY = precioY-decremento
        
        c.drawString(totalX + 120, totalY,(str(f"$ {total}")))
        totalY = totalY-decremento

else:
    c.setFillColorRGB(0,0,0)
    c.drawString(430,240,"Iva del 16%: "+str(Iva))
    c.drawString(430,280,"Pago en Efectivo:$ "+str(Cobro))
    c.drawString(430,260,"Cambio:$ "+str(Cambio))
    c.setFont('Helvetica-Bold', 13)
    c.drawString(430,300,"Total:$ " + str(TotalconIva))
    for i in range(len(productos)):

        c.drawString(canX + incremento, canY,str(cantidad[i]))
        canY = canY-decremento

        c.drawString(inicialX + incremento, inicialY,str(productos[i]))
        inicialY = inicialY-decremento

        c.drawString(precioX + incremento, precioY,str(f"${precios[i]}"))
        precioY = precioY-decremento
        
        c.drawString(totalX + 120, totalY,str(f"$ {total}"))
        totalY = totalY-decremento
#------------QR-----------------------------------
informacion=f"Compraste {productos} con un precio de {precios} ,el NO. de cantidades son {cantidad} con un precio total de:{TotalconIva}"
nombreimagen= ruta+"miQR.png"
if(Cobro==TotalconIva):

    
    def create_golden_qr(data, filename):
    # Crear el código QR con relleno dorado
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="gold", back_color="black")

        # Obtener el tamaño del código QR generado
        width, height = qr_image.size

        # Crear una nueva imagen con fondo negro del mismo tamaño que el código QR
        final_image = Image.new("RGB", (width, height), color="black")

        # Pegar el código QR con relleno dorado en la imagen con fondo negro
        final_image.paste(qr_image)

        # Guardar la imagen final con fondo negro y relleno dorado
        final_image.save(filename)

    if __name__ == "__main__":
        # Datos que quieres codificar en el QR
        qr_data =f"Compraste {productos} con un precio de {precios} ,el NO. de cantidades son {cantidad} con un precio total de:{TotalconIva}"
        
        # Nombre del archivo de salida
        output_filename ="miQR.png"
        
        # Crear el código QR con fondo negro y relleno dorado
        create_golden_qr(qr_data, output_filename)

    
    c.drawImage(output_filename,440,60,150,150)

else:
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=5)
    qr.add_data(informacion)
    qr.make(fit=True)
    img=qr.make_image(fill='#000000',back_color=f'#FFFFFF')
    f=open(nombreimagen,"wb")
    f=open(ruta+"miQR.png","wb")
    img.save(f)
    c.drawImage(nombreimagen,440,60,150,150)
    f.close()

#-----------------Promociones-----------------------------------
codigo= random.uniform(3,11)
c.setFont('Helvetica', 10)
c.drawString(10,220,f"Codigo de rastreo: {codigo}")
x = 0 
y = h - 630
c.line(x, y, x + 800, y)
logoSams = ruta + "sams.png"
c.drawImage(logoSams,450,730,100,100, mask="auto")
fondoazul=ruta+"azul.png"
c.drawImage(fondoazul,0,-150,200,200, mask="auto")
c.drawImage(fondoazul,200,-150,200,200, mask="auto")
c.drawImage(fondoazul,300,-150,200,200, mask="auto")
c.drawImage(fondoazul,400,-150,200,200, mask="auto")
c.drawImage(fondoazul,500,-150,200,200, mask="auto")
c.drawImage(fondoazul,800,-550,200,200, mask="auto")
c.setFont('Helvetica-Bold',14)
c.drawString(170,150,"**COMPRA Y GANA**")
c.drawString(150,180,"¡GRACIAS POR SU COMPRA!")
c.setFont('Helvetica-Bold',10)
c.drawString(10,130,"Tambien puedes obtener tu factura en www.sams.com")
c.drawString(10,110,"Telefono sin costo: 771 245 22 55")
c.drawString(10,90,">>Para garantizar la calidad de nuestros productos no aceptamos devoluciones>>")
c.save()
       


#Librerias
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import random
import qrcode
#variables
ahora=datetime.now()
fecha=ahora.strftime("%Y-%m-%d %H:%M:%S")
w, h = A4
#Inicio de pdf
ruta="C:/Users/zamor/OneDrive/Escritorio/ReportePythonTicket/"

c = canvas.Canvas(ruta+"ticketprueba.pdf", pagesize=A4)
c.setFont('Helvetica',30)
c.drawString(100,780, "Sams Club")
c.setFont('Helvetica',10)
c.drawString(100,760,fecha)
c.setFont('Helvetica-Bold',20)
c.drawString(250,690,"Productos")
x = 0 #Mueve hacia la derecha la linea
y = h - 160 #Sube o baja la linea 
c.line(x, y, x + 800, y)
c.setFont("Helvetica-Bold",13)
c.drawString(10,660,"Cantidad")
c.drawString(120,660,"Nombre del producto")
c.drawString(350,660,"Precio unitario")
c.drawString(500,660,"Total")
x = 0 
y = h - 200 
c.line(x, y, x + 800, y)
nombre=(input("Ingresa tu nombre de usuario: "))
c.setFont('Helvetica',10)
c.drawString(100,740,f"Nombre del usuario: {nombre}")
objetos=[

{"nombre":"Iphone","precio":12000.00},
{"nombre":"Computadora","precio":150000.00},
{"nombre":"TV","precio":40000.00},
{"nombre": "Consola de videojuegos","precio":7500.00},
{"nombre":"Audifonos","precio":1500.75},

]
Comprar=True
contador=[]
while Comprar:
    for i, producto in enumerate(objetos, 1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']}")

    Escogio=input("¿Que desea Comprar? ")
    Cantidad=int(input(f"¿Cuantas {Escogio} llevas? "))
#.append funcionara para agregar todos los elementos que el usuario escogio en nuestra variable contador
    contador.append({
        'producto': Escogio,
        'cantidad': Cantidad
    })
    Recomprar= input("¿Desea realizar otra compra? (Si/No): ")
    if Recomprar!= "Si":
        Comprar = False

if contador:
    # Imprimir los datos de la compra
    for item in contador:
        producto = item['producto']
        Cantidad = item['cantidad']
        precio = next((p['precio'] for p in objetos if p['nombre'] == producto), 0)
        subtotal = Cantidad * precio
        
    # Calcular el total a pagar
    total_compra = sum(item['cantidad'] * next((p['precio'] for p in objetos if p['nombre'] == item['producto']), 0) for item in contador)

informacion=f"Compraste {producto} con un precio de {precio} ,el NO. de cantidades son {Cantidad} con un precio total de: {subtotal}"
img=qrcode.make(informacion)
nombreimagen= ruta+"miQR.png"
f=open(nombreimagen,"wb")
f=open(ruta+"miQR.png","wb")
img.save(f)
f.close() 

c.drawString(15,620,f"{Cantidad}")
c.drawString(150,620,f"{Escogio}")
c.drawString(350,620,f"${precio}")
c.drawString(500,620,f"${total_compra}")
x = 0 
y = h - 300 
c.line(x, y, x + 800, y)
codigo= random.uniform(3,11)
c.drawString(15,500,f"Codigo de rastreo: {codigo}")
c.drawImage(nombreimagen,200,220,200,200)
logoSams = ruta + "sams.png"
c.drawImage(logoSams,450,730,100,100, mask="auto")
c.save()

import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Paleta izquierda
paleta_izq = turtle.Turtle()
paleta_izq.speed(0)
paleta_izq.shape("square")
paleta_izq.color("white")
paleta_izq.shapesize(stretch_wid=5, stretch_len=1)
paleta_izq.penup()
paleta_izq.goto(-350, 0)

# Paleta derecha
paleta_der = turtle.Turtle()
paleta_der.speed(0)
paleta_der.shape("square")
paleta_der.color("white")
paleta_der.shapesize(stretch_wid=5, stretch_len=1)
paleta_der.penup()
paleta_der.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.2
pelota.dy = 0.2

# Marcador
marcador_izq = 0
marcador_der = 0

puntaje = turtle.Turtle()
puntaje.speed(0)
puntaje.color("white")
puntaje.penup()
puntaje.hideturtle()
puntaje.goto(0, 260)
puntaje.write(f"{marcador_izq}  :  {marcador_der}",
              align="center", font=("Arial", 24, "normal"))

# Movimiento de paletas
def paleta_izq_arriba():
    if paleta_izq.ycor() < 250:
        paleta_izq.sety(paleta_izq.ycor() + 20)

def paleta_izq_abajo():
    if paleta_izq.ycor() > -250:
        paleta_izq.sety(paleta_izq.ycor() - 20)

def paleta_der_arriba():
    if paleta_der.ycor() < 250:
        paleta_der.sety(paleta_der.ycor() + 20)

def paleta_der_abajo():
    if paleta_der.ycor() > -250:
        paleta_der.sety(paleta_der.ycor() - 20)

# Controles
ventana.listen()
ventana.onkeypress(paleta_izq_arriba, "w")
ventana.onkeypress(paleta_izq_abajo, "s")
ventana.onkeypress(paleta_der_arriba, "Up")
ventana.onkeypress(paleta_der_abajo, "Down")

# Loop principal
while True:
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebote en paredes arriba y abajo
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *= -1

    # Pelota sale por la derecha
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador_izq += 1
        puntaje.clear()
        puntaje.write(f"{marcador_izq}  :  {marcador_der}",
                      align="center", font=("Arial", 24, "normal"))

    # Pelota sale por la izquierda
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador_der += 1
        puntaje.clear()
        puntaje.write(f"{marcador_izq}  :  {marcador_der}",
                      align="center", font=("Arial", 24, "normal"))

    # Colisión con paleta derecha
    if (pelota.xcor() > 340 and pelota.xcor() < 360 and
            abs(pelota.ycor() - paleta_der.ycor()) < 50):
        pelota.dx *= -1

    # Colisión con paleta izquierda
    if (pelota.xcor() < -340 and pelota.xcor() > -360 and
            abs(pelota.ycor() - paleta_izq.ycor()) < 50):
        pelota.dx *= -1
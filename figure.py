import turtle
g = turtle.Turtle()
g.shape("turtle")
g.speed(0)
counter = 0



def draw_pentagon(g):
    g.forward(80)
    g.left(72)


while counter <= 120:
    g.forward(80)
    g.left(72)
    g.forward(80)
    g.left(72)
    g.forward(80)
    g.left(72)
    g.forward(80)
    g.left(72)
    g.forward(80)
    g.left(105)
    counter += 1



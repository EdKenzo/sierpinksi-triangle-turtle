import turtle

def drawTriangle(points,color,ed):
    ed.fillcolor(color)
    ed.up()
    ed.goto(points[0][0],points[0][1])
    ed.down()
    ed.begin_fill()
    ed.goto(points[1][0],points[1][1])
    ed.goto(points[2][0],points[2][1])
    ed.goto(points[0][0],points[0][1])
    ed.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,ed):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],ed)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, ed)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, ed)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, ed)

def main():
   ed = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,ed)
   myWin.exitonclick()

main()

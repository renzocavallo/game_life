from tkinter import Canvas

class Description(Canvas):

    def __init__(self, 
                master, 
                width=600, 
                height=300, 
                bg="gray", 
                bd=0, 
                highlightthickness=0):
        super().__init__(master, 
                        width=width, 
                        height=height, 
                        bg=bg, 
                        bd=bd, 
                        highlightthickness=highlightthickness)
        
        text = "El Juego de la vida es un autómata celular diseñado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, en el que su evolución es determinada por un estado inicial, sin requerir intervención adicional. \nNormalmente, después de un determinado número de ciclos, se puede llegar a alguno de los siguientes estados finales: \nExtinción: Al cabo de un número finito de generaciones desaparecen todos los miembros de la población o células vivas. \nEstabilizacion: Al cabo de un número finito de generaciones la población queda estabilizada, ya sea de forma rígida o bien de forma oscilante entre dos o más formas \nCrecimiento constante: La población crece turno tras turno y se mantiene así un número infinito de generaciones. En un principio esta evolución solo se contemplo de forma teórica, aunque más tarde se encontrarán patrones que crecían de forma indefinida, durante un número infinito de turnos."
        
        self.create_text(width/2, height/2, font=("Arial", 13), text=text, width=500)


        


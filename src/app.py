from tkinter import Tk, Button
from src.components.bton_win import BtonWin
from src.frames.screen_game import ScreenWindow
from src.components.description import Description
from game.game_life import start_game, pause_game

class App(Tk):

    def __init__(self):
        super().__init__()  
        
        def minimize(app):
    
            app.iconify()

        def close(app):

            app.quit()

        self.title("Primera App")
        self.resizable(False, False)
        self.geometry("700x700")
        self.attributes("-fullscreen", 1)
        self.configure(bg="gray")

        bton_quit = BtonWin(self, close, "X","#2B3932", "#B80000", "arrow", "#B80000")
        bton_quit.place(x=1295, y=0)

        bton_minimize = BtonWin(self, minimize, "-", "#2B3932" , "#BDBBBB", "hand2", "#BDBBBB")
        bton_minimize.place(x=1230, y=0)

        screen = ScreenWindow(self, 650, 650,"black")
        screen.place(x=30, y=75)

        description = Description(self)
        description.place(x= 700, y= 150)

        bton_start = Button(self, 
                            width=8, 
                            height=4, 
                            text= "Start", 
                            fg="white", 
                            bd=0, 
                            highlightthickness=0, 
                            activeforeground="white",
                            activebackground="#2B3932", 
                            bg="#2B3932", 
                            font="Arial", 
                            cursor="hand2", 
                            command= lambda : start_game(screen, bton_start)
                    )
        bton_start.place(x= 880, y=550)

        bton_pause = Button(self, 
                            width=8, 
                            height=4, 
                            cursor="hand2", 
                            fg="white", 
                            bg="#2B3932", 
                            activeforeground="white", 
                            activebackground="#2B3932", 
                            bd=0, 
                            highlightthickness=0, 
                            text='Pause', 
                            font="Arial", 
                            command= lambda : pause_game(bton_pause)
                    )
        bton_pause.place(x= 1050, y=550)

        self.mainloop()


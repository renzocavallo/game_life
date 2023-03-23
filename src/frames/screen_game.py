from tkinter import Frame

class ScreenWindow(Frame):

    def __init__(self, master, width, height, bg, relief="flat"):
        super().__init__(master,
                         width=width,
                         height=height,
                         bg=bg,
                         relief=relief,
                         highlightthickness=10,
                         highlightbackground="#2B3932"
                        )
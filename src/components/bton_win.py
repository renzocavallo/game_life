from tkinter import Button

class BtonWin(Button):

    def __init__(self,
                master, 
                function,
                text, 
                bg, 
                activebackground, 
                cursor,
                hover_color,
                bd=0,
                highlightthickness=0, 
                width=7, 
                height=3 ,
                font="Arial", 
                fg="white", 
                activeforeground="white"
                ):
        super().__init__(master,
                        text=text,
                        bg=bg, 
                        bd=bd, 
                        activebackground=activebackground,
                        cursor=cursor,
                        highlightthickness=highlightthickness,
                        width=width,
                        height=height,
                        font=font,
                        fg=fg,
                        activeforeground=activeforeground
                    )
        
        def hover(e):

            self.configure(bg=hover_color)

        def out_hover(e):

            self.configure(bg="#2B3932")

        def click(e):

            function(self.master)
            
        self.bind("<Enter>", hover)
        self.bind("<Leave>", out_hover)
        self.bind("<ButtonRelease-1>", click)

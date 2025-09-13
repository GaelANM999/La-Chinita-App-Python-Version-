import tkinter as tk
from tkinter import PhotoImage

class adminView:
    
    def pantallaAdmin(self):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title("La Chinita App Administrador")
        
        icon = PhotoImage(file='img/La Chinita.png')
       
        self.root.iconphoto(False, icon)
        self.root.resizable(False, False)
        self.root.configure(bg="#D3D4D4")
        
        self.root.mainloop()
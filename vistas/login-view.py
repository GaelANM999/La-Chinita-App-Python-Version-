import tkinter as tk
from tkinter import PhotoImage

class loginView:
     # Método para centrar la pantalla
    @staticmethod
    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')
        
    def loginVista(self):
        #variables de la ventana
        self.root = tk.Tk()
        self.root.title("Inicio de sesión")
        windowWidth = 500
        windowHeight = 375
        icon = PhotoImage(file='img/La Chinita.png')
        imagen = PhotoImage(file='img/La Chinita.png')
       
        self.root.iconphoto(False, icon)
        self.root.resizable(False, False)
        self.root.configure(bg="#69D8FA")
        self.centerWindow(self.root, windowWidth, windowHeight)
        
        #imagen logo
        imagen = imagen.subsample(4,4)
        labelImagen = tk.Label(self.root, image=imagen, bg="#69D8FA")
        labelImagen.image = imagen
        labelImagen.pack(side='top', pady=10)
        
        self.usuarioIndicador = tk.Label(self.root, text="Usuario:", bg="#69D8FA", font=("Arial", 14, "bold"))
        self.usuarioIndicador.pack(pady=5)
        
        self.usuarioText = tk.Entry(self.root, font=('Arial', 12))
        self.usuarioText.pack(pady=5, padx=50, fill='x')
        
        self.contrasenaIndicador = tk.Label(self.root, text="Contraseña:", bg="#69D8FA", font=("Arial", 14, "bold"))
        self.contrasenaIndicador.pack(pady=5)
        
        self.contrasenaText = tk.Entry(self.root, font=('Arial', 12), show='*')
        self.contrasenaText.pack(pady=5, padx=50, fill='x')
        
        #Botones
        buttonFrame = tk.Frame(self.root, bg="#69D8FA")
        buttonFrame.pack(pady=15, padx=50, fill='x')
        
        buttonFrame.columnconfigure(0, weight= 1)
        buttonFrame.columnconfigure(1, weight= 1)
        
        
        self.loginButton = tk.Button(buttonFrame, text="Iniciar sesión", bg="#BBCED4", font=('Arial', 16), command=self.test)
        self.loginButton.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        
        self.registerButton = tk.Button(buttonFrame, text="Registrarse", bg="#BBCED4", font=('Arial', 16))
        self.registerButton.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        
        
        # Iniciar el bucle principal de la ventana
        self.root.mainloop()
        
    def test(self):
        usuario = self.usuarioText.get()
        contrasena = self.contrasenaText.get()
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")
        
        
loginView().loginVista()
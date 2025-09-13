import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import simpledialog
from controladores.register import register
import modelos.usuario


class registerView:
         # Método para centrar la pantalla
    @staticmethod
    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')
        
    def RegisterAction(self):
        #variables de la ventana
        self.root = tk.Tk()
        self.root.title("Registro de Usuario")
        windowWidth = 600
        windowHeight = 475
        icon = PhotoImage(file='img/La Chinita.png')
       
        self.root.iconphoto(False, icon)
        self.root.resizable(False, False)
        self.root.configure(bg="#69D8FA")
        self.centerWindow(self.root, windowWidth, windowHeight)
        
        #imagen logo
        
        #Formulario de usuario
        self.usuarioIndicador = tk.Label(self.root, text="Usuario:", bg="#69D8FA", font=("Arial", 14, "bold"))
        self.usuarioIndicador.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        
        self.usuarioText = tk.Entry(self.root, font=('Arial', 12))
        self.usuarioText.grid(row=1, column=0, sticky='w', padx=10, pady=5)
        
        self.nombreIndicador = tk.Label(self.root, text="Nombre:", bg="#69D8FA", font=("Arial", 14, "bold"))
        self.nombreIndicador.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        
        self.nombreText = tk.Entry(self.root, font=('Arial', 12))
        self.nombreText.grid(row=3, column=0, sticky='w', padx=10, pady=5)
        
        self.apellidoIndicador = tk.Label(self.root, text="Apellido:", bg="#69D8FA", font=("Arial", 14, "bold"))
        self.apellidoIndicador.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        
        self.apellidoText = tk.Entry(self.root, font=('Arial', 12))
        self.apellidoText.grid(row=5, column=0, sticky='w', padx=10, pady=5)
        
        self.contrasenaIndicador = tk.Label(self.root, text="Contraseña:", bg="#69D8FA", font=("Arial", 14, "bold"))
        self.contrasenaIndicador.grid(row=6, column=0, sticky='w', padx=10, pady=5)
        
        self.contrasenaText = tk.Entry(self.root, font=('Arial', 12), show="*")
        self.contrasenaText.grid(row=7, column=0, sticky='w', padx=10, pady=5)
        
        #Formulario roles
        rolFrame = tk.Frame(self.root, bg='#69D8FA')
        rolFrame.grid(sticky='e', padx=10, pady=5)
        rolLabel = tk.Label(self.root, text="Elige un rol:", bg="#69D8FA", font=("Arial", 14, "bold"))
        rolLabel.grid(row=0, column=1, padx=10, pady=5)
        
        rolFrame.columnconfigure(0, weight=1)
        rolFrame.columnconfigure(1, weight=1)
        rolFrame.columnconfigure(2, weight=1)
        
        self.rolVar = tk.IntVar()
        
        self.rolRadioAdmin = tk.Radiobutton(self.root, text='Administrador',bg="#69D8FA", font=("Arial", 12, "bold"), variable=self.rolVar, value=1)
        self.rolRadioAdmin.grid(row=1, column=1,padx=10, pady=5, sticky='w')
        
        self.rolRadioEmpleado = tk.Radiobutton(self.root, text='Empleado',bg="#69D8FA", font=("Arial", 12, "bold"), variable=self.rolVar, value=2)
        self.rolRadioEmpleado.grid(row=2, column=1,padx=10, pady=5, sticky='w')
        
        self.rolRadioCliente = tk.Radiobutton(self.root, text='Cliente',bg="#69D8FA", font=("Arial", 12, "bold"), variable=self.rolVar, value=3)
        self.rolRadioCliente.grid(row=3, column=1,padx=10, pady=5, sticky='w')
        
        #Botones
        buttonFrame = tk.Frame(self.root, bg="#69D8FA")
        buttonFrame.grid( sticky='s', padx=10, pady=5)
        
        buttonFrame.columnconfigure(0, weight= 1)
        buttonFrame.columnconfigure(1, weight= 1)
        
        
        self.loginButton = tk.Button(buttonFrame, text="Registrarse", bg="#BBCED4", font=('Arial', 16), command=self.registerAction)
        self.loginButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.registerButton = tk.Button(buttonFrame, text="Menú Inicial", bg="#BBCED4", font=('Arial', 16), command=self.loginAgain)
        self.registerButton.grid(row=0, column=1, padx=10, pady=10)
        
        
        # Iniciar el bucle principal de la ventana
        self.root.mainloop()
        
    def registerAction(self):
        #id automatico
        usuarioIngresado = self.usuarioText.get()
        contresanaIngresada = self.contrasenaText.get()
        rolIngresado = self.rolVar.get()
        nombreIngresado = self.nombreText.get()
        apellidoIngresado = self.apellidoText.get()
        
        datosUsuario = {
            "usuario": usuarioIngresado,
            "contrasena": contresanaIngresada,
            "rol": rolIngresado,
            "nombre": nombreIngresado,
            "apellido": apellidoIngresado,
            "pin": None
        }
        
        if rolIngresado in [1, 2]:
            pinIngresado = simpledialog.askstring("PIN", "Ingrese el PIN para el rol: ")
            datosUsuario["pin"] = pinIngresado
        
            
        resultado = register.registerUser(datosUsuario)
        if resultado:
            messagebox.showinfo("Registro exitoso", "Usuario registrado exitosamente")
            self.root.destroy()
            from vistas.login_view import loginView
            loginView().loginVista()
        else:
            messagebox.showerror("Error en registro", "Ocurrió un error al registrar al usuario")
        
        
        
    def loginAgain(self):
        self.root.destroy()
        from vistas.login_view import loginView
        
        loginView().loginVista()
        
        
        
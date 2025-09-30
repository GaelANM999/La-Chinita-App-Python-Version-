import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from controladores.agregar import agregar

class pantallaAgregar:
    # Método para centrar la pantalla
    @staticmethod
    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')
        
    def agregarVista(self):
        #variables de la ventana
        self.root = tk.Toplevel()
        self.root.title("Agregar Producto")
        windowWidth = 250
        windowHeight = 275
        icon = PhotoImage(file='./img/La Chinita.png')
       
        self.root.iconphoto(False, icon)
        self.root.resizable(False, False)
        self.root.configure(bg="#D3D4D4")
        self.centerWindow(self.root, windowWidth, windowHeight)
        
        self.nombreIndicador = tk.Label(self.root, text="Nombre:", bg="#D3D4D4", font=("Arial", 14, "bold"))
        self.nombreIndicador.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        
        self.nombreText = tk.Entry(self.root, font=('Arial', 12))
        self.nombreText.grid(row=1, column=0, sticky='ew', padx=10, pady=5)
        
        self.precioIndicador = tk.Label(self.root, text="Precio:", bg="#D3D4D4", font=("Arial", 14, "bold"))
        self.precioIndicador.grid(row=2, column=0, sticky='w', padx=10, pady=5)
        
        self.precioText = tk.Entry(self.root, font=('Arial', 12))
        self.precioText.grid(row=3, column=0, sticky='ew', padx=10, pady=5)
        
        self.cantidadIndicador = tk.Label(self.root, text="Cantidad:", bg="#D3D4D4", font=("Arial", 14, "bold"))
        self.cantidadIndicador.grid(row=4, column=0, sticky='w', padx=10, pady=5)
        
        self.cantidadText = tk.Entry(self.root, font=('Arial', 12))
        self.cantidadText.grid(row=5, column=0, sticky='ew', padx=10, pady=5)
        
        #Botones
        buttonFrame = tk.Frame(self.root, bg="#D3D4D4")
        buttonFrame.grid( sticky='s', padx=10, pady=5)
        
        buttonFrame.columnconfigure(0, weight= 1)
        buttonFrame.columnconfigure(1, weight= 1)
        
        self.agregarButton = tk.Button(buttonFrame, text="Agregar", bg="#B3B4B4", font=('Arial', 16), command=self.agregarAction)
        self.agregarButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.cancelarButton = tk.Button(buttonFrame, text="Cancelar", bg="#B3B4B4", font=('Arial', 16), command=self.cancelar)
        self.cancelarButton.grid(row=0, column=1, padx=10, pady=10)
        
        self.root.mainloop()
        
    def agregarAction(self):
        nombreIngresado = self.nombreText.get()
        precioIngresado = self.precioText.get()
        cantidadIngresada = self.cantidadText.get()
        
        datosProductos = {
            "nombre": nombreIngresado,
            "precio": precioIngresado,
            "cantidad": cantidadIngresada
        }
        
        resultado = agregar.agregar(datosProductos)
        if resultado:
            messagebox.showinfo("Registro de producto exitoso","Producto agregado con éxito" )
            self.root.destroy()
        else:
            messagebox.showerror("Error al registrar producto", "Ocurrió un error al registrar el producto")
            
    def cancelar(self):
        self.root.destroy()
        

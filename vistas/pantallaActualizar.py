import tkinter as tk
from tkinter import messagebox, PhotoImage
from controladores.update import update

class pantallaActualizar:
    # Método para centrar la pantalla
    @staticmethod
    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')
        
    def actualizarVista(self):
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
        
        #Botones
        buttonFrame = tk.Frame(self.root, bg="#D3D4D4")
        buttonFrame.grid( sticky='s', padx=10, pady=5)
        
        buttonFrame.columnconfigure(0, weight= 1)
        buttonFrame.columnconfigure(1, weight= 1)
        
        self.nextButton = tk.Button(buttonFrame, text="Siguiente", bg="#B3B4B4", font=('Arial', 16), command=self.validarNombre)
        self.nextButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.cancelarButton = tk.Button(buttonFrame, text="Cancelar", bg="#B3B4B4", font=('Arial', 16), command=self.cancelar)
        self.cancelarButton.grid(row=0, column=1, padx=10, pady=10)
        
        self.root.mainloop()
        
    def validarNombre(self):
        nombreIngresado = self.nombreText.get().strip()
        if not nombreIngresado:
                messagebox.showerror("Error con nombre","Debe llevar un nombre")
                
        from db.conexion import ConexionBD
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM juguetes WHERE nombre = %s", (nombreIngresado,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if producto: 
            self.root.destroy()
            self.modalActualizacion(producto)
        else:
            messagebox.showerror("No encontrado", "No existe el producto: ", nombreIngresado)
            
    def modalActualizacion(self, producto):
        '''Abre la ventana donde debe ir el precio y cantidad a actualziar'''
        nuevaVentana = tk.Toplevel()
        nuevaVentana.title(f"Actualizar: {producto['nombre']}")
        icon = PhotoImage(file='./img/La Chinita.png')
        nuevaVentana.iconphoto(False, icon)
        nuevaVentana.configure(bg="#D3D4D4")
        self.centerWindow(nuevaVentana, 300, 250)
        
        tk.Label(nuevaVentana, text=f"Producto: {producto['nombre']}", bg="#D3D4D4", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(nuevaVentana, text="Nueva cantidad:", bg="#D3D4D4", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
        cantidadText = tk.Entry(nuevaVentana, font=('Arial', 12))
        cantidadText.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(nuevaVentana, text="Nuevo precio:", bg="#D3D4D4", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
        precioText = tk.Entry(nuevaVentana, font=('Arial', 12))
        precioText.grid(row=2, column=1, padx=10, pady=5)
        
    
        def confirmarActualizacion():
            cantidad = cantidadText.get().strip()
            precio = precioText.get().strip()
            datos = {
                "nombre" : producto["nombre"],
                "cantidad" : cantidad,
                "precio" : precio     
            }
            resultado = update.actualizar(datos)
            
            if resultado:
                messagebox.showinfo("Éxito", f"Producto {producto['nombre']} actualizado con éxito")
                nuevaVentana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto")
                
    
                
        tk.Button(nuevaVentana, text="Actualizar", bg="#B3B4B4", font=("Arial", 14), command=confirmarActualizacion).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(nuevaVentana, text="Cancelar", bg="#B3B4B4", font=("Arial", 14), command=self.cancelar).grid(row=3, column=1, columnspan=2, pady=10)
        
    def cancelar(self):
            self.root.destroy()  
import tkinter as tk
from tkinter import messagebox, PhotoImage
from controladores.eliminar import delete

class pantallaEliminar:
    @staticmethod
    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')
        
    def eliminarVista(self):
        #variables de la ventana
        self.root = tk.Toplevel()
        self.root.title("Eliminar Producto")
        windowWidth = 275
        windowHeight = 150
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
        
        self.deleteButton = tk.Button(buttonFrame, text="Siguiente", bg="#B3B4B4", font=('Arial', 16), command=self.validarProducto)
        self.deleteButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.cancelarButton = tk.Button(buttonFrame, text="Cancelar", bg="#B3B4B4", font=('Arial', 16), command=self.cancelar)
        self.cancelarButton.grid(row=0, column=1, padx=10, pady=10)
        
        self.root.mainloop()
        
    def validarProducto(self):
        nombreIngresado = self.nombreText.get().strip()
        if not nombreIngresado:
            messagebox.showerror("Error con nombre", "Debe llevar un nombre")
            return
        
        from db.conexion import ConexionBD
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM juguetes WHERE nombre = %s", (nombreIngresado,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if producto:
            self.root.destroy()
            self.modalEliminar(producto)
        else:
            messagebox.showerror("No encontrado", f"No existe el producto: {nombreIngresado}")
            
    def modalEliminar(self, producto):
        #Abre la ventana donde debe ir el precio y cantidad a actualziar
            nuevaVentana = tk.Toplevel()
            nuevaVentana.title(f"Eliminar: {producto['nombre']}")
            icon = PhotoImage(file='./img/La Chinita.png')
            nuevaVentana.iconphoto(False, icon)
            nuevaVentana.configure(bg="#D3D4D4")
            self.centerWindow(nuevaVentana, 370, 225)
        
            tk.Label(nuevaVentana, text=f"Producto: {producto['nombre']}", bg="#D3D4D4", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

            tk.Label(nuevaVentana, text="Cantidad a eliminar:", bg="#D3D4D4", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
            cantidadText = tk.Entry(nuevaVentana, font=('Arial', 12))
            cantidadText.grid(row=1, column=1, padx=8, pady=5)
    
            def confirmarActualizacion():
                cantidad = cantidadText.get().strip()
                datos = {
                    "nombre" : producto["nombre"],
                    "cantidad" : cantidad  
                }
                resultado = delete.eliminar(datos)
            
                if resultado:
                    messagebox.showinfo("Éxito", f"Producto {producto['nombre']} eliminado con éxito")
                    nuevaVentana.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el producto")
                
            def cancelarModal():
                nuevaVentana.destroy()
                
            #Frame de botones para el tamaño correcto
            buttonFrame = tk.Frame(nuevaVentana, bg="#D3D4D4")
            buttonFrame.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10, pady=10)
        
            buttonFrame.columnconfigure(0, weight=1)
            buttonFrame.columnconfigure(1, weight=1)
            tk.Button(buttonFrame, text="Eliminar", bg="#B3B4B4", font=("Arial", 14), command=confirmarActualizacion).grid(row=0, column=0, sticky='ew', padx=5, pady=5)
            tk.Button(buttonFrame, text="Cancelar", bg="#B3B4B4", font=("Arial", 14), command=cancelarModal).grid(row=0, column=1, sticky='ew', padx=5, pady=5)      
        
            
    def cancelar(self):
        self.root.destroy() 
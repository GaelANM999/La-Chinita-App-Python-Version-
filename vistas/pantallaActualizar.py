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
                  
    def modalActualizacion(self, producto):
        '''Abre la ventana donde debe ir el precio y cantidad a actualizar'''
        nuevaVentana = tk.Toplevel()
        nuevaVentana.title(f"Actualizar: {producto['nombre']}")
        icon = PhotoImage(file='./img/La Chinita.png')
        nuevaVentana.iconphoto(False, icon)
        nuevaVentana.configure(bg="#D3D4D4")
        self.centerWindow(nuevaVentana, 325, 225)
        
        tk.Label(nuevaVentana, text=f"Producto: {producto['nombre']}", bg="#D3D4D4", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(nuevaVentana, text="Nueva cantidad:", bg="#D3D4D4", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
        cantidadText = tk.Entry(nuevaVentana, font=('Arial', 12))
        cantidadText.grid(row=1, column=1, padx=8, pady=5)

        tk.Label(nuevaVentana, text="Nuevo precio:", bg="#D3D4D4", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
        precioText = tk.Entry(nuevaVentana, font=('Arial', 12))
        precioText.grid(row=2, column=1, padx=8, pady=5)
        
    
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
                
        def cancelarModal():
            nuevaVentana.destroy()
          
                
        #Frame de botones para el tamaño correcto
        buttonFrame = tk.Frame(nuevaVentana, bg="#D3D4D4")
        buttonFrame.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10, pady=10)
        
        buttonFrame.columnconfigure(0, weight=1)
        buttonFrame.columnconfigure(1, weight=1)
        
        tk.Button(nuevaVentana, text="Actualizar", bg="#B3B4B4", font=("Arial", 14), command=confirmarActualizacion).grid(row=3, column=0, sticky='ew', padx=5, pady=5)
        tk.Button(nuevaVentana, text="Cancelar", bg="#B3B4B4", font=("Arial", 14), command=cancelarModal).grid(row=3, column=1, sticky='ew', padx=4, pady=4)
        
    def cancelar(self):
            self.root.destroy()
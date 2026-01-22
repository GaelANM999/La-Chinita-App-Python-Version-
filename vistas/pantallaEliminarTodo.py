import tkinter as tk
from tkinter import messagebox, PhotoImage
from controladores.eliminarTodo import deleteAll

class pantallaEliminarTodo:
    @staticmethod
    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        x = (screenWidth // 2) - (width // 2)
        y = (screenHeight // 2) - (height // 2)

        window.geometry(f'{width}x{height}+{x}+{y}')
        
    def eliminarTodoVista(self):
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
        
        self.deleteButton = tk.Button(buttonFrame, text="Eliminar", bg="#B3B4B4", font=('Arial', 16), command=self.eliminarTodoProducto)
        self.deleteButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.cancelarButton = tk.Button(buttonFrame, text="Cancelar", bg="#B3B4B4", font=('Arial', 16), command=self.cancelar)
        self.cancelarButton.grid(row=0, column=1, padx=10, pady=10)
        
        self.root.mainloop()
        
    def eliminarTodoProducto(self):
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
            deleteAll.eliminarTodo(producto) 
            messagebox.showinfo("Baja de producto exitosa","Existencia de producto eliminado con éxito" )
            self.root.destroy()
            
        else:
            messagebox.showerror("No encontrado", f"No existe el producto: {nombreIngresado}")
            
    def cancelar(self):
        self.root.destroy() 
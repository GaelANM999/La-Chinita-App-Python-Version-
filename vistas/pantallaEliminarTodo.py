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
        
    def eliminarTodoProducto(self, producto):
        nombreIngresado = producto["nombre"]
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
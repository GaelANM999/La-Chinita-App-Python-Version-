import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from db.conexion import ConexionBD
from util.util import resource_path


class clienteView:
    
    def pantallaCliente(self):
        
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT id, nombre, precio, cantidad FROM juguetes"
        cursor.execute(query)   
        resultado = cursor.fetchall()
        
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title("La Chinita App Cliente")
        
        icon = PhotoImage(file=resource_path('img/La Chinita.png'))
       
        self.root.iconphoto(False, icon)
        self.root.resizable(False, False)
        self.root.configure(bg="#D3D4D4")
        
        #Estilos para la tabla
        style = ttk.Style(self.root)
        style.configure("Treeview",
                        font=("Helvetica", 16),
                        rowheight=40)
        style.configure("Treeview.Heading",
                        font=("Helvetica", 18, "bold"))
        
        #Tabla
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Precio", "Cantidad"), show="headings")
        
        #Define column headings
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)
        self.tree.heading("Precio", text="Precio", anchor=tk.CENTER)
        self.tree.heading("Cantidad", text="Cantidad", anchor=tk.CENTER)
        
        #Column widths
        self.tree.column("ID", anchor=tk.CENTER, width=60)
        self.tree.column("Nombre", anchor=tk.CENTER, width=180)
        self.tree.column("Precio", anchor=tk.CENTER, width=120)
        self.tree.column("Cantidad", anchor=tk.CENTER, width=170)
        
        
        for row in resultado:
            self.tree.insert('', 'end', values=(
                row.get('id'),
                row.get('nombre'),
                row.get('precio'),
                row.get('cantidad'),
            ))
        
        
        # Frame para la barra de búsqueda
        searchFrame = tk.Frame(self.root, bg="#D3D4D4")
        searchFrame.pack(pady=5, padx=50, fill='x')

        buscarIndicador = tk.Label(searchFrame, text='Búsqueda:', bg="#D3D4D4", font=("Arial", 14, "bold"))
        buscarIndicador.pack(side='left', padx=(0, 10))
        
        self.buscarText = tk.Entry(searchFrame, font=('Arial', 14))
        self.buscarText.pack(side='left', fill='x', expand=True)
        self.buscarText.bind('<Return>', lambda event: self.buscarProducto())
        
        buscarButton = tk.Button(searchFrame, text='Buscar', font=("Arial", 14, "bold"), command=self.buscarProducto)
        buscarButton.pack(side='right', padx=(10,10))
        
        self.tree.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.actualizarTabla()
        self.root.mainloop()
        
    def actualizarTabla(self):
        if not self.buscarText.get():
            seleccion = self.tree.selection()
            if not seleccion:
                for item in self.tree.get_children():
                    self.tree.delete(item)
            
                conn = ConexionBD.conectarBD()
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT id, nombre, precio, cantidad FROM juguetes")
                resultado = cursor.fetchall()
        
                for row in resultado:
                    self.tree.insert('', 'end', values=(
                        row.get('id'),
                        row.get('nombre'),
                        row.get('precio'),
                        row.get('cantidad'),
                    ))
        self.root.after(3000, self.actualizarTabla)
        
    def buscarProducto(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        juguete = self.buscarText.get()
        queryBuscar = "SELECT id, nombre, precio, cantidad FROM juguetes WHERE LOWER(nombre) LIKE LOWER(%s)"
        jugueteBuscar = f"%{juguete}%"
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(queryBuscar, (jugueteBuscar,))
        resultadoBuscar = cursor.fetchall()
        
        for row in resultadoBuscar:
                self.tree.insert('', 'end', values=(
                    row.get('id'),
                    row.get('nombre'),
                    row.get('precio'),
                    row.get('cantidad'),
                ))
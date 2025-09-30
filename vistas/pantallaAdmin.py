import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from db.conexion import ConexionBD


class adminView:
    
    def pantallaAdmin(self):
        
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT id, nombre, precio, cantidad FROM juguetes"
        cursor.execute(query)   
        resultado = cursor.fetchall()
        
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title("La Chinita App Administrador")
        
        icon = PhotoImage(file='img/La Chinita.png')
       
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
        tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Precio", "Cantidad"), show="headings")
        
        #Define column headings
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)
        tree.heading("Precio", text="Precio", anchor=tk.CENTER)
        tree.heading("Cantidad", text="Cantidad", anchor=tk.CENTER)
        
        #Column widths
        tree.column("ID", anchor=tk.CENTER, width=60)
        tree.column("Nombre", anchor=tk.CENTER, width=180)
        tree.column("Precio", anchor=tk.CENTER, width=120)
        tree.column("Cantidad", anchor=tk.CENTER, width=170)
        
        
        for row in resultado:
            tree.insert('', 'end', values=(
                row.get('id'),
                row.get('nombre'),
                row.get('precio'),
                row.get('cantidad'),
            ))
        
        #Botones
        #Frame para botones
        buttonFrame = tk.Frame(self.root, bg="#D3D4D4")
        buttonFrame.pack(pady=15, padx=50, fill='x')
        
        buttonFrame.columnconfigure(0, weight= 1)
        buttonFrame.columnconfigure(1, weight= 1)
        buttonFrame.columnconfigure(2, weight= 1)
        buttonFrame.columnconfigure(3, weight= 1)
        
        #botones con acciones
        self.agregarButton = tk.Button(buttonFrame, text="Agregar", bg="#D3D4D4", font=('Arial', 16), command=self.abrirPantallaAgregar)
        self.agregarButton.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        
        self.updateButton = tk.Button(buttonFrame, text="Actualizar", bg="#D3D4D4", font=('Arial', 16))
        self.updateButton.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        
        self.eliminarButton = tk.Button(buttonFrame, text="Eliminar", bg="#D3D4D4", font=('Arial', 16))
        self.eliminarButton.grid(row=0, column=2, padx=10, pady=10, sticky='ew')
        
        self.eliminarTodoButton = tk.Button(buttonFrame, text="Eliminar todo", bg="#D3D4D4", font=('Arial', 16))
        self.eliminarTodoButton.grid(row=0, column=3, padx=10, pady=10, sticky='ew')
        
        
        tree.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.root.mainloop()
        
    def abrirPantallaAgregar(self):
        from vistas.pantallaAgregar import pantallaAgregar
        pantallaAgregar().agregarVista()
        

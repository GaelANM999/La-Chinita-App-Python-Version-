datosUsuario = {
    "usuario": "",
    "contrasena": "",
    "rol": 0,  # 0 = No hay usuario, 1 = Admin, 2 = Empleado, 3 = Cliente
    "nombre": "",
    "apellido": ""
}

def setDatoUsuario(key, value):
    datosUsuario[key] = value

def getDatoUsuario(key):
    return datosUsuario.get(key, None)
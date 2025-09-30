datosProducto = {
    "nombre": "",
    "precio": 0,
    "cantidad": 0
}

def setDatoProducto(key, value):
    datosProducto[key] = value

def getDatoProducto(key):
    return datosProducto.get(key, None)
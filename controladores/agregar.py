from db.conexion import ConexionBD
import modelos.productos as producto

class agregar():
    
    def agregar():
        
        try:
            conn = ConexionBD.conectarBD()
            cursor = conn.cursor(dictionary=True)
            
            nombreIngresado = producto.get("nombre", "").strip()
            precioIngresado = producto.get("precio", "")
            cantidadIngresada = producto.get("cantidad", "")
            
            if not all([nombreIngresado, precioIngresado, cantidadIngresada]):
                    print("Todos los campos son obligatorios")
                    return False
            if not float(precioIngresado):
                print("Los campos deben ser numéricos")
                return False
            if not int(cantidadIngresada):
                print("Los campos deben ser numéricos")
                return False
            
            query = "INSERT INTO juguetes (nombre, precio, cantidad VALUES (%s, %s, %s)"
            cursor.execute(query, (nombreIngresado, precioIngresado, cantidadIngresada))
            conn.commit()
            
            print("El producto se agregó con éxito")
            return True
            
        except Exception as e:
            print(f"Error al agregar producto")
            return False
        
        finally:
            cursor.close()
            conn.close()
        
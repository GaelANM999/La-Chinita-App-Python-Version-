from db.conexion import ConexionBD
import modelos.productos as producto

class agregar():
    
    def agregar(datosProducto):
        
        try:
            conn = ConexionBD.conectarBD()
            cursor = conn.cursor(dictionary=True)
            
            nombreIngresado = producto.get("nombre", "").strip()
            precioIngresado = producto.get("precio", "").strip()
            cantidadIngresada = producto.get("cantidad", "").strip()
            
            producto.getDatoProducto("nombre")
            
            if not all([nombreIngresado, precioIngresado, cantidadIngresada]):
                    raise ValueError("Todos los campos son obligatorios")
                    return False
            
            try:
                precio = float(precio)
                cantidad = int(cantidad)
            except ValueError:
                raise ValueError("Precio y cantidad deben ser números válidos")
            
            query = "INSERT INTO juguetes (nombre, precio, cantidad VALUES (%s, %s, %s)"
            cursor.execute(query, (nombreIngresado, precioIngresado, cantidadIngresada))
            conn.commit()
            
            print("El producto se agregó con éxito")
            return True
            
        except Exception as e:
            print(f"Error al agregar producto {e}")
            return False
        
        finally:
            cursor.close()
            conn.close()
        
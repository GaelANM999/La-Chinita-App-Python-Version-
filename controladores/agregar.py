from db.conexion import ConexionBD
import modelos.productos as producto

class agregar():
    
    def agregar(datosProducto):
        
        try:
            conn = ConexionBD.conectarBD()
            cursor = conn.cursor(dictionary=True)
            
            nombreIngresado = datosProducto.get("nombre", "").strip()
            precioIngresado = datosProducto.get("precio", "")
            cantidadIngresada = datosProducto.get("cantidad", "")
            
            
            if not all([nombreIngresado, precioIngresado, cantidadIngresada]):
                    raise ValueError("Todos los campos son obligatorios")
            
            try:
                precioIngresado = float(precioIngresado)
                cantidadIngresada = int(cantidadIngresada)
            except ValueError:
                raise ValueError("Precio y cantidad deben ser números válidos")
            '''
            queryCheck = "SELECT id, cantidad FROM juguetes WHERE nombre = %s"
            cursor.execute(queryCheck, (nombreIngresado,))
            productoExistente = cursor.fetchone()
            
            if productoExistente:
                pass'''
            
            query = """INSERT INTO juguetes (nombre, precio, cantidad)
                        VALUES (%s, %s, %s)"""
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
        
from db.conexion import ConexionBD
import modelos.productos as producto

class update:
    
    def actualizar(datosProducto):
        
        try:
            conn = ConexionBD.conectarBD()
            cursor = conn.cursor(dictionary=True)
                
            nombreIngresado = datosProducto.get("nombre","").strip()
            
            if not nombreIngresado:
                raise ValueError("Debe llevar un nombre")
            
            queryCheck = "SELECT id, cantidad FROM juguetes WHERE nombre = %s"
            cursor.execute(queryCheck, (nombreIngresado,))
            productoExistente = cursor.fetchone()
            
            
            
            if productoExistente:
                producto_id = productoExistente.get("id")
                precioIngresado = datosProducto.get("precio", "").strip()
                cantidadIngresada = datosProducto.get("cantidad","").strip()
                
                
                try:
                      
                    cantidad = int(cantidadIngresada)
                    precio = float(precioIngresado)
                except ValueError:
                    raise ValueError("falló el parse")
                
                queryUpdate = ""
                if precioIngresado and cantidadIngresada:
                    queryUpdate = "UPDATE juguetes SET precio = %s, cantidad = %s WHERE id = %s"
                elif precioIngresado and cantidadIngresada is None:
                    queryUpdate = "UPDATE juguetes SET precio = %s WHERE id = %s"
                elif precioIngresado is None and cantidadIngresada:
                    queryUpdate = "UPDATE juguetes SET cantidad = %s WHERE id = %s"
                cursor.execute(queryUpdate, (precio, cantidad, producto_id))
                conn.commit()
                
                cursor.close()
                conn.close()
                print("Producto existente actualizado con nueva cantidad")
                return True
            else:
                raise ValueError("No existe un producton con ese nombre")
        
        except Exception as e:
            print(f"Error al actualizar producto {e}")
            if 'conn' in locals():
                conn.rollback()
                cursor.close()
                conn.close()
            return False
    
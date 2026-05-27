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
                
                if precioIngresado and cantidadIngresada:
                    try:
                        precio = float(precioIngresado)
                        cantidad = int(cantidadIngresada)
                    except ValueError:
                        raise ValueError("formato inválido")
                    queryUpdate = "UPDATE juguetes SET precio = %s, cantidad = %s WHERE id = %s"
                    cursor.execute(queryUpdate, (precio, cantidad, producto_id))
                    
                elif precioIngresado and not cantidadIngresada:
                    try:
                        precio = float(precioIngresado)
                    except ValueError:
                        raise ValueError("Precio con formato inválido")
                    queryUpdate = "UPDATE juguetes SET precio = %s WHERE id = %s"
                    cursor.execute(queryUpdate, (precio, producto_id))
                elif not precioIngresado and cantidadIngresada:
                    try:
                        cantidad = int(cantidadIngresada)
                    except ValueError:
                        raise ValueError("Cantidad con formato inválido")
                    queryUpdate = "UPDATE juguetes SET cantidad = %s WHERE id = %s"
                    cursor.execute(queryUpdate, (cantidad, producto_id))
                else:
                    raise ValueError("Debes ingresar por lo menos un campo a actualizar")
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
    
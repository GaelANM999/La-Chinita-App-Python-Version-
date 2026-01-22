from db.conexion import ConexionBD

class delete:
    
    @staticmethod
    def eliminar(datosProducto):
        conn = None
        cursor = None
        
        try:
            conn = ConexionBD.conectarBD()
            cursor = conn.cursor(dictionary=True)
                
            nombreIngresado = datosProducto.get("nombre","").strip()
            cantidad_str = datosProducto.get("cantidad", "").strip()
            
            if not nombreIngresado:
                raise ValueError("Debe llevar un nombre")
            
            if not cantidad_str:
                raise ValueError("Debe especificar una cantidad a eliminar")
            
            queryCheck = "SELECT id, cantidad FROM juguetes WHERE nombre = %s"
            cursor.execute(queryCheck, (nombreIngresado,))
            productoExistente = cursor.fetchone()
            
            if not productoExistente:
                raise ValueError("No existe un producto con ese nombre")
            
            producto_id = productoExistente.get("id")
            cantidad_existente = productoExistente.get("cantidad", 0)
            
            cantidad_ingresada_str = datosProducto.get("cantidad", "")
            if not cantidad_ingresada_str:
                raise ValueError("Debe especificar una cantidad a eliminar")
            
            try:
                cantidad_a_eliminar = int(cantidad_ingresada_str)
            except ValueError:
                raise ValueError("La cantidad debe ser un número válido")
            
            if cantidad_a_eliminar <= 0:
                raise ValueError("La cantidad a eliminar debe ser mayor a 0")
            
            # Validamos que no intentemos eliminar más de lo que existe
            if cantidad_a_eliminar > cantidad_existente:
                raise ValueError(f"No se pueden eliminar {cantidad_a_eliminar} unidades. Solo existen {cantidad_existente} unidades en stock.")
            
            # Calculamos la nueva cantidad
            nueva_cantidad = cantidad_existente - cantidad_a_eliminar
            
            if nueva_cantidad <= 0:
                queryDelete = "DELETE from juguetes WHERE id = %s"
                cursor.execute(queryDelete, (producto_id,))
                print(f"Se eliminó el producto {nombreIngresado} porque la cantidad llegó a 0")
            else:
                queryUpdate = "UPDATE juguetes SET cantidad = %s WHERE id = %s"
                cursor.execute(queryUpdate, (nueva_cantidad, producto_id))
            
            queryUpdate = "UPDATE juguetes SET cantidad = %s WHERE id = %s"
            
            cursor.execute(queryUpdate, (nueva_cantidad, producto_id))
            conn.commit()
            
            cursor.close()
            conn.close()
            
            print(f"Se eliminaron {cantidad_a_eliminar} unidades de {nombreIngresado}. Cantidad restante: {nueva_cantidad}")
            return True
        
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            if 'conn' in locals():
                conn.rollback()
                if 'cursor' in locals():
                    cursor.close()
                conn.close()
            return False
        except Exception as e:
            print(f"Error al eliminar unidades del producto: {e}")
            if 'conn' in locals():
                conn.rollback()
                if 'cursor' in locals():
                    cursor.close()
                conn.close()
            return False
from db.conexion import ConexionBD
import modelos.productos as producto

class deleteAll:
    
    def eliminarTodo(datosProducto):
        
        try:
            conn = ConexionBD.conectarBD()
            cursor = conn.cursor(dictionary=True)
                
            nombreIngresado = str(datosProducto.get("nombre","").strip())
            
            if not nombreIngresado:
                raise ValueError("Debe llevar un nombre")
            
            queryCheck = "SELECT id, cantidad FROM juguetes WHERE nombre = %s"
            cursor.execute(queryCheck, (nombreIngresado,))
            productoExistente = cursor.fetchone()
            
            if productoExistente:
                producto_id = productoExistente.get("id")
                
                
                queryDelete = "DELETE FROM juguetes WHERE id = %s"
                
                
                cursor.execute(queryDelete, ( producto_id,))
                conn.commit()
                
                cursor.close()
                conn.close()
                print(f"Se eliminó el producto {nombreIngresado} con éxito")
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
    
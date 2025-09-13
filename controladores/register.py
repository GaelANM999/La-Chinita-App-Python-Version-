from db.conexion import ConexionBD
import modelos.usuario as usuario

class register():
    @staticmethod
    def registerUser(datosUsuario):
        
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)
        
        try:
            usuarioIngresado = datosUsuario.get("usuario", "").strip()
            nombreIngresado = datosUsuario.get("nombre", "").strip()
            apellidoIngresado = datosUsuario.get("apellido", "").strip()
            contrasenaIngresada = datosUsuario.get("contrasena", "").strip()
            rolIngresado = datosUsuario.get("rol", "")
            pinIngresado = datosUsuario.get("pin", None)
            
            if not all([usuarioIngresado, nombreIngresado, apellidoIngresado, contrasenaIngresada, rolIngresado]):
                raise ValueError("Todos los campos son obligatorios")
            
            if int(rolIngresado) in [1, 2]:
                queryRol = "SELECT pin FROM roles WHERE id = %s"
                cursor.execute(queryRol,(rolIngresado,))
                resultado = cursor.fetchone()
                
                if not resultado or resultado["pin"] != pinIngresado:
                    raise ValueError("PIN incorrecto")
                
                
            
            query = """INSERT INTO usuarios (usuario, nombre, apellido, contrasena, rol_id)
                    VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (usuarioIngresado, nombreIngresado, apellidoIngresado, contrasenaIngresada, rolIngresado))
            conn.commit()
            
            
            print("Registro de ususario exitoso")
            return True
            
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False
        
        finally:
            cursor.close()
            conn.close()
    

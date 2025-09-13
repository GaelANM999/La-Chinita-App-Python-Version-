from db.conexion import ConexionBD
import modelos.usuario as usuario

class login():
    
    def login(datosUsuario):
        
        
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)
        
        try:
            usuarioIngresado = datosUsuario.get("usuario", "")
            contrasenaIngresada = datosUsuario.get("contrasena", "")
            query = "SELECT id, usuario, nombre, apellido, rol_id FROM usuarios WHERE usuario = %s AND contrasena = %s"
            cursor.execute(query, (usuarioIngresado, contrasenaIngresada))
            resultado = cursor.fetchone()
            
            if not all([usuarioIngresado, contrasenaIngresada]):
                print("Hay campos vacíos")
                return False
           
            
            if resultado is not None:
                datosDic = {
                "id": resultado["id"],
                "usuario": resultado["usuario"],
                "nombre": resultado["nombre"],
                "apellido": resultado["apellido"],
                "rol_id": resultado["rol_id"]
                }
                usuario.setDatoUsuario("usuario", usuarioIngresado)
                usuario.setDatoUsuario("contrasena", contrasenaIngresada)
                usuario.setDatoUsuario("rol", datosDic["rol_id"])
                        
            return True
        
            
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return False
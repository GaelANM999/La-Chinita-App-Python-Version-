from db.conexion import ConexionBD
import modelos.usuario as usuario

class login():
    
    def login(datosUsuario):
        ADMIN = 1
        EMPLEADO = 2
        CLIENTE = 3
        
        conn = ConexionBD.conectarBD()
        cursor = conn.cursor(dictionary=True)
        
        try:
            usuarioIngresado = datosUsuario.get("usuario", "")
            contrasenaIngresada = datosUsuario.get("contrasena", "")
            query = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
            cursor.execute(query,usuarioIngresado, contrasenaIngresada)
            
            if usuarioIngresado is None or contrasenaIngresada is None:
                raise ValueError("Usuario o contraseña no pueden ser nulos")
            
            if cursor.fetchone() is not None:
                usuario.setDatoUsuario("usuario", usuarioIngresado)
                usuario.setDatoUsuario("contrasena", contrasenaIngresada)
                print("Inicio de sesión exitoso")
                return True
            
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return False
from database import mysqlConn, cleverCursor
import datetime


# funcion para validar roles permitidos
def validar_rol(func):
    def wrapper(self):
        if self.rol not in ["aspirante", "consultor"]:
            print("Rol no válido. Solo se permite 'aspirante' o 'consultor'.")
            return
        return func(self)

    return wrapper


# ---------------------------------------------------------------------------------------------------------------------
# Clase usuario para crear usuarios y perfiles
class Usuario:
    def __init__(self, nombre, correo, contrasena, rol):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    @validar_rol  # Decorador para validar el rol
    def guardar_usuario(self):
        # Buscar ID del rol
        cleverCursor.execute("SELECT id FROM roles WHERE nombre = %s", (self.rol,))
        rol_result = cleverCursor.fetchone()
        if not rol_result:
            print("El rol no existe en la base de datos.")
            return
        rol_id = rol_result[0]

        # Insertar en la tabla usuarios
        cleverCursor.execute(
            "INSERT INTO usuarios (nombre_completo, email, contrasena, rol_id) VALUES (%s, %s, %s, %s)",
            (self.nombre, self.correo, self.contrasena, rol_id),
        )
        mysqlConn.commit()
        self.usuario_id = cleverCursor.lastrowid
        print(f"Usuario '{self.nombre}' guardado con ID {self.usuario_id}")

        if self.rol == "aspirante":
            self.crear_perfil()

    # Funcion para validar rol para crear perfil
    def crear_perfil(self):
        resumen = input("Resumen profesional: ")
        experiencia = input("Experiencia laboral: ")
        educacion = input("Educación: ")
        habilidades = input("Habilidades (separadas por comas): ")

        cleverCursor.execute(
            "INSERT INTO perfiles (usuario_id, resumen, experiencia, educacion, habilidades) VALUES (%s, %s, %s, %s, %s)",
            (self.usuario_id, resumen, experiencia, educacion, habilidades),
        )
        mysqlConn.commit()
        print("📄 Perfil creado exitosamente.")
        
        # Metodo para verificar las credenciales del usuario
    @staticmethod  # Decorador estático para verificar credenciales
    def verificar_credenciales(correo, contrasena):
        try:
            cleverCursor.execute(
                "SELECT id FROM usuarios WHERE email = %s AND contrasena = %s",
                (correo, contrasena),
            )
            result = cleverCursor.fetchone()
            if result:
                return result[0]  # Retorna el ID del usuario
            else:
                return None
        except Exception as e:
            print(f"Error al verificar credenciales: {e}")
            return None


# ---------------------------------------------------------------------------------------------------------------------
# Clase Empresa para crear empresas
class Empresa:
    def __init__(self, nombre, descripcion, direccion, telefono, email_contacto):
        self.nombre = nombre
        self.descripcion = descripcion
        self.direccion = direccion
        self.telefono = telefono
        self.email_contacto = email_contacto

    # Metoedo para crear empresas en tabla empresas
    def guardar_empresa(self):
        cleverCursor.execute(
            "INSERT INTO empresas (nombre, descripcion, direccion, telefono, email_contacto) VALUES (%s, %s, %s, %s, %s)",
            (
                self.nombre,
                self.descripcion,
                self.direccion,
                self.telefono,
                self.email_contacto,
            ),
        )
        mysqlConn.commit()
        print(f"Empresa '{self.nombre}' guardada exitosamente.")


# ---------------------------------------------------------------------------------------------------------------------
# Crear ofertas de empleo
class oferta_empleo:
    def __init__(self, titulo, descripcion, empresa_id, cargo_id, fecha_publicacion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.empresa_id = empresa_id
        self.cargo_id = cargo_id
        self.fecha_publicacion = fecha_publicacion

    def guardar_oferta(self):
        cleverCursor.execute(
            "INSERT INTO ofertas (titulo, descripcion, empresa_id, cargo_id, fecha_publicacion) VALUES (%s, %s, %s, %s, %s)",
            (
                self.titulo,
                self.descripcion,
                self.empresa_id,
                self.cargo_id,
                self.fecha_publicacion,
            ),
        )
        mysqlConn.commit()
        print(f"Oferta de empleo '{self.titulo}' guardada exitosamente.")


# ----------------------------------------------------------------------------------------------------------------------
# Clase para consultar ofertas aplicadas
class ofertas_aplicadas:
    def __init__(self, oferta_id, usuario_id, fecha_aplicacion=None):
        self.oferta_id = oferta_id
        self.usuario_id = usuario_id
        self.fecha_aplicacion = (
            fecha_aplicacion if fecha_aplicacion is not None else datetime.date.today()
        )

    # Método para guardar la aplicación a una oferta de empleo
    def guardar_aplicacion(self):
        try:
            cleverCursor.execute(
                "INSERT INTO ofertas_aplicadas (oferta_id, usuario_id, fecha_aplicacion) VALUES (%s, %s, %s)",
                (self.oferta_id, self.usuario_id, self.fecha_aplicacion),
            )
            mysqlConn.commit()  # Confirma los cambios en la base de datos
            print(f"Aplicación a la oferta ID {self.oferta_id} guardada exitosamente.")
            return True  # Indica que la operación fue exitosa
        except Exception as e:
            print(f"Error al guardar la aplicación: {e}")
            # Si ocurre un error, es buena práctica hacer un rollback para deshacer la transacción.
            if "mysqlConn" in globals() and mysqlConn:  # Solo si mysqlConn existe
                mysqlConn.rollback()
            return False  # Indica que la operación falló


# ---------------------------------------------------------------------------------------------------------------------
# Clase para consultar ofertas disponibles
class ofertas_disponibles:
    def __init__(
        self,
        titulo=None,
        descripcion=None,
        empresa_id=None,
        cargo_id=None,
        fecha_publicacion=None,
    ):
        self.titulo = titulo
        self.descripcion = descripcion
        self.empresa_id = empresa_id
        self.cargo_id = cargo_id
        self.fecha_publicacion = fecha_publicacion

    # Método para consultar ofertas de empleo disponibles
    @staticmethod
    def consultar():
        cleverCursor.execute("""
            SELECT
                o.id,
                o.titulo,
                o.descripcion,
                e.nombre AS nombre_empresa,
                c.nombre AS nombre_cargo, -- Ahora obtenemos el nombre del cargo
                o.fecha_publicacion
            FROM
                ofertas AS o
            JOIN
                empresas AS e
            ON
                o.empresa_id = e.id
            JOIN
                cargos AS c -- Unimos con la tabla cargos
            ON
                o.cargo_id = c.id; -- La condición para unir ofertas y cargos
        """)
        return cleverCursor.fetchall()


# ---------------------------------------------------------------------------------------------------------------------
# Clase para aplicar a ofertas de empleo
class aplicar_oferta:
    # Constructor de la clase
    def __init__(self, oferta_id, usuario_id, fecha_aplicacion=None):
        self.aplicacion_data = ofertas_aplicadas(oferta_id, usuario_id, fecha_aplicacion)
    
    # Método para aplicar a una oferta de empleo
    def aplicar(self):
        return self.aplicacion_data.guardar_aplicacion()

# ---------------------------------------------------------------------------------------------------------------------
# Terminal Menu: Muestra un menú interactivo para crear usuarios, empresas, consultar ofertas y aplicar a ellas.


def menu():
    while True:
        print("\n============== MENÚ ==================")
        print("|       1. Crear nuevo usuario        |")
        print("|       2. Crear nueva empresa.       |")
        print("|  3. Consultar ofertas disponibles.  |")
        print("|  4. Crear ofertas (Solo Empleador). |")
        print("|   5. Consultar ofertas aplicadas.   |")
        print("|        6. Aplicar a ofertas.        |")
        print("|              7. Salir               |")
        opcion = input("|Selecciona una opción:           |")
        print("=======================================")

        if opcion == "1":
            print("Creando nuevo usuario, por favor ingresa los siguientes datos:")
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")
            contrasena = input("Contraseña: ")
            rol = input("Rol (aspirante o consultor): ").lower()

            nuevo_usuario = Usuario(nombre, correo, contrasena, rol)
            nuevo_usuario.guardar_usuario()

        elif opcion == "2":
            print("Creando nueva empresa, por favor ingresa los siguientes datos:")
            nombre = input("nombre de la empresa: ")
            descripcion = input("Descripción de la empresa: ")
            direccion = input("Dirección de la empresa: ")
            telefono = input("Teléfono de contacto: ")
            email_contacto = input("Email de contacto: ")

            nueva_empresa = Empresa(
                nombre, descripcion, direccion, telefono, email_contacto
            )
            nueva_empresa.guardar_empresa()

        elif opcion == "3":
            print("Consultando ofertas disponibles...")
            ofertas = ofertas_disponibles.consultar()
            if ofertas:
                print("Ofertas disponibles:")
                for oferta in ofertas:
                    print(
                        f"ID: {oferta[0]}, Título: {oferta[1]}, Descripción: {oferta[2]}, Empresa: {oferta[3]}, Cargo: {oferta[4]}, Fecha de Publicación: {oferta[5]}"
                    )
            else:
                print("No hay ofertas disponibles en este momento.")

        elif opcion == "4":
            print(
                "Creando nueva oferta de empleo, por favor ingresa los siguientes datos:"
            )
            titulo = input("Titulo de la oferta: ")
            descipcion = input("Descripción de la oferta: ")
            empresa_id = input("ID de la empresa: ")
            cargo_id = input("ID del cargo: ")
            fecha_publicacion = input("Fecha de publicación (YYYY-MM-DD): ")

            nueva_empresa = oferta_empleo(
                titulo, descipcion, empresa_id, cargo_id, fecha_publicacion
            )
            nueva_empresa.guardar_oferta()

        elif opcion == "5":
            print("Consultando ofertas aplicadas...")
            cleverCursor.execute("""
                SELECT
                    oa.oferta_id,
                    o.titulo,
                    u.nombre_completo,
                    oa.fecha_aplicacion
                FROM
                    ofertas_aplicadas AS oa
                JOIN
                    ofertas AS o ON oa.oferta_id = o.id
                JOIN
                    usuarios AS u ON oa.usuario_id = u.id;
            """)
            resultados = cleverCursor.fetchall()

            if resultados:
                print("Ofertas aplicadas:")
                for fila in resultados:
                    print(
                        f"Oferta ID: {fila[0]}, Título: {fila[1]}, Usuario: {fila[2]}, Fecha de Aplicación: {fila[3]}"
                    )
            else:
                print("No hay ofertas aplicadas en este momento.")

        elif opcion == "6":
            print("\n--- APLICAR A OFERTAS ---")
            correo = input("Ingresa tu correo electrónico: ").strip()
            contrasena = input("Ingresa tu contraseña: ").strip()
            
            # Autenticar y obtener ID del usuario
            usuario_id_autenticado = Usuario.verificar_credenciales(correo, contrasena) # <<-- Aquí ya recibes un INT o None
            
            if usuario_id_autenticado: # Si es un INT, significa que se autenticó
                print(f"Usuario {correo} autenticado correctamente.")
                
                
                id_oferta_a_aplicar_str = input("Ingresa el ID de la oferta a la que deseas aplicar: ").strip()
                
                try:
                    oferta_id_seleccionada = int(id_oferta_a_aplicar_str)
                    
                    
                    # La fecha_aplicacion se pone automáticamente en el constructor de ofertas_aplicadas
                    nueva_aplicacion_obj = aplicar_oferta(oferta_id_seleccionada, usuario_id_autenticado)
                    
                    if nueva_aplicacion_obj.aplicar():
                        print(f"¡Aplicación a la oferta ID {oferta_id_seleccionada} registrada exitosamente!")
                    else:
                        print(f"No se pudo registrar la aplicación a la oferta ID {oferta_id_seleccionada}. Por favor, inténtalo de nuevo.")
                        
                except ValueError:
                    print("ID de oferta inválido. Por favor, ingresa un número.")
                except Exception as e:
                    print(f"Ocurrió un error inesperado al aplicar a la oferta: {e}")
            else:
                print("Credenciales incorrectas. No se pudo autenticar al usuario.")
                
        elif opcion == "7":
            print("¡Hasta luego!")
            return
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()

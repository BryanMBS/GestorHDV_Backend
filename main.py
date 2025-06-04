# Importando FastAPI y el cursor de la base de datos
from fastapi import FastAPI
from database import cleverCursor

# app = FastAPI() para crear la instancia de FastAPI
app = FastAPI()

#---------------------------------------------------------------------------
# Ruta (Endpoint) para obtener todos los usuarios
@app.get("/Usuarios")
def obtener_usuarios():
    query = """
        SELECT 
            usuarios.id,
            usuarios.nombre_completo,
            usuarios.email,
            roles.nombre AS rol
        FROM usuarios
        JOIN roles ON usuarios.rol_id = roles.id
    """
    cleverCursor.execute(query)
    resultados = cleverCursor.fetchall()

    usuarios = []
    for fila in resultados:
        usuario = {
            "id": fila[0],
            "nombre_completo": fila[1],
            "email": fila[2],
            "rol": fila[3]
        }
        usuarios.append(usuario)

    return usuarios
#---------------------------------------------------------------------------
# Ruta (Endpoint) para obtener todas las empresas
@app.get("/Empresas")
def obtener_empresas():
    query = """
        SELECT
            empresas.id,
            empresas.nombre,
            empresas.descripcion,
            empresas.direccion,
            empresas.telefono,
            empresas.email_contacto
        FROM empresas    
    """
    cleverCursor.execute(query)
    resultados = cleverCursor.fetchall()
    
    empresas = []
    for fila in resultados:
        empresa = {
            "id": fila[0],
            "nombre": fila[1],
            "direccion": fila[3],
            "telefono": fila[4],
            "email_contacto": fila[5]
        }
        empresas.append(empresa)
    
    return empresas
#---------------------------------------------------------------------------
# Ruta (Endpoint) para obtener todos los perfiles
@app.get("/Perfiles")
def obtener_perfiles():
    query = """
        SELECT
            perfiles.id,
            perfiles.usuario_id,
            perfiles.resumen,
            perfiles.experiencia,
            perfiles.educacion,
            perfiles.habilidades,
            usuarios.nombre_completo AS usuario, -- Se mantiene el alias 'usuario' para el nombre completo
            roles.nombre AS rol_nombre          -- Añadimos el nombre del rol
        FROM perfiles
        JOIN usuarios ON perfiles.usuario_id = usuarios.id
        JOIN roles ON usuarios.rol_id = roles.id;
    """
    cleverCursor.execute(query)
    resultados = cleverCursor.fetchall()
    
    perfiles = []
    for fila in resultados:
        perfil = {
            "id": fila[0],         
            "usuario_id": fila[1],  
            "resumen": fila[2],     
            "habilidades": fila[5], 
            "experiencia": fila[3], 
            "educacion": fila[4],   
            "nombre_usuario": fila[6], 
            "nombre_rol": fila[7]    
        }
        perfiles.append(perfil)
    
    return perfiles
#---------------------------------------------------------------------------
# Ruta (Endpoint) para obtener todas las ofertas de empleo
@app.get("/Ofertas")
def obtener_ofertas():
    query = """
        SELECT
            ofertas.id,
            ofertas.titulo,
            ofertas.descripcion,
            empresas.nombre AS empresa,
            cargos.nombre AS cargo,
            ofertas.fecha_publicacion
        FROM ofertas
        JOIN empresas ON ofertas.empresa_id = empresas.id
        JOIN cargos ON ofertas.cargo_id = cargos.id
    """
    cleverCursor.execute(query)
    resultados = cleverCursor.fetchall()
    
    ofertas = []
    for fila in resultados:
        oferta = {
            "id": fila[0],
            "titulo": fila[1],
            "descripcion": fila[2],
            "empresa": fila[3],
            "cargo": fila[4],
            "fecha_publicacion": fila[5]
        }
        ofertas.append(oferta)
    
    return ofertas
#---------------------------------------------------------------------------
# Ruta (Endpoint) para obtener todas las ofertas aplicadas
@app.get("/Ofertas Aplicadas")
def obtener_ofertas_aplicadas():
    query = """
        SELECT
            ofertas_aplicadas.id,
            usuarios.nombre_completo AS usuario,
            ofertas.titulo AS oferta,
            ofertas.fecha_publicacion
        FROM ofertas_aplicadas
        JOIN usuarios ON ofertas_aplicadas.usuario_id = usuarios.id
        JOIN ofertas ON ofertas_aplicadas.oferta_id = ofertas.id
    """
    cleverCursor.execute(query)
    resultados = cleverCursor.fetchall()
    
    ofertas_aplicadas = []
    for fila in resultados:
        oferta_aplicada = {
            "id": fila[0],
            "usuario": fila[1],
            "oferta": fila[2],
            "fecha_publicacion": fila[3]
        }
        ofertas_aplicadas.append(oferta_aplicada)
    
    return ofertas_aplicadas
#---------------------------------------------------------------------------

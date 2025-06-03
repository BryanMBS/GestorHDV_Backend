<a name="readme-top"></a>

<div align="center">
  <h3><b>SISTEMA DE GESTION DE EMPLEOS</b></h3>
</div>

## 📗 Tabla de Contenidos
- [📖 Sobre el Proyecto](#about-project)
- [🛠 Construido Con](#tech-stack)
- [Características Clave](#key-features)
- [🚀 Demostración en Vivo](#live-demo)
- [💻 Primeros Pasos](#getting-started)
  - [Configuración](#setup)
  - [Requisitos Previos](#prerequisites)
  - [Instalación](#install)
  - [Uso](#usage)
  - [Ejecutar Pruebas](#usage)
  - [Despliegue](#usage)
- [👥 Autores](#authors)
- [🔭 Características Futuras](#key-features)
- [🤝 Contribuciones](#contributing)
- [⭐️ Muestra tu Apoyo](#support)
- [🙏 Agradecimientos](#acknowledgements)
- [📝 Licencia](#license)

## 📖 Sistema de Gestión de Empleo <a name="about-project"></a>

Sistema de Gestión de Empleo es un backend robusto diseñado para administrar usuarios, empresas, ofertas de empleo y las aplicaciones a estas ofertas. Está construido con FastAPI, lo que te permite interactuar con él a través de una API RESTful, y cuenta con una interfaz de terminal para una gestión directa.

## 🛠 Pila Tecnológica <a name="tech-stack"></a>

<details>
<summary>Backend</summary>

- Python  
- FastAPI  
- Uvicorn  

</details>

<details>
<summary>Base de Datos</summary>

- MySQL  
- MySQL Connector/Python  

</details>

<details>
<summary>Otros</summary>

- Git  
- GitHub Actions  
- Linters  

</details>

## Características Clave <a name="key-features"></a>

- **Gestión de Usuarios**: Creación y administración de perfiles para aspirantes, consultores y empleadores.  
- **Registro de Empresas**: Funcionalidad para añadir y gestionar la información de empresas.  
- **Publicación de Ofertas**: Permite a los empleadores publicar nuevas ofertas de empleo.  
- **Aplicación a Ofertas**: Los aspirantes pueden aplicar a las ofertas disponibles.  
- **Interacción por Terminal**: Acceso a las funcionalidades principales a través de un menú interactivo en la línea de comandos.  
- **API RESTful**: Exposición de endpoints para la gestión programática a través de FastAPI.  
- **Persistencia de Datos**: Almacenamiento seguro de toda la información en una base de datos MySQL.  

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## 🚀 Demostración en Vivo <a name="live-demo"></a>

Actualmente, este proyecto no cuenta con una demo en vivo pública, pero puedes ejecutarlo localmente siguiendo las instrucciones de uso.  
La API se expone en `http://127.0.0.1:8000/docs` para una interacción interactiva.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## 💻 Primeros Pasos <a name="getting-started"></a>

Para obtener una copia local y ponerla en marcha, sigue estos pasos:

### Requisitos Previos <a name="prerequisites"></a>

Necesitas las siguientes herramientas:

- Python 3.8+  
- pip  
- MySQL Server  
- VS Code (o tu editor preferido)  
- Git  

### Configuración <a name="setup"></a>

Clona este repositorio:

bash
git clone https://github.com/BryanMBS/GestorHDV_Backend.git
cd GestorHDV_Backend

### Instalación <a name="install"></a>
Crea y activa un entorno virtual:

bash

python -m venv venv
### source venv/bin/activate  # En Linux/macOS
### o: .\venv\Scripts\activate     # En Windows PowerShell
### o: venv\Scripts\activate.bat   # En Windows CMD

Instala las dependencias:

bash

pip install fastapi uvicorn "mysql-connector-python"
o si usas PyMySQL:
pip install pymysql

# Configura tu base de datos MySQL:

Las credenciales están en el archivo database.py.

Importa el archivo .sql con la estructura y datos:

bash

mysql -u tu_usuario -p tu_nombre_de_la_base_de_datos < archivo.sql

# Uso <a name="usage"></a>

### 1. Interfaz de Terminal

bash

python terminal_menu.py

### 2. API RESTful

bash

uvicorn main:app --reload

## Accede a la documentación:

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Autores <a name="authors"></a>

👤 BRYAN MORA

GitHub: @BryanMBS

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

🤝 Contribuciones <a name="contributing"></a>
¡Las contribuciones, problemas y solicitudes de funcionalidades son bienvenidas!
Revisa la sección de issues para más detalles.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>
⭐️ Muestra tu Apoyo <a name="support"></a>
Si te gusta este proyecto, por favor dale una estrella ⭐ en GitHub. ¡Tu apoyo es muy apreciado!

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>
🙏 Agradecimientos <a name="acknowledgements"></a>
Agradezco a Dios por darme la fuerza para llevar a cabo este proyecto, y a los instructores del SENA por brindarnos ejercicios que fortalecen nuestras habilidades en desarrollo de software.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>
📝 Licencia <a name="license"></a>
Este proyecto está bajo la licencia MIT.

&lt;a name="readme-top">&lt;/a>

&lt;div align="center">

&lt;h3>&lt;b>Sistema de Gestión de Empleo&lt;/b>&lt;/h3>

&lt;/div>

📗 Tabla de Contenidos
📖 Sobre el Proyecto
🛠 Construido Con
Pila Tecnológica
Características Clave
🚀 Demostración en Vivo
💻 Primeros Pasos
Configuración
Requisitos Previos
Instalación
Uso
Ejecutar Pruebas
Despliegue
👥 Autores
🔭 Características Futuras
🤝 Contribuciones
⭐️ Muestra tu Apoyo
🙏 Agradecimientos
📝 Licencia
📖 Sistema de Gestión de Empleo &lt;a name="about-project">&lt;/a>
Sistema de Gestión de Empleo es un backend robusto diseñado para administrar usuarios, empresas, ofertas de empleo y las aplicaciones a estas ofertas. Está construido con FastAPI, lo que te permite interactuar con él a través de una API RESTful, y cuenta con una interfaz de terminal para una gestión directa.

Pila Tecnológica &lt;a name="tech-stack">&lt;/a>
&lt;details>
&lt;summary>Backend&lt;/summary>
&lt;ul>
&lt;li>&lt;a href="[enlace sospechoso eliminado]">Python&lt;/a>&lt;/li>
&lt;li>&lt;a href="[enlace sospechoso eliminado]">FastAPI&lt;/a>&lt;/li>
&lt;li>&lt;a href="[enlace sospechoso eliminado]">Uvicorn&lt;/a>&lt;/li>
&lt;/ul>
&lt;/details>
&lt;details>
&lt;summary>Base de Datos&lt;/summary>
&lt;ul>
&lt;li>&lt;a href="[enlace sospechoso eliminado]">MySQL&lt;/a>&lt;/li>
&lt;li>&lt;a href="[enlace sospechoso eliminado]">MySQL Connector/Python&lt;/a>&lt;/li>
&lt;/ul>
&lt;/details>
&lt;details>
&lt;summary>Otros&lt;/summary>
&lt;ul>
&lt;li>Git&lt;/li>
&lt;li>GitHub Actions&lt;/li>
&lt;li>Linters&lt;/li>
&lt;/ul>
&lt;/details>

Características Clave &lt;a name="key-features">&lt;/a>
Gestión de Usuarios: Creación y administración de perfiles para aspirantes, consultores y empleadores.
Registro de Empresas: Funcionalidad para añadir y gestionar la información de empresas.
Publicación de Ofertas: Permite a los empleadores publicar nuevas ofertas de empleo.
Aplicación a Ofertas: Los aspirantes pueden aplicar a las ofertas disponibles.
Interacción por Terminal: Acceso a las funcionalidades principales a través de un menú interactivo en la línea de comandos.
API RESTful: Exposición de endpoints para la gestión programática a través de FastAPI.
Persistencia de Datos: Almacenamiento seguro de toda la información en una base de datos MySQL.
&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

🚀 Demostración en Vivo &lt;a name="live-demo">&lt;/a>
Actualmente, este proyecto no cuenta con una demo en vivo pública, pero puedes ejecutarlo localmente siguiendo las instrucciones de uso. La API se expone en http://127.0.0.1:8000/docs para una interacción interactiva.

&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

💻 Primeros Pasos &lt;a name="getting-started">&lt;/a>
Para obtener una copia local y ponerla en marcha, sigue estos pasos.

Requisitos Previos &lt;a name="prerequisites">&lt;/a>
Para ejecutar este proyecto, necesitas las siguientes herramientas:

Python 3.8+
pip (el gestor de paquetes de Python)
Una instancia de MySQL Server en ejecución.
VS Code (o tu editor de código preferido)
Git
Configuración &lt;a name="setup">&lt;/a>
Clona este repositorio:
Bash

git clone [](https://github.com/BryanMBS/GestorHDV_Backend.git)
cd [](https://github.com/BryanMBS/GestorHDV_Backend.git)
Instalación &lt;a name="install">&lt;/a>
Crea y activa un entorno virtual (recomendado):

Bash

python -m venv venv
source venv/bin/activate  # En Linux/macOS
# o: .\venv\Scripts\activate # En Windows (PowerShell)
# o: venv\Scripts\activate.bat # En Windows (CMD)
Instala las dependencias del proyecto:
Asegúrate de tener un archivo requirements.txt en la raíz del proyecto con todas las dependencias. Si no lo tienes, puedes instalar las principales manualmente:

Bash

pip install fastapi uvicorn "mysql-connector-python"
# Si utilizas PyMySQL en lugar de mysql-connector-python, instala:
# pip install pymysql

Configura tu base de datos MySQL:

R: Las credenciales de la base de datos se configuran en el archivo database.py (o similar) en la raíz del proyecto.
&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

Importa el archivo .sql que contiene la definición de las tablas y algunos insert usados. Puedes cargarlo así desde la línea de comandos:

Bash

mysql -u tu_usuario -p tu_nombre_de_la_base_de_datos < tu_archivo.sql
(El sistema te pedirá la contraseña de tu usuario de MySQL).
Uso &lt;a name="usage">&lt;/a>

Este proyecto ofrece dos modos de interacción:

1. Interfaz de Terminal (CLI)
Para interactuar con el sistema a través de un menú interactivo en la línea de comandos:

Bash

python terminal_menu.py
2. Acceso a la API (FastAPI)
Para iniciar el servidor de la API RESTful:

Bash

fastapi dev main.py

Una vez que el servidor esté en ejecución, podrás acceder a la documentación interactiva de la API en tu navegador:
http://127.0.0.1:8000/docs

O a la documentación alternativa (Redoc):
http://127.0.0.1:8000/redoc

👥 Autores &lt;a name="authors">&lt;/a>
👤 BRYAN MORA

GitHub: @BryanMBS
&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

🤝 Contribuciones &lt;a name="contributing">&lt;/a>
¡Las contribuciones, problemas y solicitudes de características son bienvenidas!

No dudes en revisar la página de issues (asegúrate de que este enlace apunte a tu propio repositorio de GitHub).

&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

⭐️ Muestra tu Apoyo &lt;a name="support">&lt;/a>
Si te gusta este proyecto, ¡por favor dale una estrella en GitHub! Tu apoyo es muy apreciado.

&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

🙏 Agradecimientos &lt;a name="acknowledgements">&lt;/a>
Me gustaría agradecer a Dios por darme la fuerza para llevar a cabo este proyecto y a los instuctores del SENA quienes nos brindan este tipo de ejercicios para practicar y asi crecer en el ambito inmenso que es el desarrollo de software.

&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

📝 Licencia &lt;a name="license">&lt;/a>
Este proyecto está bajo la licencia MIT.

&lt;p align="right">(&lt;a href="#readme-top">volver arriba&lt;/a>)&lt;/p>

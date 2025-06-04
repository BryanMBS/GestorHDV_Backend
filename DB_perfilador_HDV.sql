-- Creación de la base de datos y tablas para el perfilador de ofertas de empleo HDV
CREATE DATABASE IF NOT EXISTS DB_perfilador_HDV;

USE DB_perfilador_HDV;

-- Tabla de roles
CREATE TABLE roles IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de usuarios
CREATE TABLE usuarios IF NOT EXISTS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

-- Tabla de perfiles (solo para aspirantes)
CREATE TABLE perfiles IF NOT EXISTS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    resumen TEXT,
    experiencia TEXT,
    educacion TEXT,
    habilidades TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Tabla de empresas
CREATE TABLE empresas IF NOT EXISTS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email_contacto VARCHAR(100)
);

-- Tabla de cargos (categorías o tipos de trabajo)
CREATE TABLE cargos IF NOT EXISTS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla de ofertas
CREATE TABLE ofertas IF NOT EXISTS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    empresa_id INT NOT NULL,
    cargo_id INT NOT NULL,
    fecha_publicacion DATE,
    FOREIGN KEY (empresa_id) REFERENCES empresas(id),
    FOREIGN KEY (cargo_id) REFERENCES cargos(id)
);

-- Tabla de ofertas aplicadas
CREATE TABLE ofertas_aplicadas IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    oferta_id INT NOT NULL,
    usuario_id INT NOT NULL,
    fecha_aplicacion DATE,
    FOREIGN KEY (oferta_id) REFERENCES ofertas(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Ingresando datos para cargos
INSER INTO cargos (nombre) VALUES
('Desarrollador Web');
INSER INTO cargos (nombre) VALUES
('Diseñador grafico');
INSER INTO cargos (nombre) VALUES
('Analista de Datos');
INSER INTO cargos (nombre) VALUES
('Desarrollador frontend');
INSER INTO cargos (nombre) VALUES
('Desarrollador backend');
INSER INTO cargos (nombre) VALUES
('Desarrollador Full Stack');
INSER INTO cargos (nombre) VALUES
('Administrador de Bases de Datos');

-- Ingresando datos para la tabla empresas
INSERT INTO empresas (nombre, descripcion, direccion, telefono, email_contacto) VALUES
('Tech Innovators Inc.', 'Líder en soluciones de software a medida y desarrollo de aplicaciones web.', 'Calle 10 # 5-20, Bogotá', '+573101234567', 'contacto@techinnovators.com');

INSERT INTO empresas (nombre, descripcion, direccion, telefono, email_contacto) VALUES
('Quantum Coders', 'Empresa especializada en inteligencia artificial y desarrollo de sistemas cuánticos.', 'Av. El Dorado # 68-50, Medellín', '+573209876543', 'info@quantumcoders.dev');

INSERT INTO empresas (nombre, descripcion, direccion, telefono, email_contacto) VALUES
('Pixel Pioneers', 'Estudio de desarrollo de videojuegos y experiencias interactivas en 3D.', 'Carrera 7 # 32-10, Cali', '+573001122334', 'hello@pixelpioneers.games');

INSERT INTO empresas (nombre, descripcion, direccion, telefono, email_contacto) VALUES
('Data Driven Solutions', 'Consultoría en análisis de datos, big data y desarrollo de plataformas de BI.', 'Diagonal 23 # 4-15, Barranquilla', '+573155678901', 'consultas@datadriven.co');

INSERT INTO empresas (nombre, descripcion, direccion, telefono, email_contacto) VALUES
('CloudVerse Technologies', 'Proveedores de servicios en la nube y desarrollo de infraestructura escalable.', 'Transversal 12 # 8-30, Bucaramanga', '+573054321098', 'support@cloudverse.tech');

-- Ingresando datos para la tabla ofertas
INSERT INTO ofertas (titulo, descripcion, empresa_id, cargo_id, fecha_publicacion) VALUES
('Desarrollador Frontend Senior', 'Buscamos un desarrollador frontend experimentado con dominio de React y Vue.js para liderar proyectos innovadores.', 1, 1, '2025-05-28');

INSERT INTO ofertas (titulo, descripcion, empresa_id, cargo_id, fecha_publicacion) VALUES
('Ingeniero de Backend Junior (Python/Node.js)', 'Oportunidad para un ingeniero backend con pasión por construir APIs robustas y escalables utilizando Python o Node.js.', 2, 2, '2025-05-29');

INSERT INTO ofertas (titulo, descripcion, empresa_id, cargo_id, fecha_publicacion) VALUES
('Desarrollador Fullstack Medior (Java/Spring Boot)', 'Únete a nuestro equipo para trabajar en todas las capas de nuestras aplicaciones empresariales con Java y Spring Boot.', 1, 3, '2025-05-30');

INSERT INTO ofertas (titulo, descripcion, empresa_id, cargo_id, fecha_publicacion) VALUES
('Especialista en DevOps Cloud', 'Necesitamos un experto en automatización de despliegues, CI/CD y gestión de infraestructuras en la nube (AWS/Azure).', 5, 4, '2025-05-31');

INSERT INTO ofertas (titulo, descripcion, empresa_id, cargo_id, fecha_publicacion) VALUES
('Analista de Datos con SQL y Python', 'Si te apasiona extraer insights de grandes volúmenes de datos y tienes fuertes habilidades en SQL y Python, ¡esta es tu oportunidad!', 4, 5, '2025-06-01');

-- Ingresando datos para la tabla usuarios (ID de roles: 1=Cosnsultor, 2=Aspirante)
INSERT INTO usuarios (nombre_completo, email, contrasena, rol_id) VALUES
('Bryan Mora', 'bmora@gmail.com', 'bryan123', 1);

INSERT INTO usuarios (nombre_completo, email, contrasena, rol_id) VALUES
('Ana García', 'ana.garcia@example.com', 'ana123', 1); 

INSERT INTO usuarios (nombre_completo, email, contrasena, rol_id) VALUES
('Carlos Ruiz', 'carlos.ruiz@techinnovators.com', 'carlos123', 2); 

INSERT INTO usuarios (nombre_completo, email, contrasena, rol_id) VALUES
('Sofía Martínez', 'sofia.admin@example.com', 'sofia123', 2); 

INSERT INTO usuarios (nombre_completo, email, contrasena, rol_id) VALUES
('Juan López', 'juan.lopez@example.com', 'juan123', 1); 

INSERT INTO usuarios (nombre_completo, email, contrasena, rol_id) VALUES
('Laura Pérez', 'laura.support@example.com', 'laura123', 2);

-- Ingresando datos en roles
INSERT INTO roles (nombre) VALUES
('Consultor');
INSERT INTO roles (nombre) VALUES
('Aspirante');
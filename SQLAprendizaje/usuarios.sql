-- Borrar tabla si ya existe
DROP TABLE IF EXISTS usuarios;

-- Crear tabla usuarios
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    fecha_registro DATE NOT NULL
);

-- Insertar usuarios iniciales
INSERT INTO usuarios (nombre, email, fecha_registro) VALUES
('Yuriangel Perez', 'yuriangel@example.com', '2024-01-15'),
('Zoe Solis', 'zoe@example.com', '2024-02-20'),
('Juan García', 'juan@example.com', '2024-03-05'),
('Ana López', 'ana@example.com', '2024-04-10'),
('Luis Torres', 'luis@example.com', '2024-05-18');


CREATE TABLE rol (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE descripcion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion TEXT NOT NULL
);

CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE descuento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    porcentaje DECIMAL(5,2) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL
);

CREATE TABLE precio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    precio DECIMAL(10,2) NOT NULL
);

CREATE TABLE lugar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE estado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE vendedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fk_rol INT,
    fk_lugar INT,
    FOREIGN KEY (fk_rol) REFERENCES rol(id),
    FOREIGN KEY (fk_lugar) REFERENCES lugar(id)
);

CREATE TABLE producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fk_descripcion INT,
    fk_categoria INT,
    fk_descuento INT,
    fk_precio INT,
    fk_vendedor INT,
    fk_estado INT,
    fecha_publicacion DATE NOT NULL,
    FOREIGN KEY (fk_descripcion) REFERENCES descripcion(id),
    FOREIGN KEY (fk_categoria) REFERENCES categoria(id),
    FOREIGN KEY (fk_descuento) REFERENCES descuento(id),
    FOREIGN KEY (fk_precio) REFERENCES precio(id),
    FOREIGN KEY (fk_vendedor) REFERENCES vendedor(id),
    FOREIGN KEY (fk_estado) REFERENCES estado(id)
);

CREATE TABLE comprador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fk_rol INT,
    FOREIGN KEY (fk_rol) REFERENCES rol(id)
);

CREATE TABLE orden (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fk_comprador INT,
    fk_estado INT,
    fecha_orden DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (fk_comprador) REFERENCES comprador(id),
    FOREIGN KEY (fk_estado) REFERENCES estado(id)
);

CREATE TABLE ordenproducto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock INT NOT NULL,
    fk_orden INT,
    fk_producto INT,
    FOREIGN KEY (fk_orden) REFERENCES orden(id),
    FOREIGN KEY (fk_producto) REFERENCES producto(id)
);

CREATE TABLE calificacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    calificacion INT NOT NULL
);

CREATE TABLE calificacion_producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fk_comprador INT,
    fk_producto INT,
    fk_calificacion INT,
    fecha DATE NOT NULL,
    FOREIGN KEY (fk_comprador) REFERENCES comprador(id),
    FOREIGN KEY (fk_producto) REFERENCES producto(id),
    FOREIGN KEY (fk_calificacion) REFERENCES calificacion(id)
);

CREATE TABLE calificacion_vendedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fk_comprador INT,
    fk_vendedor INT,
    fk_calificacion INT,
    fecha DATE NOT NULL,
    FOREIGN KEY (fk_comprador) REFERENCES comprador(id),
    FOREIGN KEY (fk_vendedor) REFERENCES vendedor(id),
    FOREIGN KEY (fk_calificacion) REFERENCES calificacion(id)
);

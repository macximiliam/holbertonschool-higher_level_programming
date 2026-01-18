-- Crea la base de datos si no existe ya
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selecciona la base de datos para usarla
USE hbtn_0d_usa;

-- Crea la tabla 'cities' si no existe ya
-- state_id es una llave foránea que referencia a states(id)
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
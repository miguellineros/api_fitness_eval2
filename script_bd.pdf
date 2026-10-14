-- 1. Crear la base de datos
CREATE DATABASE fitness_db;

-- 2. Crear el usuario de la aplicación con su contraseña
CREATE USER fitness_user WITH PASSWORD 'tu_password_seguro';

-- 3. Configurar parámetros recomendados para Django
ALTER ROLE fitness_user SET client_encoding TO 'utf8';
ALTER ROLE fitness_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE fitness_user SET timezone TO 'UTC';

-- 4. Asignar los permisos del usuario sobre la base de datos
GRANT ALL PRIVILEGES ON DATABASE fitness_db TO fitness_user;
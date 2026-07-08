# Tienda Tecnología

Proyecto web hecho con Flask + MySQL

## Tecnologías
- Python 3.11.7
- Flask 3.0.3
- MySQL 8

## Ejecución
pip install -r requirements.txt
python run.py

# 🛒 Tienda Tecnología

Aplicación web desarrollada con **Python + Flask + MySQL** para la gestión de productos tecnológicos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar), búsqueda de productos y administración de inventario.

---

# Autor

**Bryan Quishpe**

GitHub:
https://github.com/bryanquishpe-hue

Repositorio:
https://github.com/bryanquishpe-hue/tienda-tecnologia

---

# Objetivo

Desarrollar una aplicación web pequeña que cumpla con los requisitos académicos:

- Aplicación Web
- Lenguaje de programación definido
- Framework definido
- Sistema Operativo definido
- Base de datos definida
- ORM
- Migraciones
- Variables de entorno (.env)
- requirements.txt
- GitHub
- Branch
- Pull Request
- Protección de rama main
- Pruebas
- Despliegue

---

# Tecnologías utilizadas

| Tecnología | Versión |
|------------|----------|
| Python | 3.11.9 |
| Flask | 3.0.3 |
| SQLAlchemy | 2.0.30 |
| Flask-SQLAlchemy | 3.1.1 |
| Flask-Migrate | 4.0.7 |
| PyMySQL | 1.1.1 |
| python-dotenv | 1.0.1 |
| MySQL Server | 8.0 |
| MySQL Workbench | 8.0 CE |
| Visual Studio Code | Última versión |
| Git | 2.x |
| GitHub | Repositorio remoto |

---

# Sistema Operativo

Desarrollo

- Windows 11

Compatible con

- Ubuntu 22.04 LTS

Despliegue compatible con

- Azure App Service
- Azure Database for MySQL Flexible Server

---

# Base de datos

Motor

MySQL 8

Administrador

MySQL Workbench 8

Nombre de la base

```
tienda_tecnologia
```

Tabla

```
productos
```

---

# ORM

Se utiliza

SQLAlchemy

Para administrar la base de datos desde Python.

---

# Migraciones

Se utiliza

Flask-Migrate

Comandos

```bash
flask db init

flask db migrate -m "Primera migracion"

flask db upgrade
```

---

# Variables de entorno

Archivo

```
.env
```

Contenido

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=tienda_tecnologia
DB_USER=root
DB_PASSWORD=********
SECRET_KEY=tienda2026
```

---

# Instalación

## Clonar repositorio

```bash
git clone https://github.com/bryanquishpe-hue/tienda-tecnologia.git
```

Entrar

```bash
cd tienda-tecnologia
```

---

## Crear entorno virtual

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar

```bash
python run.py
```

Abrir

```
http://127.0.0.1:5000
```

---

# requirements.txt

```text
Flask==3.0.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
PyMySQL==1.1.1
python-dotenv==1.0.1
SQLAlchemy==2.0.30
```

---

# Estructura del proyecto

```
tienda-tecnologia/

│

├── app/

│ ├── __init__.py

│ ├── config.py

│ ├── models.py

│ ├── routes.py

│

│ ├── static/

│ │ └── style.css

│

│ └── templates/

│ ├── index.html

│ ├── agregar.html

│ └── editar.html

│

├── migrations/

├── .env

├── .gitignore

├── README.md

├── requirements.txt

└── run.py
```

---

# Funcionalidades

✔ Mostrar productos

✔ Buscar productos

✔ Agregar productos

✔ Editar productos

✔ Eliminar productos

✔ Inventario

---

# Base de datos

Crear

```sql
CREATE DATABASE tienda_tecnologia;
```

Seleccionar

```sql
USE tienda_tecnologia;
```

Tabla

```sql
CREATE TABLE productos(

id INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(100),

precio DECIMAL(10,2),

stock INT

);
```

Insertar

```sql
INSERT INTO productos(nombre,precio,stock)
VALUES
('Laptop Lenovo',750,10),
('Mouse Logitech',18,30),
('Teclado Redragon',45,20);
```

---

# Git

Inicializar

```bash
git init
```

Agregar

```bash
git add .
```

Commit

```bash
git commit -m "Primer commit"
```

Crear rama

```bash
git checkout -b desarrollo
```

Subir

```bash
git push origin desarrollo
```

Actualizar main

```bash
git checkout main

git pull origin main
```

---

# GitHub

Repositorio remoto

```
origin
```

Ramas

```
main

desarrollo
```

Flujo

```
desarrollo

↓

Pull Request

↓

main
```

---

# Protección de la rama main

Configuración en GitHub

Settings

↓

Branches

↓

Branch Protection Rules

Activar

✔ Require a pull request before merging

✔ Require approvals

✔ Restrict pushes

✔ Require status checks

---

# Pull Request

Todo cambio se realiza en una rama secundaria.

Después se crea un Pull Request hacia la rama principal.

---

# Pruebas

Ejecutar

```bash
python run.py
```

Comprobar

✔ Inicio del sistema

✔ Conexión MySQL

✔ CRUD

✔ Búsqueda

✔ Inserción

✔ Eliminación

---

# Despliegue

Compatible con

Azure App Service

Azure Database for MySQL Flexible Server

---

# Licencia

MIT License

Copyright (c) 2026 Bryan Quishpe

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

---

# Conclusión

Este proyecto implementa una aplicación web utilizando Flask y MySQL, siguiendo buenas prácticas de desarrollo:

- Arquitectura organizada.
- Uso de ORM.
- Variables de entorno.
- Control de versiones con Git.
- Gestión mediante ramas.
- Pull Request.
- Protección de la rama principal.
- Preparado para despliegue en Azure.
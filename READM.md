# 📰 Blog Informativo – Proyecto Final Django (Informatorio 2025)

Proyecto colaborativo desarrollado en el marco del **Informatorio Chaco 2025**, construido con **Django** y **Python**.  
El objetivo principal es ofrecer un espacio dinámico para compartir **noticias, análisis y tendencias del mundo tecnológico**, acercando la informática a personas de todos los niveles.

---

## 🚀 Tecnologías utilizadas

- **Python 3.x**  
- **Django 5.x**  
- **HTML5 / CSS3**  
- **Bootstrap 5**  
- **SQLite3** (base de datos por defecto)  
- **django-crispy-forms** + **crispy-bootstrap5**  
- **Pillow** (manejo de imágenes)  

> Las versiones exactas de los paquetes están en `requirements.txt`.
---

## 🧩 Características principales

- **Gestión de usuarios**
  - Registro
  - Inicio de sesión / Logout
  - CRUD (crear, editar, eliminar) usuarios
  - Roles básicos y permisos

- **Blog**
  - Listado de artículos
  - Detalle de artículo
  - Crear / editar / eliminar artículos (según permisos)
  - Imágenes asociadas a artículos

- **Categorías**
  - Administración de categorías
  - Filtrado de artículos por categoría

- **Sistema de comentarios**
  - Agregar comentarios por artículo
  - Gestión de comentarios desde el administrador

- **Páginas informativas**
  - Inicio
  - About / Nosotros
  - Contacto (formulario funcional)

- **Formularios**
  - Django Forms con `crispy-forms`
  - Validaciones y mensajes de error/éxito

- **Interfaz**
  - Diseño simple, orientado a la lectura y responsive con Bootstrap

---

## 📦 Instalación

> A continuación se muestran comandos para sistemas Unix/macOS y Windows. Ajustá según tu sistema.

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/deborah-obes/Proyecto-final-Django.git


2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv

4. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt


5. **Aplicar migraciones: python manage.py makemigrations**
   ```bash
   python manage.py migrate


6. **Crear superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
    
7. **Ejecución del proyecto:**
   ```bash
   python manage.py runserver

8. **Luego abrir en el navegador:**
   ```bash
     http://127.0.0.1:8000/


## 🖼️ Views del proyecto:
<p align="center">
  <img src="https://github.com/user-attachments/assets/b2d828aa-7063-40ed-a3a8-46945afbfda6" height="200"/>
  <img src="https://github.com/user-attachments/assets/31e9e0b7-ee96-41e4-83a2-616c07513da4" height="200"/>
  <img src="https://github.com/user-attachments/assets/fc0399f6-f66e-49f8-920e-a2cdeac465c2" height="200"/>
  <img src="https://github.com/user-attachments/assets/d1186e1a-c4a7-4e64-9bbd-b84aa0e08bd8" height="200"/>
  <img src="https://github.com/user-attachments/assets/231c03e1-5b2c-486b-8167-40bc798c4a4f" height="200"/>
  <img src="https://github.com/user-attachments/assets/3101ae9a-ca1b-4eaa-ada0-3ca7700e19ee" height="200"/>
</p>

## 📁 Estructura del proyecto:

Proyecto-final-Django/

│

├── blog/

│   ├── migrations/

│   ├── templates/blog/

│   └── models.py

│

├── category/

│   ├── templates/category/

│   └── models.py

│

├── comentario/

│   ├── templates/comentario/

│   └── models.py

│

├── crud_usuario/

│   ├── templates/crud_usuario/

│   └── views.py

│

├── inicio/

│   ├── templates/inicio/

│   └── views.py

│

├── pages/

│   ├── templates/pages/

│   └── views.py

│

├── usuario/

│   ├── templates/usuario/

│   └── models.py

│

├── templates/        # Plantillas globales

├── static/           # CSS, imágenes, etc.

├── requirements.txt

├── manage.py

└── db.sqlite3


 ## 🌐 INFORMATORIO 2025 - 2da Etapa del INFO: Desarrollo Web.
- Profesor: Diego Vargas
- Mentor: Darian Alexis Hiebl
  
⚡Proyecto Final desarrollado por Comision#8 / Grupo#4 -

## 🤝Colaboradores:

- Brenda Torres
- Deborah Obes
- Marianela Cardozo



## 📜 Licencia

Este proyecto puede utilizarse con fines educativos y de práctica.
# Proyecto Django: CRUD de Usuarios con Login

Este proyecto es un sistema básico desarrollado en **Django**, donde se implementa un **CRUD completo de usuarios** con autenticación, registro y manejo de sesiones.  

El proyecto se centra en el aprendizaje y la práctica de las funcionalidades esenciales de Django, incluyendo:

- **Registro de usuarios** con campos personalizados (username, email, fecha de nacimiento).
- **Login y manejo de sesiones** para proteger vistas y redirigir según el estado del usuario.
- **Perfil de usuario**, donde se pueden visualizar y actualizar los datos personales.
- **Eliminar cuenta**, que cierra la sesión y borra los datos del usuario de manera segura.
- **Configuración de un usuario base** mediante `AbstractUser` para extender el modelo de Django.
- Uso de **formularios personalizados** para estilizar los formularios de registro y edición de perfil.

---

## Qué aprendí con este proyecto

1. Cómo **crear un modelo de usuario personalizado** usando `AbstractUser`.
2. Cómo **configurar el CRUD de usuarios**: Create, Read, Update, Delete.
3. Cómo manejar **sesiones y autenticación** con login y logout.
4. Cómo **proteger vistas** con `@login_required` y redirigir según el estado del usuario.
5. Cómo organizar **templates y archivos estáticos** (CSS puro) para una interfaz limpia.

---

## Cómo usar la aplicación

1. **Clonar el repositorio**:

``` bash
git clone https://github.com/MathiasVeraM/django-crud-login.git
cd django-crud-login
```

2. **Crear un entorno virtual**:
``` 
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Instalar las dependencias**:
```
pip install -r requirements.txt
Nota: en este proyecto solo se utiliza Django, por lo que el requirements.txt contiene únicamente esa librería y lo que necesita para funcionar.
```

4. **Aplicar migraciones**:
```
python manage.py makemigrations
python manage.py migrate
```

5. **Ejecutar el servidor**:
``` python
python manage.py runserver
```

6. **Acceder al servidor**:

```
http://localhost:8000/ 
Esto por defecto te lleva a la pantalla de login o de perfil si estas ingresado al sistema
```

7. **Rutas clave**:

```
Registrar un nuevo usuario: http://localhost:8000/account/register/
Login: http://localhost:8000/account/login/
Perfil y edición: http://localhost:8000/account/profile/
```
---

## Notas

Todos los formularios están estilizados con CSS puro.

Se recomienda usar navegadores modernos para que el estilo de los inputs y botones se vea correctamente.

Actualmente no se implementa subida de avatar ni funciones de correo electrónico, pero el proyecto está preparado para agregar estas funcionalidades en el futuro.

---

Autor: Mathias Vera
Tecnologia: Django
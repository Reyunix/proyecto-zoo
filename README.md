# Proyecto de Zoo en FastAPI

Este es un proyecto de clase que simula un sistema de gestión de un zoológico utilizando **FastAPI**. El proyecto implementa un CRUD completo (Crear, Leer, Actualizar, Eliminar) para gestionar tres tipos de recursos: **empleados**, **inventario** y **animales**.

## Funcionalidades

El sistema proporciona las siguientes operaciones para cada recurso:

- **GET**: Obtener información de los recursos.
- **POST**: Crear nuevos recursos (si se implementa).
- **PUT**: Actualizar los recursos existentes.
- **DELETE**: Eliminar los recursos.

### Rutas disponibles:
- **/employees**: Para gestionar la información de los empleados del zoo. Esto incluye detalles como nombre, puesto, salario y horario de trabajo.
  - **GET**: Listar todos los empleados o **/employees/{idEmpleado} devuelve un solo empleado por ID.
  - **POST**: Crear un nuevo empleado en el sistema.
  - **PUT**: Actualizar la información de un empleado.
  - **DELETE**: Eliminar un empleado del sistema.
  
- **/inventory**: Para gestionar el inventario del zoológico, como alimentos, equipo de mantenimiento y otros recursos necesarios para la operación del zoológico.
  - **GET**: Listar los elementos del inventario **/inventory/{idItem} devuelve un solo item por ID.
  - **POST**: Añadir nuevos elementos al inventario.
  - **PUT**: Actualizar la cantidad o la información de un artículo en el inventario.
  - **DELETE**: Eliminar un artículo del inventario.

- **/animals**: Para gestionar la información de los animales del zoológico, como nombre, especie, edad y estado de salud.
  - **GET**: Listar todos los animales o **/animals/{animalName} devuelve un animal por su nombre.
  - **POST**: Crear un nuevo animal en el zoológico.
  - **PUT**: Actualizar la información de un animal.
  - **DELETE**: Eliminar un animal del zoológico.

## Tecnologías utilizadas

- **FastAPI**: Framework para construir la API de manera rápida y eficiente.
- **Pydantic**: Para validaciones y modelos de datos (Basemodel), asegurando que los datos sean correctos y consistentes.
- **JSON**: Archivos JSON simulando una base de datos para almacenar los recursos, lo que facilita el desarrollo y las pruebas.
- **APIRouter**: Para gestionar y organizar las rutas de la API de forma modular, permitiendo una estructura limpia y escalable.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI de manera rápida y eficiente.

## Instalación

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/zoo-fastapi.git

2. Accede al directorio del proyecto
    ```bash
    cd zoo-fastapi


3. Crea un entorno virtual

    ```bash
    
    python -m venv venv

4. Activa el entorno virtual:

    En Windows:
    
        ```bash
        .\venv\Scripts\activate

    En macOS/Linux:
    
        ```bash
        source venv/bin/activate

5. Instala las dependencias del proyecto:

        ```bash

        pip install -r requirements.txt

6. Arranca el servidor uvicorn de FastAPI:
    ```bash

    fastapi dev app/main.py 

7. Accede a la documentación interactiva de la API en:
    ```bash

    http://127.0.0.1:8000/docs

8. Estructura del proyecto
    ```bash    
    .
    ├── app
    │   ├── documents
    │   ├── __init__.py
    │   ├── main.py
    │   ├── models
    │   ├── __pycache__
    │   ├── routers
    │   └── test.py
    ├── README.md
    └── requirements.txt
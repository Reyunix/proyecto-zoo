# Proyecto de Zoo en FastAPI

Este es un proyecto de clase que simula un sistema de gestión de un zoológico utilizando **FastAPI**. El proyecto implementa un CRUD completo (Crear, Leer, Actualizar, Eliminar) para gestionar tres tipos de recursos: **empleados**, **inventario** y **animales**.

## Funcionalidades

El sistema proporciona las siguientes operaciones para cada recurso:

- **GET**: Obtener información de los recursos.
- **POST**: Crear nuevos recursos (si se implementa).
- **PUT**: Actualizar los recursos existentes.
- **DELETE**: Eliminar los recursos.

### Rutas disponibles:
- **/employees**: Para gestionar la información de los empleados del zoo.
- **/inventory**: Para gestionar el inventario del zoológico.
- **/animals**: Para gestionar la información de los animales del zoo.

## Tecnologías utilizadas

- **FastAPI**: Framework para construir la API.
- **Pydantic**: Para validaciones y modelos de datos (Basemodel).
- **JSON**: Archivos JSON simulando una base de datos para almacenar los recursos.
- **APIRouter**: Para gestionar y organizar las rutas de la API.
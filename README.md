# CRUD para Registro de Productos en Python

Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar un registro de productos utilizando Python. 
El registro incluye datos como ID, nombre, descripción, precio y cantidad disponible de cada producto. 
El sistema también incluye un conjunto de pruebas unitarias para garantizar el correcto funcionamiento de cada operación CRUD.

## Características
- Crear un nuevo producto con información relevante (ID, nombre, descripción, precio, cantidad).
- Leer los detalles de un producto existente mediante su ID.
- Actualizar la información de un producto existente.
- Eliminar un producto del registro.
- Validaciones para evitar duplicados o manejar productos inexistentes.
- Persistencia de datos: Los productos se almacenan en un archivo JSON (`data/productos.json`) para garantizar que no se pierdan entre ejecuciones.
- Sistema interactivo mediante un menú en consola.
- Pruebas unitarias básicas para garantizar la calidad del código.

## Requisitos Previos
- Tener Python 3.8 o superior instalado.
- Editor de texto o entorno de desarrollo (recomendado: Visual Studio Code).

## Cómo Ejecutar el Proyecto

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de estar en la carpeta del proyecto:
   ```bash
   cd crud_productos

## Persistencia de Datos

El sistema utiliza un archivo JSON ubicado en la carpeta `data` para almacenar la información de los productos. Cada vez que se realiza una operación CRUD, el archivo `productos.json` se actualiza automáticamente.

- Si el archivo no existe, el sistema lo crea automáticamente.
- Si el archivo está vacío, el sistema lo inicializa como una lista vacía (`[]`).
- El archivo tiene el siguiente formato:
```json
[
    {
        "id": 1,
        "nombre": "Producto1",
        "descripcion": "Descripción del producto 1",
        "precio": 100.0,
        "cantidad": 10
    },
    {
        "id": 2,
        "nombre": "Producto2",
        "descripcion": "Descripción del producto 2",
        "precio": 200.0,
        "cantidad": 5
    }
]


## Tecnologías Utilizadas
- Python 3.11
- Biblioteca `unittest` para pruebas unitarias.
- Visual Studio Code como editor de código.

## Autor
Andres Felipe Montoya Bustamante
Estudiante de Desarrollo de Software del ITM. 

## Docente
Jonathan Sanchez Giraldo
Aplicación y Servicios Web
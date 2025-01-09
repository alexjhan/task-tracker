# task-tracker
This is a code repository for the first roadmap.sh project
https://roadmap.sh/projects/task-tracker

# Task Tracker 🗂️✅

**Task Tracker** es una aplicación de consola 🖥️ para gestionar tus tareas personales. Permite agregar, modificar, eliminar tareas y consultar estadísticas sobre su estado. Las tareas se almacenan en un archivo JSON 📂 para facilitar su persistencia.

## Funcionalidades ✨
- **Crear tareas** ➕: Agrega nuevas tareas con el estado inicial "Sin empezar".
- **Modificar el estado de las tareas** 🔄: Cambia el estado de las tareas entre "Sin empezar", "En progreso" y "Finalizado".
- **Mostrar estadísticas** 📊: Muestra cuántas tareas están en cada estado.
- **Listar tareas** 📜: Muestra todas las tareas con su título, estado y fecha de creación.
- **Eliminar tareas** 🗑️: Elimina tareas del registro.

## Estructura del Proyecto 📁

    /mi_aplicacion
    ├── main.py               # Ejecuta la aplicación
    ├── tareas.py             # Funciones relacionadas con las tareas
    ├── almacenamiento.py     # Módulo para cargar/guardar datos en JSON
    ├── estadisticas.py       # Módulo para mostrar estadísticas
    ├── menu.py               # Módulo para mostrar el menú
    └── tareas.json           # Archivo JSON que almacena las tareas

## Cómo Ejecutar 🚀

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python instalado en tu sistema (preferentemente Python 3).
3. Navega al directorio del proyecto en tu terminal o línea de comandos.
4. Ejecuta el archivo principal con el siguiente comando:

```bash
python main.py

    /mi_aplicacion
    │
    ├── main.py               # Archivo principal que ejecuta la aplicación
    ├── tareas.py             # Módulo para funciones relacionadas con las tareas
    ├── almacenamiento.py     # Módulo para cargar/guardar datos en JSON
    ├── estadisticas.py       # Módulo para funciones de estadísticas
    ├── menu.py               # Módulo para mostrar y gestionar el menú
    └── tareas.json           # Archivo JSON para almacenar las tareas

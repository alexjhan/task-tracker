import json

def load_tasks(filename="tareas.json"):
    """Carga las tareas desde un archivo JSON."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tareas.json"):
    """Guarda las tareas en un archivo JSON."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

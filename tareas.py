from datetime import datetime

from almacenamiento import save_tasks

def create_new_task(tasks):
    """Crea una nueva tarea y la añade a la lista."""
    title = input("Introduce el título de la tarea: ")
    status = "Sin empezar"  # Estado inicial por defecto
    date_and_our = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual
    task = {"title": title, "status": status, "date_and_our": date_and_our}
    tasks.append(task)  # Añade la tarea a la lista
    save_tasks(tasks)  # Guarda los cambios en el archivo JSON
    print("Tarea creada y guardada exitosamente.")

def modify_task_status(tasks):
    """Modifica el estado de una tarea existente."""
    list_tasks(tasks)  # Muestra todas las tareas
    try:
        index = int(input("Selecciona el número de la tarea que deseas modificar: ")) - 1
        if 0 <= index < len(tasks):
            print("Estados disponibles: Sin empezar, En progreso, Finalizado")
            new_status = input("Introduce el nuevo estado: ")
            while True:
                if new_status in ["Sin empezar", "En progreso", "Finalizado"]:
                    break
                else:
                    print("Estado no válido. Inténtalo de nuevo.")
                    new_status = input("Introduce el nuevo estado: ")
            tasks[index]["status"] = new_status
            tasks[index]["date_and_our"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)  # Guarda los cambios en el archivo JSON
            print("Estado modificado exitosamente.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

def list_tasks(tasks):
    """Muestra todas las tareas."""
    if not tasks:
        print("No hay tareas registradas.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['title']} - {task['status']} - {task['date_and_our']}")

def delete_task(tasks):
    """Elimina una tarea existente."""
    list_tasks(tasks)  # Muestra todas las tareas
    try:
        index = int(input("Selecciona el número de la tarea que deseas eliminar: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)  # Elimina la tarea de la lista
            save_tasks(tasks)  # Guarda los cambios en el archivo JSON
            print("Tarea eliminada exitosamente.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

from almacenamiento import load_tasks
from tareas import create_new_task, modify_task_status, list_tasks, delete_task
from estadisticas import show_statistics
from menu import show_menu

def main():
    tasks = load_tasks()  # Carga las tareas desde el archivo JSON

    while True:
        show_menu()
        option = input("Elige una opción (1-6): ")

        if option == "1":
            create_new_task(tasks)
        elif option == "2":
            modify_task_status(tasks)
        elif option == "3":
            show_statistics(tasks)
        elif option == "4":
            list_tasks(tasks)
        elif option == "5":
            delete_task(tasks)
        elif option == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

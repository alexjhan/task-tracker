def show_statistics(tasks):
    """Muestra estadísticas sobre el estado de las tareas."""
    sin_empezar = sum(1 for task in tasks if task["status"] == "Sin empezar")
    en_progreso = sum(1 for task in tasks if task["status"] == "En progreso")
    finalizado = sum(1 for task in tasks if task["status"] == "Finalizado")

    print(f"Tareas sin empezar: {sin_empezar}")
    print(f"Tareas en progreso: {en_progreso}")
    print(f"Tareas finalizadas: {finalizado}")

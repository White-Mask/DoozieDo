import os
import json

import time


def add_task(data):
    os.system("cls || clear")
    task_name = input("Ingresa el nombre de la tarea: ")
    new_task = {"task_name": task_name, "status": "pending"}
    with open(f'projects/{data["project_name"]}.json', "w") as file:
        json.dump(data, file)
    data["tasks"].append(new_task)
    return data


def print_tasks(data, type_task):
    if len(data[type_task]) > 0:
        for index, task in enumerate(data[type_task]):
            print(f"{index + 1}. {task['task_name']} - {task['status']}")
        print("")
    else:
        print("-")


def edit_task(data, task):
    # Editar el nombre de la tarea
    os.system("cls || clear")
    print(f"Nombre de la tarea: {task['task_name']}")
    new_task_name = input("Nuevo nombre de la tarea: ")
    task["task_name"] = new_task_name

    with open(f'projects/{data["project_name"]}.json', "w") as file:
        json.dump(data, file)


def update_status_task(data, task):
    # Mover la tarea de 'tasks' a 'completed_tasks'
    data["tasks"].remove(task)
    task["status"] = "completed"
    data["completed_tasks"].append(task)

    with open(f'projects/{data["project_name"]}.json', "w") as file:
        json.dump(data, file)


def delete_task(data, task):
    data["tasks"].remove(task)
    with open(f'projects/{data["project_name"]}.json', "w") as file:
        json.dump(data, file)


def iterate_projects(data):
    while True:
        os.system("cls || clear")
        title = f"| proyecto: {data['project_name']} |".upper()
        print(len(title) * "=")
        print(f"{title}")
        print(len(title) * "=", end="\n\n")

        print("Tareas pendientes:")
        print_tasks(data, "tasks")

        print("Tareas completadas:")
        print_tasks(data, "completed_tasks")

        print(
            """
Selecciona una opción:
1. Crear una nueva tarea
2. Editar una tarea (selecciona el número de la tarea)
3. Eliminar una tarea (selecciona el número de la tarea)
4. Marcar una tarea como completada (selecciona el número de la tarea)
5. Presiona ENTER para volver al menú principal
        """
        )
        option = input("> Ingresa una opción: ")

        if option == "1":
            add_task(data)
        elif option == "2":
            if len(data["tasks"]) > 0:
                n_taks = input("Ingresa el número de la tarea que deseas editar: ")
                edit_task(data, data["tasks"][int(n_taks) - 1])
            else:
                print("No hay tareas.")
        elif option == "3":
            if len(data["tasks"]) > 0:
                n_taks = input("Ingresa el número de la tarea que deseas eliminar: ")
                delete_task(data, data["tasks"][int(n_taks) - 1])
            else:
                print("No hay tareas.")
        elif option == "4":
            if len(data["tasks"]) > 0:
                n_taks = input(
                    "Ingresa el número de la tarea que deseas marcar como completada: "
                )
                update_status_task(data, data["tasks"][int(n_taks) - 1])
            else:
                print("No hay tareas.")
        elif option == "":
            print("Has seleccionado la opción 5")
            break
        else:
            print("Opción no válida")


def create_project():
    # Debes ingresar el nombre del proyecto
    # Pero si existe el proyecto debes volver a pedir el nombre

    while True:
        # Limpiar la pantalla
        os.system("cls || clear")

        # Pedir el nombre del proyecto o volver al menú principal
        print(
            """
Crear un nuevo proyecto:
1. Ingresa el nombre del proyecto
2. Presiona ENTER para volver al menú principal
"""
        )
        project_name = input(" > ")

        if project_name == "":
            return

        # Si ya existe el proyecto, volver a pedir el nombre
        if not os.path.exists(f"projects/{project_name}.json"):
            break
        else:
            print("El proyecto ya existe...")
            time.sleep(2)

    # Crear el archivo del proyecto
    with open(f"projects/{project_name}.json", "w") as file:
        data = {"project_name": project_name, "tasks": [], "completed_tasks": []}
        json.dump(data, file)
    file.close()
    print(f"Proyecto {project_name} creado correctamente", end=" ")
    time.sleep(2)
    iterate_projects(data)


def initialize_project(list_projects):
    while True:
        print(
            """
Iniciar un proyecto:
 * Ingresa el número del proyecto que deseas iniciar
 * Presiona ENTER para volver al menú principal
"""
        )
        option = input("> ")

        if option == "":
            return

        try:
            project = list_projects[int(option) - 1]
            with open(f"projects/{project}", "r") as file:
                text = file.read()
                os.system("cls || clear")
            file.close()
            break
        except IndexError:
            print("No existe el proyecto")
        except ValueError:
            print("Ingresa un número")
        except Exception:
            print("Ha ocurrido un error")

    return json.loads(text)


def show_projects():
    # Limpiar la pantalla
    os.system("cls || clear")

    print("Proyectos disponibles:")
    # Si no existe la carpeta 'projects' la crea
    if not os.path.exists("projects"):
        print("No hay proyectos...", end=" ")
        # Un input para salir del ciclo
        input("Presiona ENTER para continuar")
        return

    projects = os.listdir("projects")
    for index, project in enumerate(projects):
        print(f"{index + 1}. {project}")

    return projects


def main():
    while True:
        os.system("cls || clear")

        print(
            """
Selecciona una opción:
1. Crear un nuevo proyecto
2. Iniciar un proyecto existente
3. Presiona ENTER para salir 
        """
        )
        option = input("Ingresa una opción: ")

        if option == "1":
            create_project()
        elif option == "2":
            projects = show_projects()
            project = initialize_project(projects)
            iterate_projects(project)
        elif option == "":
            print("Has seleccionado la opción 3")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()

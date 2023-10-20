import os
import json


def create_project():
    #Limpiar la pantalla
    os.system('cls || clear')
    
    project_name = input("Ingresa el nombre del proyecto: ")
    # Si en la carpeta 'DoozieDo' ('DoozieDo' es la carpeta raíz de este programa) no existe la carpeta 'projects' la crea
    # Si ya existe la carpeta 'projects', solamente crea el archivo

    # Si no existe la carpeta 'projects' la crea
    if not os.path.exists('projects'):
        os.makedirs('projects')
    
    # Si no existe el archivo 'projects.json' lo crea
    if not os.path.exists(f'projects/{project_name}.json'):
        with open(f'projects/{project_name}.json', 'w') as file:
            new_schema = {
                "project_name": project_name,
                "tasks": [],
                "completed_tasks": []
            }
            # new_schema es un diccionario y hay que convertirlo a un string para poder escribirlo en el archivo
            json.dump(new_schema, file)
        file.close()

def initialize_project(list_projects):
    while True:
        print("Ingresa el número del proyecto que deseas iniciar:", end=" ")
        option = input()

        try:
            project = list_projects[int(option) - 1]
            with open(f'projects/{project}', 'r') as file:
                text = file.read()
                os.system('cls || clear')
                #print(f"Iniciando el proyecto {data['project_name']}...")
            file.close()
            break
        except IndexError:
            print("No existe el proyecto")
        except ValueError:
            print("Ingresa un número")
        except Exception:
            print("Ha ocurrido un error")
    data = json.loads(text)
    #interate_projects(data)


def show_projects():
    #Limpiar la pantalla
    os.system('cls || clear')
    # Si no existe la carpeta 'projects' la crea
    if not os.path.exists('projects'):
        print("No hay proyectos...", end=' ')
        #Un input para salir del ciclo
        input("Presiona ENTER para continuar")
        return
    
    proyects = os.listdir('projects')
    for index, project in enumerate(proyects):
        print(f"{index + 1}. {project}")

    initialize_project(proyects)


def main():
    while True:
        os.system('cls || clear')

        print('''
Selecciona una opción:
1. Crear un nuevo proyecto
2. Iniciar un proyecto existente
3. Salir
        ''')
        option = input("Ingresa una opción: ")

        if option == '1':
            create_project()
        elif option == '2':
            show_projects()
        elif option == '3':
            print("Has seleccionado la opción 3")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

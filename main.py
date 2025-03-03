import os
import time
import datetime
import prettytable

from tareas import agregar_tarea, listar_tareas, completar_tarea, eliminar_tarea
from storage import guardar_tareas, cargar_tareas

#  Declaramos la lista global de tareas y cargamos desde el archivo JSON
tareas_lista = cargar_tareas()

def main():
    global tareas_lista  #  Ahora sí podemos modificarla dentro de la función

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("📋 Bienvenido al gestor de tareas"
              "\n1️⃣ Agregar tarea"
              "\n2️⃣ Listar tareas"
              "\n3️⃣ Eliminar tarea"
              "\n4️⃣ Completar tarea"
              "\n5️⃣ Cargar tareas"
              "\n0️⃣ Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = agregar_tarea()
            tareas_lista.append(tarea)  # ✅ Agregamos la tarea a la lista
            guardar_tareas(tareas_lista)  # Guardado automático

        elif opcion == "2":
            listar_tareas(tareas_lista)  # ✅ Pasamos la lista

        elif opcion == "3":
            eliminar_tarea(tareas_lista)  # ✅ Pasamos la lista
            guardar_tareas(tareas_lista)  # Guardado automático

        elif opcion == "4":
            completar_tarea(tareas_lista)  # ✅ Pasamos la lista
            guardar_tareas(tareas_lista)  # Guardado automático

        elif opcion == "5":
            tareas_lista = cargar_tareas()  # ✅ Cargamos las tareas desde JSON
            print("📂 Tareas cargadas correctamente.")

        elif opcion == "0":
            print("👋 Saliendo del gestor de tareas...")
            break

        else:
            print("🚫 Opción no válida. Intente nuevamente.")

        time.sleep(2)

if __name__ == "__main__":
    main()
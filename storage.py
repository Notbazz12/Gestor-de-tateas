import os
import datetime
import json
from tareas import Tarea

# Definir la ruta del directorio de datos y el archivo
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TAREAS_FILE = os.path.join(DATA_DIR, "tareas.json")

print(f"Ruta del archivo de tareas: {TAREAS_FILE}")

# 🔹 Asegurar que el directorio data existe
def asegurar_directorio():
    if not os.path.exists(DATA_DIR):
        try:
            os.makedirs(DATA_DIR)
            print(f"Directorio creado: {DATA_DIR}")
        except Exception as e:
            print(f"❌ Error al crear el directorio: {e}")
    else:
        print(f"El directorio ya existe: {DATA_DIR}")

# 🔹 Guardar tareas en un archivo JSON
def guardar_tareas(tareas):
    # Asegurar que el directorio existe
    asegurar_directorio()
    
    print(f"Intentando guardar {len(tareas)} tareas...")
    
    # Convertir las tareas a diccionarios con fechas en formato string
    tareas_dict = []
    for tarea in tareas:
        tarea_dict = tarea.__dict__.copy()
        if isinstance(tarea_dict['fecha_creacion'], datetime.datetime):
            tarea_dict['fecha_creacion'] = tarea_dict['fecha_creacion'].strftime("%Y-%m-%d %H:%M:%S.%f")
        if isinstance(tarea_dict['fecha_limite'], datetime.datetime):
            tarea_dict['fecha_limite'] = tarea_dict['fecha_limite'].strftime("%Y-%m-%d %H:%M:%S.%f")
        tareas_dict.append(tarea_dict)

    try:
        with open(TAREAS_FILE, "w") as archivo:
            json.dump(tareas_dict, archivo, indent=4)
        print(f"💾 Tareas guardadas correctamente en {TAREAS_FILE}")
    except Exception as e:
        print(f"❌ Error al guardar las tareas: {e}")

# 🔹 Cargar tareas desde el archivo JSON
def cargar_tareas():
    # Asegurar que el directorio existe
    asegurar_directorio()
    
    try:
        with open(TAREAS_FILE, "r") as archivo:
            tareas_dict = json.load(archivo)
            return [
                Tarea(
                    t["titulo"], 
                    t["descripcion"], 
                    datetime.datetime.strptime(t["fecha_creacion"], "%Y-%m-%d %H:%M:%S.%f"), 
                    datetime.datetime.strptime(t["fecha_limite"], "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%Y"), 
                    t["estado"]
                ) 
                for t in tareas_dict
            ]
    except FileNotFoundError:
        print("📂 No se encontró el archivo de tareas. Se creará uno nuevo.")
        return []
    except Exception as e:
        print(f"❌ Error al cargar las tareas: {e}")
        return []

# 🔹 Crear un archivo vacío
def crear_archivo():
    try:
        nombre = input("Ingrese el nombre del archivo: ")
        with open(nombre, "w") as archivo:
            archivo.write("")
        print(f"📄 Archivo '{nombre}' creado correctamente.")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

# 🔹 Eliminar un archivo
def eliminar_archivo():
    try:
        nombre = input("Ingrese el nombre del archivo o del directorio: ")
        if os.path.exists(nombre):
            os.remove(nombre)
            print(f"🗑️ Archivo '{nombre}' eliminado correctamente.")
        else:
            print("❌ El archivo no existe.")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")
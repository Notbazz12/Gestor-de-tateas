import datetime
import prettytable

class Tarea:
    def __init__(self, titulo, descripcion, fecha_creacion, fecha_limite, estado="Pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.fecha_limite = datetime.datetime.strptime(fecha_limite, "%d/%m/%Y")
        self.estado = estado

    def __str__(self):
        return f"{self.titulo} - {self.descripcion} - {self.fecha_creacion.strftime('%d/%m/%Y')} - {self.fecha_limite.strftime('%d/%m/%Y')} - {self.estado}"

    def cambiar_estado(self, estado):
        self.estado = estado

# 🔹 FUNCIONES PARA MANEJAR LISTA DE TAREAS 🔹

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_creacion = datetime.datetime.now()
    fecha_limite = input("Ingrese la fecha límite de la tarea (dd/mm/aaaa): ")
    return Tarea(titulo, descripcion, fecha_creacion, fecha_limite)

def listar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas registradas.")
        return

    table = prettytable.PrettyTable()
    table.field_names = ["Título", "Descripción", "Fecha de Creación", "Fecha Límite", "Estado"]
    for tarea in tareas:
        table.add_row([
            tarea.titulo,
            tarea.descripcion,
            tarea.fecha_creacion.strftime("%d/%m/%Y"),
            tarea.fecha_limite.strftime("%d/%m/%Y"),
            tarea.estado
        ])
    print(table)

def completar_tarea(tareas):
    titulo = input("Ingrese el título de la tarea a completar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tarea.cambiar_estado("Completada")
            print("✅ Tarea completada.")
            return
    print("❌ Tarea no encontrada.")

def eliminar_tarea(tareas):
    titulo = input("Ingrese el título de la tarea a eliminar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower() == titulo:
            tareas.remove(tarea)
            print("🗑️ Tarea eliminada.")
            return
    print("❌ Tarea no encontrada.")
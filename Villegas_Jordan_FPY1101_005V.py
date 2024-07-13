import random
import csv
import math


trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]

def asignar_sueldos(trabajadores):
    for trabajador in trabajadores:
        trabajador["sueldo"] = random.randint(300000, 2500000)
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos(trabajadores):
    bajos = []
    medios = []
    altos = []
    for trabajador in trabajadores:
        sueldo = trabajador["sueldo"]
        if sueldo < 800000:
            bajos.append(trabajador)
        elif sueldo <= 2000000:
            medios.append(trabajador)
        else:
            altos.append(trabajador)
    
    print("\nSueldos menores a $800.000:")
    for trabajador in bajos:
        print(f"{trabajador['nombre']} - ${trabajador['sueldo']}")
    
    print("\nSueldos entre $800.000 y $2.000.000:")
    for trabajador in medios:
        print(f"{trabajador['nombre']} - ${trabajador['sueldo']}")
    
    print("\nSueldos superiores a $2.000.000:")
    for trabajador in altos:
        print(f"{trabajador['nombre']} - ${trabajador['sueldo']}")
        
def ver_estadisticas(trabajadores):
    sueldos = [trabajador["sueldo"] for trabajador in trabajadores]
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geo = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
    
    print(f"\nSueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")
    print(f"Media geométrica de sueldos: ${sueldo_geo:.2f}")

def generar_reporte(trabajadores):
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for trabajador in trabajadores:
            sueldo_base = trabajador["sueldo"]
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            writer.writerow([trabajador["nombre"], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
    
    print("\nReporte de sueldos generado: reporte_sueldos.csv")

def menu():
    while True:
        print("\nMenu de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            asignar_sueldos(trabajadores)
        elif opcion == "2":
            clasificar_sueldos(trabajadores)
        elif opcion == "3":
            ver_estadisticas(trabajadores)
        elif opcion == "4":
            generar_reporte(trabajadores)
        elif opcion == "5":
            print("Finalizando programa...")
            print("Desarrollado por Jordán Villegas.")
            print("RUT 19.507.472-0")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()

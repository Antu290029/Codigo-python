# Nombre del curso
nombre_curso = input("Nombre del Curso: ")

# Cantidad de alumnos inscritos
cantidad_alumnos = 0

while cantidad_alumnos <= 0:
    cantidad_alumnos_str = input("Cantidad de Alumnos inscritos: ")

    if cantidad_alumnos_str.isdigit():
        cantidad_alumnos = int(cantidad_alumnos_str)

        if cantidad_alumnos <= 0:
            print("La cantidad de alumnos debe ser mayor que 0.")
    else:
        print("Por favor, ingresa un número entero válido para la cantidad de alumnos.")

alumnos = []

# Nombre de cada alumno
for i in range(cantidad_alumnos):
    nombre_alumno = input(f"Nombre del Alumno {i + 1}: ").capitalize()
    alumnos.append({"nombre": nombre_alumno, "notas": [], "asistencia": 0, "examen": 0})

# Cantidad de evaluaciones
cantidad_evaluaciones = 0

while cantidad_evaluaciones <= 0:
    cantidad_evaluaciones_str = input("Cantidad de evaluaciones: ")

    if cantidad_evaluaciones_str.isdigit():
        cantidad_evaluaciones = int(cantidad_evaluaciones_str)

        if cantidad_evaluaciones <= 0:
            print("La cantidad de evaluaciones debe ser mayor que 0.")
    else:
        print("Por favor, ingresa un número entero válido para la cantidad de evaluaciones.")

# Ponderacion de evaluaciones
ponderacion_evaluaciones = []

# Ingresar ponderaciones de evaluaciones
while sum(ponderacion_evaluaciones) != 100:
    ponderacion_evaluaciones = []
    for i in range(cantidad_evaluaciones):
        ponderacion = 0
        while ponderacion <= 0:
            ponderacion_str = input(f"Ponderación de Evaluación {i + 1}: ")
            if ponderacion_str.replace('.', '', 1).isdigit():
                ponderacion = float(ponderacion_str)
                if ponderacion <= 0:
                    print("La ponderación debe ser mayor que 0.")
            else:
                print("Por favor, ingresa un número válido para la ponderación.")
        ponderacion_evaluaciones.append(ponderacion)

# Tiene examen y ponderación del examen
tiene_examen = input("¿Tiene examen? (S/N): ")
ponderacion_examen = 0

if tiene_examen.lower() == "s":
    ponderacion_examen_str = input("Ponderación del Examen: ")
    if ponderacion_examen_str.replace('.', '', 1).isdigit():
        ponderacion_examen = float(ponderacion_examen_str)
    else:
        print("Por favor, ingresa un número válido para la ponderación del examen.")

# Asignatura es teórica o práctica
asignatura_tipo = input("Asignatura Teórica o Práctica (T/P): ").lower()
asistencia_minima = 80 if asignatura_tipo == "p" else 60


# Función para calcular la nota final de un estudiante
def calcular_nota_final(notas, nota_examen):
    nota_final = sum(notas) / len(notas)
    if ponderacion_examen > 0:
        nota_final = (nota_final * sum(ponderacion_evaluaciones) + nota_examen * ponderacion_examen) / (
                sum(ponderacion_evaluaciones) + ponderacion_examen)
    return nota_final


# Validar nota en el rango de 1.0 a 7.0 con un decimal
def validar_nota(nota):
    return 1.0 <= nota <= 7.0 and round(nota, 1) == nota


# Menú permanente
while True:
    print("\n=== Menú ===")
    print("1. Ingreso de Evaluación")
    print("2. Ingreso Asistencia")
    print("3. Consultar Condición Estudiante")
    print("4. Calcular Promedio General")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Ingreso de Evaluación
        for idx, alumno in enumerate(alumnos, 1):
            print(f"Alumno {idx}: {alumno['nombre']}")

        estudiante_idx = 0
        estudiante_idx_str = input(f"Ingrese el número del Estudiante (1-{cantidad_alumnos}): ")

        while not estudiante_idx_str.isdigit() or not (1 <= int(estudiante_idx_str) <= cantidad_alumnos):
            print("Número de estudiante no válido.")
            estudiante_idx_str = input(f"Ingrese el número del Estudiante (1-{cantidad_alumnos}): ")

        estudiante_idx = int(estudiante_idx_str)
        estudiante = alumnos[estudiante_idx - 1]

        estudiante["notas"] = []
        for i in range(cantidad_evaluaciones):
            nota_evaluacion = 0

            nota_evaluacion_str = input(f"Ingrese la nota de la Evaluación {i + 1}: ")
            while not nota_evaluacion_str.replace('.', '', 1).isdigit() or not (1.0 <= float(nota_evaluacion_str) <= 7.0):
                print("La nota debe estar en el rango de 1.0 a 7.0 con máximo un decimal.")
                nota_evaluacion_str = input(f"Ingrese la nota de la Evaluación {i + 1}: ")

            nota_evaluacion = float(nota_evaluacion_str)
            estudiante["notas"].append(nota_evaluacion)

        if tiene_examen.lower() == "s":
            estudiante["examen"] = 0
            nota_examen_str = input("Ingrese la nota del Examen: ")
            while not nota_examen_str.replace('.', '', 1).isdigit() or not (1.0 <= float(nota_examen_str) <= 7.0):
                print("La nota del examen debe estar en el rango de 1.0 a 7.0 con máximo un decimal.")
                nota_examen_str = input("Ingrese la nota del Examen: ")

            estudiante["examen"] = float(nota_examen_str)

        print("Notas ingresadas exitosamente.")

    elif opcion == "2":
        # Ingreso de Asistencia
        for idx, alumno in enumerate(alumnos, 1):
            print(f"Alumno {idx}: {alumno['nombre']}")

        estudiante_idx = 0
        estudiante_idx_str = input(f"Ingrese el número del Estudiante (1-{cantidad_alumnos}) para ingresar asistencia: ")

        while not estudiante_idx_str.isdigit() or not (1 <= int(estudiante_idx_str) <= cantidad_alumnos):
            print("Número de estudiante no válido.")
            estudiante_idx_str = input(f"Ingrese el número del Estudiante (1-{cantidad_alumnos}) para ingresar asistencia: ")

        estudiante_idx = int(estudiante_idx_str)
        estudiante = alumnos[estudiante_idx - 1]

        estudiante["asistencia"] = -1
        while estudiante["asistencia"] < 0 or estudiante["asistencia"] > 100:
            asistencia_str = input(f"Ingrese el porcentaje de asistencia (0-100) para {estudiante['nombre']}: ")
            if asistencia_str.replace('.', '', 1).isdigit():
                estudiante["asistencia"] = float(asistencia_str)
                if estudiante["asistencia"] < 0 or estudiante["asistencia"] > 100:
                    print("La asistencia debe estar en el rango de 0 a 100.")
            else:
                print("Por favor, ingresa un número válido para la asistencia.")

        print("Asistencia ingresada exitosamente.")

    elif opcion == "3":
        for idx, alumno in enumerate(alumnos, 1):
            print(f"Alumno {idx}: {alumno['nombre']}")

        estudiante_idx = 0
        estudiante_idx_str = input(f"Ingrese el número del Estudiante (1-{cantidad_alumnos}) para consultar su condición: ")

        while not estudiante_idx_str.isdigit() or not (1 <= int(estudiante_idx_str) <= cantidad_alumnos):
            print("Número de estudiante no válido.")
            estudiante_idx_str = input(f"Ingrese el número del Estudiante (1-{cantidad_alumnos}) para consultar su condición: ")

        estudiante_idx = int(estudiante_idx_str)
        estudiante = alumnos[estudiante_idx - 1]
        nota_examen = estudiante["examen"]

        if all(estudiante["notas"]) and estudiante["asistencia"]:
            nota_final = calcular_nota_final(estudiante["notas"], nota_examen)
            condicion = "APROBADO" if nota_final >= 4 and estudiante['asistencia'] >= asistencia_minima else "REPROBADO"
            print(f"Nombre del Estudiante: {estudiante['nombre']}")
            print(f"Condición: {condicion}")
            print(f"Nota Final: {nota_final:.2f}")
            print(f"Asistencia: {estudiante['asistencia']}%")
        else:
            print(f"Nombre del Estudiante: {estudiante['nombre']}")
            print("Condición: PENDIENTE (No se han ingresado notas o asistencia)")

    elif opcion == "4":
        if cantidad_alumnos > 0 and all(
                all(estudiante["notas"]) and estudiante["asistencia"] >= asistencia_minima for estudiante in alumnos):
            promedio_general = sum(calcular_nota_final(estudiante["notas"], estudiante["examen"]) for estudiante in
                                   alumnos) / cantidad_alumnos
            print(f"Promedio General del Curso: {promedio_general:.2f}")
        else:
            print("Falta información para calcular el Promedio General del curso.")

    elif opcion == "5":
        break

    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")

print("¡Hasta luego!")
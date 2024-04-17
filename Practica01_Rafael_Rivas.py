contador = 0

while contador < 5:
    #Creamos los usuarios
    nombre_empleado = input("Ingrese Nombre completo del empleado :")
    dni_empleado = input("Ingrese el DNI del empleado :")
    telefono_empleado = input("Ingrese el telefono del empleado :")
    antiguedad_empleado = input("Ingrese el tiempo que lleva trabajandoel empleado (meses):")
    cargo_empleado = input("Ingrese el cargo del empleado: ")
    respuesta = input("Desea continuar : Si/No")
    if respuesta == "Si":
        print("Si")
        contador = contador + 1
    else:
        print("No")
        contador = 6




#Asignamos los sueldos del personal
sueldo_limpieza = 1025
sueldo_mesero = 1500
sueldo_cajero = 1500
sueldo_vigilante = 1400
sueldo_gerente = 2500

diccionario1 = {"Nombre Completo " : nombre_empleado,
                "DNI ": dni_empleado,
                "Telefono ": telefono_empleado,
                "Tiempo trabajando (meses)": antiguedad_empleado,
                "Cargo ": cargo_empleado}



print("====================== Gestion de Empleados ========================")
print("|| 1. Visualizar informacion de un empleado.                      ||")
print("|| 2. Mostrar empleado cuyo tiempo en la empresa sea el menor     ||")
print("|| 3. Actualizar salario de un empleado                           ||")
print("|| 4. Terminar programa                                           ||")
print("====================================================================")

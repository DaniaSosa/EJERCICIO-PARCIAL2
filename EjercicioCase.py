name= []
lastName= []
age= []
birthday= []
email= []
password= []
confirmPass= []
opcion= 0

while True:
    print("Bienvenido al sistema de registro")
    print("---------MENÚ PRINCIPAL---------")
    print("1. Registrar usuario")
    print("2. Ver la información del usuario")
    print("3. Borrar la información del usuario")
    print("4. Modificar la información del usuario")
    print("5. Salir")
    print("---------------------------------")
opcion= int(input("Seleccioneuna opción: "))
match opcion:
    case 1:
        name.append(input("Ingresa tu nombre: "))
        lastName.append(input("Ingresa tu apellido: "))
        age.append(int(input("Ingresa tu edad: ")))
        birthday.append(input("Ingresa tu fecha de nacimiento: "))
        email.append(input("Ingresa tu correo electrónico: "))
        password.append(input("Ingresa tu contraseña: "))
        confirmPass.append(input("Confirma tu contraseña: "))
        print ("Usuario registrado exitosamente, con el ID. " + str(len(name)-1))
    case 2:
        print("Nombre:", name, "Edad:", age, "Fecha de nacimiento:", birthday, "Correo electrónico:", email)
    case 3:
        name= ""
        lastName= ""
        age= 0
        birthday= ""
        email= ""
        password= ""
    case 4:
        name.append(input("Ingresa tu nuevo nombre: "))
        lastNam.append(input("Ingresa tu nuevo apellido: "))
        age.appen(int(input("Ingresa tunueva edad: ")))
        birthday.append(input("Ingresa tu nueva fecha de nacimiento (dd/mm/aaaa): "))
        password.append(input("Ingresa tu nueva contraseña: "))
    case 5:
         print("!Hasta luego!")
        break
    case _:
         print("opción no válida")
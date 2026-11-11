name= ""
lastName= ""
age= 0
birthday= ""
email= ""
password= ""
confirmPass= ""
opcion= 0

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
        name= input("Ingresa tu nombre: ")
        lastName= input("Ingresa tu apellido: ")
        age= int(input("Ingresa tu edad: "))
        birthday= input("Ingresa tu fecha de nacimiento: ")
        email= input("Ingresa tu correo electrónico: ")
        password= input("Ingresa tu contraseña: ")
        confirmPass= input("Confirma tu contraseña: ")
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
        name= input("Ingresa tu nuevo nombre: ")
        lastName= input("Ingresa tu nuevo apellido: ")
        age= int(input("Ingresa tunueva edad: "))
        birthday= input("Ingresa tu nueva fecha de nacimiento (dd/mm/aaaa): ")
        email= input("Ingresa tu nuevo correo electrónico: ")
        password= input("Ingresa tu nueva contraseña: ")
        case 5:
         print("!Hasta luego!")
        
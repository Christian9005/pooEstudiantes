import mysql.connector
import re
def conectar_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ckrisfoxx;13A#",
        database="dbproject"
    )
    return mydb

def Validacion_Nota(n_nota):
    while True:
        nota = int(input(f"Ingrese la nota {n_nota}: "))
        if nota < 0 or nota > 100:
            print("Ingresar la nota en el rango (0-100)")
            continue
        else:
            return nota

def validar_usuario(nombre):
    estado_valido = True
    conectar = conectar_db()
    base_datos = conectar.cursor()
    base_datos.execute("SELECT nombre FROM usuarios")
    usuarios = base_datos.fetchall()
    for usuario in usuarios:
        if usuario[0] == nombre:
            estado_valido = False
            return estado_valido
    return estado_valido

def validar_estudiante(cedula):
    estado_valido = True
    conectar = conectar_db()
    base_datos = conectar.cursor()
    base_datos.execute("SELECT cedula FROM estudiantes")
    estudiantes = base_datos.fetchall()
    for estudiante in estudiantes:
        if estudiante[0] == cedula:
            estado_valido = False
            return estado_valido
    return estado_valido

def validar_respuesta():
    while True:
        n = input("Confirme los datos a guardar (S/N): ")
        if n.upper() == "S":
            return n
        elif n.upper() == "N":
            return n
        else:
            continue

def validar_correo():
    while True:
        correo = input("Correo: ")
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
            return correo
        else:
            continue
class Usuario:
    def __init__(self, nombre, clave = ""):
        self.nombre = nombre
        self.clave = clave

    def crear_usuario(self):
        conectar = conectar_db()
        base_datos = conectar.cursor()
        usuario_valido = validar_usuario(self.nombre)
        if usuario_valido:
            sql = "INSERT INTO usuarios (nombre, contrasena) VALUES (%s, %s)"
            val = (self.nombre, self.clave)
            base_datos.execute(sql, val)
            conectar.commit()
            print(f"Usuario {self.nombre} creado exitosamente")
        else:
            print("Error Usuario duplicado")

    def listar_usuarios(self):
        conectar = conectar_db()
        base_datos = conectar.cursor()
        base_datos.execute("SELECT * FROM usuarios")
        usuarios = base_datos.fetchall()
        print("Id     Usuario     Contraseña")
        for usuario in usuarios:
            print(f"{usuario[0]}      {usuario[1]}       {usuario[2]}")
    def buscar_usuario(self):
        usuario_valido = validar_usuario(self.nombre)
        if not usuario_valido:
            print("Usuario Encontrado")
            conectar = conectar_db()
            base_datos = conectar.cursor()
            nombre_usuario = (f"{self.nombre}",)
            sql = "SELECT * FROM usuarios WHERE nombre= %s"
            base_datos.execute(sql, nombre_usuario)
            nombres_usuarios = base_datos.fetchall()
            for usuario in nombres_usuarios:
                print("Id       Nombre      Clave")
                print(f"{usuario[0]}        {usuario[1]}       {usuario[2]}")
        else:
            print("Usuario no registrado!!!")

    def modificar_usuario(self):
        usuario_valido = validar_usuario(self.nombre)
        if not usuario_valido:
            print("Usuario Encontrado")
            print("Ingrese el nombre a modificar")
            nombre_actualizado = input("Usuario: ")
            clave_actualizada = input("Clave: ")
            confirmacion = input("Confirme la actualizacion del usuario (S/N): ")
            if confirmacion.upper() == "S":
                conectar = conectar_db()
                base_datos = conectar.cursor()
                usuario_actualizado = (f"{nombre_actualizado}", f"{clave_actualizada}", f"{self.nombre}")
                sql = "UPDATE usuarios set nombre= %s, contrasena= %s WHERE nombre= %s"
                base_datos.execute(sql, usuario_actualizado)
                conectar.commit()
                print("Usuario modificado exitosamente")
            elif confirmacion.upper() == "N":
                print("Usuario no modificado")
            else:
                print("Opcion no valida")
        else:
            print("Usuario no registrado!!!")

    def borrar_usuario(self):
        usuario_valido = validar_usuario(self.nombre)
        if not usuario_valido:
            print("Usuario Encontrado")
            confirmacion = input("Confirme la eliminacion del usuario (S/N): ")
            if confirmacion.upper() == "S":
                conectar = conectar_db()
                base_datos = conectar.cursor()
                nombre_usuario = (f"{self.nombre}",)
                sql = "DELETE FROM usuarios WHERE nombre= %s"
                base_datos.execute(sql, nombre_usuario)
                conectar.commit()
                print("Usuario eliminado exitosamente")
            elif confirmacion.upper() == "N":
                print("Usuario no eliminado")
            else:
                print("Opcion no valida")
        else:
            print("Usuario no registrado!!!")


class Estudiante:
    def __init__(self, cedula, nombre = "", apellido = "", correo = "", celular = ""):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.celular = celular
    
    def crear_estudiante(self):
        conectar = conectar_db()
        base_datos = conectar.cursor()
        estudiante_valido = validar_estudiante(self.cedula)
        if estudiante_valido:
            sql = "INSERT INTO estudiantes (cedula, nombre, apellido, correo, celular) VALUES (%s, %s, %s, %s, %s)"
            val = (self.cedula, self.nombre, self.apellido, self.correo, self.celular)
            base_datos.execute(sql, val)
            conectar.commit()
            print(f"El Estudiante: {self.nombre} con CI: {self.cedula} creado exitosamente")
        else:
            print("Error Estudiante duplicado")

    def buscar_estudiante(self):
        estudiante_valido = validar_estudiante(self.cedula)
        if not estudiante_valido:
            print("Estudiante Encontrado")
            conectar = conectar_db()
            base_datos = conectar.cursor()
            cedula_estudiante = (f"{self.cedula}",)
            sql = "SELECT * FROM estudiantes WHERE cedula= %s"
            base_datos.execute(sql, cedula_estudiante)
            estudiantes = base_datos.fetchall()
            for estudiante in estudiantes:
                print("Id     Cedula   Nombre   Apellido  Correo      Celular")
                print(f"{estudiante[0]}      {estudiante[1]}       {estudiante[2]}     {estudiante[3]}     {estudiante[4]}     {estudiante[5]}")
        else:
            print("Estudiante no registrado!!!")

    def modificar_estudiante(self):
        estudiante_valido = validar_estudiante(self.cedula)
        if not estudiante_valido:
            print("Estudiante Encontrado")
            print("Ingrese las credenciales del estudiante a modificar")
            cedula = input("Cedula: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            celular = input("Celular: ")
            confirmacion = input("Confirme la actualizacion del estudiante (S/N): ")
            if confirmacion.upper() == "S":
                conectar = conectar_db()
                base_datos = conectar.cursor()
                estudiante_modificado = (f"{cedula}", f"{nombre}", f"{apellido}", f"{correo}", f"{celular}", f"{self.cedula}")
                sql = "UPDATE estudiantes set cedula= %s, nombre= %s, apellido= %s, correo= %s, celular= %s WHERE cedula= %s"
                base_datos.execute(sql, estudiante_modificado)
                conectar.commit()
                print("Estudiante modificado exitosamente")
            elif confirmacion.upper() == "N":
                print("Estudiante no modificado")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")

    def eliminar_estudiante(self):
        estudiante_valido = validar_estudiante(self.cedula)
        if not estudiante_valido:
            print("Estudiante Encontrado")
            confirmacion = input("Confirme la eliminacion del estudiante (S/N): ")
            if confirmacion.upper() == "S":
                conectar = conectar_db()
                base_datos = conectar.cursor()
                cedula = (f"{self.cedula}",)
                sql = "DELETE FROM estudiantes WHERE cedula= %s"
                base_datos.execute(sql, cedula)
                conectar.commit()
                print("Usuario eliminado exitosamente")
            elif confirmacion.upper() == "N":
                print("Estudiante no eliminado")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")


class Calificaciones(Estudiante):
    def __init__(self, cedula, nombre="", apellido="", correo="", celular="", promedio=0):
        super().__init__(cedula, nombre, apellido, correo, celular)
        self.promedio = promedio

    def Entrada_Notas_Promedio(self):
        nota1 = Validacion_Nota(1)
        nota2 = Validacion_Nota(1)
        nota3 = Validacion_Nota(1)
        nota4 = Validacion_Nota(1)

        self.promedio = (nota1 + nota2 + nota3 + nota4) / 4

    def registrar_notas(self):
        conectar = conectar_db()
        base_datos = conectar.cursor()
        estudiante_valido = validar_estudiante(self.cedula)
        if estudiante_valido:
            sql = "INSERT INTO calificaciones (cedula, nombre, apellido, correo, celular, promedio) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (self.cedula, self.nombre, self.apellido, self.correo, self.celular, self.promedio)
            base_datos.execute(sql, val)
            conectar.commit()
            print(f"Notas del Estudiante con CI: {self.cedula} creadas exitosamente")
        else:
            print("Error Estudiante duplicado")

    def listar_notas(self):
        print("Notas de los Estudiantes")
        conectar = conectar_db()
        base_datos = conectar.cursor()
        sql = "SELECT * FROM calificaciones"
        base_datos.execute(sql)
        notas_estudiantes = base_datos.fetchall()
        for nota in notas_estudiantes:
            print("Id     Cedula     Promedio")
            print(f"{nota[0]}      {nota[1]}       {nota[6]}")

    def buscar_notas_estudiante(self):
        estudiante_valido = validar_estudiante(self.cedula)
        if not estudiante_valido:
            print("Estudiante Encontrado")
            conectar = conectar_db()
            base_datos = conectar.cursor()
            cedula_estudiante = (f"{self.cedula}",)
            sql = "SELECT * FROM calificaciones WHERE cedula= %s"
            base_datos.execute(sql, cedula_estudiante)
            nota_estudiante = base_datos.fetchall()
            for nota in nota_estudiante:
                print("Id     Cedula     Promedio")
                print(f"{nota[0]}      {nota[1]}       {nota[6]}")
        else:
            print("Estudiante no registrado!!!")

    def modificar_notas(self):
        estudiante_valido = validar_estudiante(self.cedula)
        if not estudiante_valido:
            print("Estudiante Encontrado")
            print("Ingrese las notas del estudiante a modificar")
            nota1 = Validacion_Nota(1)
            nota2 = Validacion_Nota(2)
            nota3 = Validacion_Nota(3)
            nota4 = Validacion_Nota(4)
            print(f"Notas {nota1}, {nota2}, {nota3}, {nota4}")
            confirmation = input(f"Confirme las notas ingresado. (S/N): ")
            if confirmation.upper() == "S":
                self.promedio = (nota1 + nota2 + nota3 + nota4) // 4
                conectar = conectar_db()
                base_datos = conectar.cursor()
                estudiante_modificado = (f"{self.cedula}", f"{self.promedio}", f"{self.cedula}")
                sql = "UPDATE calificaciones set cedula= %s, promedio= %s WHERE cedula= %s"
                base_datos.execute(sql, estudiante_modificado)
                conectar.commit()
                print("Notas del estudiante modificadas exitosamente")
            elif confirmation.upper() == "N":
                print("Notas del estudiante no modificadas")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")

    def eliminar_notas(self):
        estudiante_valido = validar_estudiante(self.cedula)
        if not estudiante_valido:
            print("Estudiante Encontrado")
            confirmacion = input("Confirme la eliminacion de las notas del estudiante (S/N): ")
            if confirmacion.upper() == "S":
                conectar = conectar_db()
                base_datos = conectar.cursor()
                cedula = (f"{self.cedula}",)
                sql = "DELETE FROM calificaciones WHERE cedula= %s"
                base_datos.execute(sql, cedula)
                conectar.commit()
                print("Notas eliminadas exitosamente")
            elif confirmacion.upper() == "N":
                print("Notas no eliminadas")
            else:
                print("Opcion no valida")
        else:
            print("Estudiante no registrado!!!")

def Ingresar(nombre, clave):
    indice = None
    indice_db = 0
    usuario_valido = False
    conectar = conectar_db()
    base_datos = conectar.cursor()
    base_datos.execute("SELECT nombre FROM usuarios")
    usuarios = base_datos.fetchall()

    for usuario in usuarios:
        if usuario[0] == nombre:
            usuario_valido = True
            break

    if usuario_valido:
        for usuario in usuarios:
            if usuario[0] == nombre:
                indice = usuarios[indice_db].index(nombre)
                break
            indice_db += 1

        base_datos.execute("SELECT contrasena FROM usuarios")
        passwords_users = base_datos.fetchall()

        if passwords_users[indice_db][indice] == clave:
            print(f"\nIngreso exitoso, {nombre}")
            return True
        else:
            print("\nContraseña incorrecta")
            return False

    else:
        print("Usuario no encontrado")
        print("Vuelva a intentar")
        return False
def Programa_Principal():
    while True:
        print("\n-----Bienvenido-----")
        print("Para acceder al menu debe ingresar sesion")
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")
        validacion_ingreso = Ingresar(usuario, clave)

        if validacion_ingreso:
            while (True):
                print("\n-----Menu-----")
                print("1. Usuarios")
                print("2. Estudiantes")
                print("3. Calificaciones")
                print("4. Cerrar Sesión")
                print("5. Salir del programa")
                opcion = input("Opcion: ")

                if opcion == "1":
                    while (True):
                        print("\n---Usuarios---")
                        print("1. Ingresar usuario")
                        print("2. Listar usuarios")
                        print("3. Consultar un usuario")
                        print("4. Modificar usuario")
                        print("5. Eliminar usuario")
                        print("6. Salir al Menu Principal")
                        opcion_usuario = input("Opcion: ")

                        if opcion_usuario == "1":
                            while (True):
                                print("\nIngresando nuevo usuario")
                                usuario = input("Usuario: ")
                                clave = input("Contraseña: ")
                                confirmacion = validar_respuesta()

                                if confirmacion.upper() == "S":
                                    usuario_obj = Usuario(usuario, clave)
                                    usuario_obj.crear_usuario()
                                    validacion = input("\nDesea seguir registrando usuarios (S/N): ")
                                    if validacion.upper() == "N":
                                        break
                                    elif validacion.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                elif confirmacion.upper() == "N":
                                    print("Usuario no registrado")
                                    validacion = input("\nDesea seguir registrando usuarios (S/N): ")
                                    if validacion.upper() == "N":
                                        break
                                    elif validacion.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                else:
                                    print("Opcion invalida!!")

                        elif opcion_usuario == "2":
                            usuario_obj = Usuario("", "")
                            usuario_obj.listar_usuarios()


                        elif opcion_usuario == "3":
                            while (True):
                                print("\nConsulta")
                                usuario = input("Ingrese el usuario a consultar: ")
                                usuario_obj = Usuario(usuario)
                                usuario_obj.buscar_usuario()
                                validacion = input("\nDesea seguir consultado usuarios (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a consultar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "4":
                            while (True):
                                print("\nModificar usuario")
                                usuario = input("Ingrese el usuario a modificar: ")
                                usuario_obj = Usuario(usuario)
                                usuario_obj.modificar_usuario()
                                validacion = input("\nDesea seguir modificando usuarios (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a modificar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "5":
                            while (True):
                                print("\nEliminacion de usuario")
                                usuario = input("Ingrese el usuario a eliminar: ")
                                usuario_obj = Usuario(usuario)
                                usuario_obj.borrar_usuario()
                                validacion = input("\nDesea seguir eliminado usuarios (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a eliminar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "6":
                            break

                elif opcion == "2":
                    while (True):
                        print("\n---Estudiantes---")
                        print("1. Ingresar estudiante")
                        print("2. Consultar un estudiante")
                        print("3. Modificar estudiante")
                        print("4. Eliminar estudiante")
                        print("5. Salir al Menu Principal")
                        opcion_usuario = input("Opcion: ")

                        if opcion_usuario == "1":
                            while (True):
                                print("\nIngresando nuevo estudiante")
                                cedula = input("Cedula: ")
                                nombre = input("Nombre: ")
                                apellido = input("Apellido: ")
                                correo = validar_correo()
                                celular = input("Celular: ")
                                confirmacion = validar_respuesta()

                                if confirmacion.upper() == "S":
                                    student_dto = Estudiante(cedula, nombre, apellido, correo, celular)
                                    student_dto.crear_estudiante()
                                    validacion = input("\nDesea seguir registrando estudiantes (S/N): ")
                                    if validacion.upper() == "N":
                                        break
                                    elif validacion.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                elif confirmacion.upper() == "N":
                                    print("Estudiante no registrado")
                                    validacion = input("\nDesea seguir registrando estudiantes (S/N): ")
                                    if validacion.upper() == "N":
                                        break
                                    elif validacion.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                else:
                                    print("Opcion invalida!!")

                        elif opcion_usuario == "2":
                            while (True):
                                print("\nConsulta")
                                cedula = input("Ingrese la cedula del estudiante a consultar: ")
                                student_dto = Estudiante(cedula)
                                student_dto.buscar_estudiante()
                                validacion = input("\nDesea seguir consultado estudiantes (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a consultar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "3":
                            while (True):
                                print("\nModificar Estudiante")
                                cedula = input("Ingrese la cedula del estudiante a modificar: ")
                                student_dto = Estudiante(cedula)
                                student_dto.modificar_estudiante()
                                validacion = input("\nDesea seguir modificando estudiantes (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a modificar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "4":
                            while (True):
                                print("\nEliminacion de Estudiante")
                                cedula = input("Ingrese la cedula del estudiante a eliminar: ")
                                student_dto = Estudiante(cedula)
                                student_dto.eliminar_estudiante()
                                validacion = input("\nDesea seguir eliminado estudiantes (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a eliminar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "5":
                            break

                elif opcion == "3":
                    while (True):
                        print("\n---Calificaciones---")
                        print("1. Ingresar calificaciones estudiante")
                        print("2. Listar todas las calificaciones de los estudiantes")
                        print("3. Consultar notas de un estudiante")
                        print("4. Modificar notas de un estudiante")
                        print("5. Eliminar notas de un estudiante")
                        print("6. Salir al Menu Principal")
                        opcion_usuario = input("Opcion: ")

                        if opcion_usuario == "1":
                            while (True):
                                cedula = input("\nIngrese cedula del estudiante: ")
                                print("\nIngresando notas de un estudiante")
                                nota1 = Validacion_Nota(1)
                                nota2 = Validacion_Nota(1)
                                nota3 = Validacion_Nota(1)
                                nota4 = Validacion_Nota(1)
                                print(f"Notas {nota1}, {nota2}, {nota3}, {nota4}")
                                confirmacion = input(f"Confirme las notas ingresado. (S/N): ")
                                if confirmacion.upper() == "S":
                                    promedio = (nota1 + nota2 + nota3 + nota4) // 4
                                    notas_poo = Calificaciones(cedula, "", "", "", "", promedio)
                                    notas_poo.registrar_notas()
                                    validacion = input("\nDesea seguir registrando notas de estudiantes (S/N): ")
                                    if validacion.upper() == "N":
                                        break
                                    elif validacion.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                elif confirmacion.upper() == "N":
                                    print("Notas no registradas")
                                    validacion = input("\nDesea seguir registrando estudiantes (S/N): ")
                                    if validacion.upper() == "N":
                                        break
                                    elif validacion.upper() == "S":
                                        print("Vuela a registrar")
                                    else:
                                        print("Opcion invalida")

                                else:
                                    print("Opcion invalida!!")

                        elif opcion_usuario == "2":
                            notas_poo = Calificaciones("")
                            notas_poo.listar_notas()

                        elif opcion_usuario == "3":
                            while (True):
                                print("\nConsulta")
                                cedula = input("Ingrese la cedula del estudiante a consultar: ")
                                notas_poo = Calificaciones(cedula)
                                notas_poo.buscar_notas_estudiante()
                                validacion = input("\nDesea seguir consultado notas de estudiantes (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a consultar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "4":
                            while (True):
                                print("\nModificar notas del estudiante")
                                cedula = input("Ingrese la cedula del estudiante a modificar: ")
                                notas_poo = Calificaciones(cedula)
                                notas_poo.modificar_notas()
                                validacion = input("\nDesea seguir modificando notas de estudiantes (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a modificar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "5":
                            while (True):
                                print("\nEliminacion de notas del estudiante")
                                cedula = input("Ingrese la cedula del estudiante a eliminar: ")
                                notas_poo = Calificaciones(cedula)
                                notas_poo.eliminar_notas()
                                validacion = input("\nDesea seguir eliminado notas de estudiantes (S/N): ")
                                if validacion.upper() == "N":
                                    break
                                elif validacion.upper() == "S":
                                    print("\nVuela a eliminar")
                                else:
                                    print("Opcion invalida")

                        elif opcion_usuario == "6":
                            break

                elif opcion == "4":
                    print("Cerrando Sesión")
                    break
                elif opcion == "5":
                    print("Saliendo...")
                    exit(0)
                else:
                    print(f"Error opcion invalida {opcion}")
                    print("Ingrese una opcion valida!!!")

if __name__ == '__main__':
    Programa_Principal()

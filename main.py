import mysql.connector

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

def conectar_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", #clave colocada al instalar mysql
        database="dbproject"
    )
    return mydb



class Usuario:
    def __init__(self, nombre, clave):
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
    def __init__(self, cedula, nombre, apellido, correo, celular):
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
    def __init__(self, cedula, nombre, apellido, correo, celular, promedio=0):
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

    def Delete_Student_Scores(self):
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



if __name__ == '__main__':
    pass



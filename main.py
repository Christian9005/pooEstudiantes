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





if __name__ == '__main__':
    pass


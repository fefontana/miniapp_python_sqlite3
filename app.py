from os import system
import time
import conexion as conn
db = conn.DB()
system("clear")
def create():
    name = str(input("Ingrese nombre: "))
    email = str(input("Ingrese email: "))
    if(len(name) > 0 and len(email) > 0):
        sql = "INSERT INTO personas(name,email) VALUES(?,?)"
        parametros = (name,email)
        db.ejecutar_consulta(sql,parametros)
        print(conn.sqlite3_log())
        print("Insertado ok")
def read():
    sql = "SELECT * FROM personas"
    result = db.ejecutar_consulta(sql)
    for data in result:
        print(""" 
        ID :        {}
        NOMBRE :    {}
        EMAIL :     {}
        """.format(data[0],data[1],data[2]))
def update():
    id = int(input("Ingrese Id: "))
    if(id != 0):
        name = str(input("Ingrese nombre: "))
        email = str(input("Ingrese email: "))
        if(len(name) > 0 and len(email) > 0):
            sql = "UPDATE personas SET name=?,email=? WHERE id=?"
            parametros = (name,email,id)
            db.ejecutar_consulta(sql,parametros)
            print("Actualizado ok!")
    else:
        print("Es requerido el Id")
def delete():
    id = int(input("Ingrese Id: "))
    if(id != 0):
        sql = "DELETE FROM personas WHERE id=?"
        parametros = (id,)
        db.ejecutar_consulta(sql,parametros)
        print("Eliminado ok!")
    else:
        print("Es requerido el Id")
def search():
    nombre = str(input("Buscar por nombre: "))
    if(len(nombre) > 0):
        sql = "SELECT * FROM personas WHERE name LIKE ?"
        parametros = ('%{}%'.format(nombre),)
        result = db.ejecutar_consulta(sql,parametros)
        for data in result:
            print(""" 
            +ID :        {}
            +NOMBRE :    {}
            +EMAIL :     {}""".format(data[0],data[1],data[2]))
while True:
    print("=========================================")
    print("\tSistema de Administracion de Usuarios")
    print("=========================================")
    print("\t[1] Insertar persona")
    print("\t[2] Listar personas")
    print("\t[3] Actualizar persona")
    print("\t[4] Eliminar persona")
    print("\t[5] Buscar persona")
    print("\t[6] Salir")
    print("=========================================")

    try:
        opcion = int(input("Elija opcion: "))
        if(opcion == 1):
            create()
            time.sleep(2)
            system("clear")
        elif (opcion == 2):
            read()
            time.sleep(2)
        elif (opcion == 3):
            update()
            time.sleep(2)
            system("clear")
        elif (opcion == 4):
            delete()
            time.sleep(2)
            system("clear")
        elif (opcion == 5):
            search()

        elif (opcion == 6):
            break
    except:
        print("Opcion incorrecta. Intente nuevamente.")
        system("clear")

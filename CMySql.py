import os
import mysql.connector

# =========================================================
# CONEXIÓN A MYSQL
# =========================================================
def f_conectar():
    try:
        conexion = mysql.connector.connect(
            host="bkpondqlssv4gg1ww591-mysql.services.clever-cloud.com",
            user="uwvepwmqjv86kc11",
            password="J65SliM1f6aKZnXXO9WG",
            database="bkpondqlssv4gg1ww591",
            port=3306
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"=== DETALLE DEL ERROR DE MYSQL: {err} ===")
        raise err

# =========================================================
# AGREGAR CLIENTE
# =========================================================
def f_agregar_registro(
    nombre,
    apellido_paterno,
    apellido_materno,
    fecha_nacimiento,
    genero,
    correo,
    telefono,
    estado,
    ciudad,
    codigo_postal,
    tipo_cliente,
    intereses,
    limite_credito,
    observaciones
):
    conexion = f_conectar()
    cursor = conexion.cursor()
    sql = """
    INSERT INTO clientes
    (
        nombre,
        apellido_paterno,
        apellido_materno,
        fecha_nacimiento,
        genero,
        correo,
        telefono,
        estado,
        ciudad,
        codigo_postal,
        tipo_cliente,
        intereses,
        limite_credito,
        observaciones
    )
    VALUES
    (
        %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s
    )
    """
    valores = (
        nombre,
        apellido_paterno,
        apellido_materno,
        fecha_nacimiento,
        genero,
        correo,
        telefono,
        estado,
        ciudad,
        codigo_postal,
        tipo_cliente,
        intereses,
        limite_credito,
        observaciones
    )
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

# =========================================================
# LISTAR CLIENTES
# =========================================================
def f_listar_clientes():
    conexion = f_conectar()
    cursor = conexion.cursor()
    sql = """
    SELECT
        id_cliente,
        nombre,
        apellido_paterno,
        apellido_materno,
        fecha_nacimiento,
        genero,
        correo,
        telefono,
        estado,
        ciudad,
        codigo_postal,
        tipo_cliente,
        intereses,
        limite_credito,
        observaciones
    FROM clientes
    ORDER BY id_cliente
    """
    cursor.execute(sql)
    clientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return clientes

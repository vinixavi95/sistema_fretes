from database.connection import get_connection
from fastapi import HTTPException

def inserir(nome, email, telefone, senha, eh_funcionario):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO usuarios (nome, email, telefone, senha, eh_funcionario)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id, nome, email, telefone;
    """

    cur.execute(query, (nome, email, telefone, senha, eh_funcionario))
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return result

def buscar(email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, email, senha FROM usuarios WHERE email = %s", (email,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if not result:
        return None

    return {
        'id': result[0],
        'email': result[1],
        'senha': result[2]
    }

def obter_usuario_por_id(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    row = cur.fetchone()
    columns = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    if not row:
        return None

    return dict(zip(columns, row))

def atualizar_usuario_bd(user_id, nome, email, senha):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        UPDATE usuarios
        SET nome = %s, email = %s, senha = %s
        WHERE id = %s
    """

    cur.execute(query, (nome, email, senha, user_id))
    conn.commit()
    cur.close()
    conn.close()

def inserir_funcionario(usuario_id: int, cargo: str, numero_registro: int):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO funcionarios (id_usuario, cargo, numero_registro)
        VALUES (%s, %s, %s)
        RETURNING id_usuario, cargo;
    """

    cur.execute(query, (usuario_id, cargo, numero_registro))
    result = cur.fetchone()
    conn.commit()
    
    cur.close()
    conn.close()
    
    return result

def buscar_status(usuario_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT eh_funcionario
        FROM usuarios
        WHERE id = %s;
    """

    cur.execute(query, (usuario_id,))
    result = cur.fetchone()

    if cur:
        cur.close()
    if conn:
        conn.close()
        
    if result is None:
        return False 

    return result[0]
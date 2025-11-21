from database.connection import get_connection

def verificar_cargo(usuario_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT cargo FROM funcionarios WHERE id_usuario = %s", (usuario_id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        return None
    
    return row[0]

def listar(data_busca):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, status, valor, meio_pagamento
        FROM fretes 
        WHERE DATE(criado_em) = %s
    """, (data_busca,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def buscar_ponto_do_dia(usuario_id, data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, usuario_id, data, entrada, saida
        FROM pontos
        WHERE usuario_id = %s AND data = %s
    """, (usuario_id, data))

    row = cur.fetchone()
    
    cur.close()
    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "usuario_id": row[1],
        "data": row[2],
        "entrada": row[3],
        "saida": row[4],
    }

def inserir_entrada(usuario_id, data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO pontos (usuario_id, data, entrada)
        VALUES (%s, %s, NOW())
        RETURNING id, usuario_id, data, entrada, saida
    """, (usuario_id, data))

    row = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    return {
        "id": row[0],
        "usuario_id": row[1],
        "data": row[2],
        "entrada": row[3],
        "saida": row[4]
    }

def inserir_saida(ponto_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE pontos
        SET saida = NOW()
        WHERE id = %s
        RETURNING id, usuario_id, data, entrada, saida
    """, (ponto_id,))

    row = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    return {
        "id": row[0],
        "usuario_id": row[1],
        "data": row[2],
        "entrada": row[3],
        "saida": row[4]
    }
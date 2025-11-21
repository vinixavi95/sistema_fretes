from database.connection import get_connection

def inserir_frete(user_id, tipo, valor, distancia, peso, status, cep_origem, cep_destino):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO fretes (usuario_id, tipo_entrega, valor, distancia, peso, status, cep_origem, cep_destino)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """

    cur.execute(query, (user_id, tipo, valor, distancia, peso, status, cep_origem, cep_destino))
    frete_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return frete_id

def obter_frete_por_id(frete_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM fretes WHERE id = %s", (frete_id,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        return None

    columns = [desc[0] for desc in cur.description]
    return dict(zip(columns, row))

def atualizar_status(frete_id, atualizar_status, meio_pagamento):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE fretes SET status = %s, meio_pagamento = %s WHERE id = %s",
        (atualizar_status, meio_pagamento, frete_id)
    )

    conn.commit()
    cur.close()
    conn.close()

def listar(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT * FROM fretes WHERE usuario_id = %s ORDER BY criado_em DESC"
    cur.execute(query, (user_id,))
    rows = cur.fetchall()

    columns = [desc[0] for desc in cur.description]
    resultado = [dict(zip(columns, row)) for row in rows]

    cur.close()
    conn.close()

    return resultado

def buscar_frete(frete_id):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT f.cep_origem, f.cep_destino, u.nome, u.telefone
        FROM fretes f
        JOIN usuarios u ON u.id = f.usuario_id
        WHERE f.id = %s;
    """

    cur.execute(query, (frete_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        return None

    return {
        "cep_origem": row[0],
        "cep_destino": row[1],
        "nome": row[2],
        "telefone": row[3]
    }
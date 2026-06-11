import sqlite3

#lista dos 36 times participantes do torneio
teams = [
    'GER', 'PAR', 'FRA', 'SWE', 'MEX', 'CAN', 'JPN', 'MAR',
    'COL', 'CRO', 'ESP', 'ALG', 'USA', 'AUT', 'BEL', 'RSA',
    'BRA', 'NED', 'CIV', 'NOR', 'KOR', 'ECU', 'ENG', 'SEN',
    'ARG', 'URU', 'TUR', 'IRN', 'SUI', 'NZL', 'POR', 'GHA'
]

#Inicializacao do banco
def initDb():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.executescript("""
            CREATE TABLE IF NOT EXISTS equipes (
                nome_time TEXT PRIMARY KEY,
                gols_pro INTEGER DEFAULT 0,
                gols_contra INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS partidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fase TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS equipe_partidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                equipe_nome TEXT NOT NULL,
                partida_id INTEGER NOT NULL,

                FOREIGN KEY (equipe_nome) REFERENCES equipes(nome_time),
                FOREIGN KEY (partida_id) REFERENCES partidas(id)
            );

            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                partida_id INTEGER NOT NULL,
                ganhador_id TEXT NOT NULL,
                perdedor_id TEXT NOT NULL,

                FOREIGN KEY (partida_id) REFERENCES partidas(id),
                FOREIGN KEY (ganhador_id) REFERENCES equipes(nome_time),
                FOREIGN KEY (perdedor_id) REFERENCES equipes(nome_time)
            );
        """)

    for team in teams:
        cursor.execute(
            "INSERT INTO equipes (nome_time) VALUES (?)",
            (team,)
        )
        
    conn.commit()
    conn.close()

#Reset do banco
def reset():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.executescript("""
    DROP TABLE IF EXISTS resultados;
    DROP TABLE IF EXISTS equipe_partidas;
    DROP TABLE IF EXISTS partidas;
    DROP TABLE IF EXISTS equipes;
    """)
    conn.commit()
    conn.close()

#Atualizar a quantidade de gols feito por cada pais por partida
def atualizarGols(golsPro, golsContra, Equipe):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    
    cursor.execute(
    """
    UPDATE equipes
    SET
        gols_pro = gols_pro + ?,
        gols_contra = gols_contra + ?
    WHERE nome_time = ?
    """,
    (golsPro, golsContra, Equipe)
    )
    conn.commit()
    conn.close()

#Inserir cada partida no banco e relaciona-la com suas respectivas equipes
def inserirPartidas(fase, equipe1, equipe2):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    # Cria a partida
    cursor.execute(
        "INSERT INTO partidas (fase) VALUES (?)",
        (fase,)
    )

    partida_id = cursor.lastrowid

    # Relaciona equipe 1
    cursor.execute(
        """
        INSERT INTO equipe_partidas (equipe_nome, partida_id)
        VALUES (?, ?)
        """,
        (equipe1, partida_id)
    )

    # Relaciona equipe 2
    cursor.execute(
        """
        INSERT INTO equipe_partidas (equipe_nome, partida_id)
        VALUES (?, ?)
        """,
        (equipe2, partida_id)
    )

    conn.commit()
    conn.close()
    return partida_id

#Inserir resultado final das partidas
def inserirResultados(partidaId, ganhador, perdedor):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO resultados (partida_id, ganhador_id, perdedor_id)
        VALUES (?, ?, ?)
        """,
        (partidaId, ganhador, perdedor)
    )
    conn.commit()
    conn.close()

#====INFORMACOES E ESTATISTICAS====

# Qual equipe marcou mais gols na competição?
def ConsultarMaiorGoleador():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome_time, gols_pro
        FROM equipes
        WHERE gols_pro = (
            SELECT MAX(gols_pro)
            FROM equipes
        )
    """)

    resultado = cursor.fetchall()

    conn.close()

    return resultado
    
# Qual equipe sofreu menos gols na competição?
def ConsultarEquipeMenosGols():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome_time, gols_contra
        FROM equipes
        WHERE gols_contra = (
            SELECT MIN(gols_contra)
            FROM equipes
        )
    """)

    resultado = cursor.fetchall()

    conn.close()

    return resultado
    
# Quantas partidas foram disputadas em cada fase?
def ConsultarPartidasFases():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT fase, COUNT(*) as total
        FROM partidas
        GROUP BY fase
        ORDER BY total DESC
    """)
    
    resultado = cursor.fetchall()

    conn.close()

    return resultado
    
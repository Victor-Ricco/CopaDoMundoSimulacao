import sqlite3

teams = [
    'GER', 'PAR', 'FRA', 'SWE', 'MEX', 'CAN', 'JPN', 'MAR',
    'COL', 'CRO', 'ESP', 'ALG', 'USA', 'AUT', 'BEL', 'RSA',
    'BRA', 'NED', 'CIV', 'NOR', 'KOR', 'ECU', 'ENG', 'SEN',
    'ARG', 'URU', 'TUR', 'IRN', 'SUI', 'NZL', 'POR', 'GHA'
]
def initDb():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.executescript("""
            CREATE TABLE IF NOT EXISTS equipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_time TEXT NOT NULL,
                gols_pro INTEGER DEFAULT 0,
                gols_contra INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS partidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fase TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS equipe_partidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                equipe_id INTEGER NOT NULL,
                partida_id INTEGER NOT NULL,

                FOREIGN KEY (equipe_id) REFERENCES equipes(id),
                FOREIGN KEY (partida_id) REFERENCES partidas(id)
            );

            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                partida_id INTEGER NOT NULL,
                ganhador_id INTEGER NOT NULL,
                perdedor_id INTEGER NOT NULL,

                FOREIGN KEY (partida_id) REFERENCES partidas(id),
                FOREIGN KEY (ganhador_id) REFERENCES equipes(id),
                FOREIGN KEY (perdedor_id) REFERENCES equipes(id)
            );
        """)

    for team in teams:
        cursor.execute(
            "INSERT INTO equipes (nome_time) VALUES (?)",
            (team,)
        )
        
    conn.commit()
    conn.close()
    
def reset():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM equipes")
    conn.commit()
    conn.close()
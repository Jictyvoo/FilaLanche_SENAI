import sqlite3;

# conectando...
conn = sqlite3.connect('FilaLanche_SENAI.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE Estudante (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        turma VARCHAR(9) NOT NULL,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
);
""")

# desconectando...
conn.close()
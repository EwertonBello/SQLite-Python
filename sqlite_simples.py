import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

#cursor.execute('CREATE TABLE nomes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)')
nome = input('Cadastrar nome: ')
cursor.execute('INSERT INTO nomes(nome) VALUES(?)',(nome,))
cursor.execute('SELECT * FROM nomes')
rows= cursor.fetchall()
for row in rows:
    print ('ID: {0} Nome: {1}'.format(row[0], row[1]))
conn.commit()

import mysql.connector
from raspagem_dos_dados import titulo
from raspagem_dos_dados import precos_formatados

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Wes170702',
    database='bdprojeto',
)
#cursor é quem faz a conexao com o banco de dados
cursor = conexao.cursor()

#crud
nome_produto = titulo.text
valor = precos_formatad
comando = f'INSERT INTO raspagem (nome_produto, valor) VALUES ({nome_produto} , {valor}) '
cursor.execute(comando)
conexao.commit()
#resultado = cursor.fetchall()


#finalizar a conexao e o cursor
cursor.close()
conexao.close()

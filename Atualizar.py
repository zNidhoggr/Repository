#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('projeto.db')
cursor = conn.cursor()

id_cliente = input("Digite o id do cliente: ")
novo_fone = input("Digite o novo fone do cliente: ")

# alterando os dados da tabela
cursor.execute("""
UPDATE projeto
SET fone = ? where id = ?
""", (novo_fone, id_cliente))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()
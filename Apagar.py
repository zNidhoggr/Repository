#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('projeto.db')
cursor = conn.cursor()

id_cliente = input("Digite o id do cliente que deseja deletar: ")

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM projeto
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('projeto.db')
cursor = conn.cursor()

# solicitando os dados ao usuário
p_nome = input('Nome: ')
p_idade = input('Idade: ')
p_fone = input('Fone: ')
p_cidade = input('Cidade: ')
p_uf = input('UF: ')


cursor.execute("""
INSERT INTO projeto (nome, idade, fone, cidade, uf)
VALUES (?,?,?,?,?)
""", (p_nome, p_idade, p_fone, p_cidade, p_uf))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
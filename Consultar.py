#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('projeto.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM projeto;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
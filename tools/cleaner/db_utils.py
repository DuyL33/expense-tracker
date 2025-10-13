import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="expdb",
        user="expuser",
        password="expsecret"
    )

def insert_transaction(cur, t):
    cur.execute("""
        INSERT INTO transactions (transaction_date, post_date, description, category, type, amount_cents, memo)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        t['Transaction Date'],
        t['Post Date'],
        t['Description'],
        t['Category'],
        t['Type'],
        t['Amount_cents'],
        t.get('Memo')
    ))

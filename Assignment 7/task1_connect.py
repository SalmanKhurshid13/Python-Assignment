import psycopg2

# connect to the default postgres database first
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="mypassword123",
    database="postgres"
)

cur = conn.cursor()
cur.execute("SELECT version();")
result = cur.fetchone()
print("Connected to PostgreSQL!")
print("Server version:", result)

cur.close()
conn.close()

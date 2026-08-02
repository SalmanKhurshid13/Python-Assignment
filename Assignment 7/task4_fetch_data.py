import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="mypassword123",
    database="employee_db"
)
cur = conn.cursor()

# fetchone example
cur.execute("SELECT * FROM employees;")
first = cur.fetchone()
print("First employee:", first)

# fetchall example
cur.execute("SELECT * FROM employees;")
all_rows = cur.fetchall()
print("\nAll employees:")
for row in all_rows:
    print(row)

cur.close()
conn.close()

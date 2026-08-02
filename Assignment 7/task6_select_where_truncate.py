import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="mypassword123",
    database="employee_db"
)
cur = conn.cursor()

# SELECT with WHERE condition
cur.execute("SELECT * FROM employees WHERE department = %s", ("Engineering",))
rows = cur.fetchall()
print("Employees in Engineering department:")
for row in rows:
    print(row)

# TRUNCATE the table (removes all rows)
confirm = input("\nType yes to truncate the employees table: ")
if confirm.lower() == "yes":
    cur.execute("TRUNCATE TABLE employees RESTART IDENTITY;")
    conn.commit()
    print("Table truncated successfully! All rows removed.")
else:
    print("Truncate cancelled.")

cur.close()
conn.close()

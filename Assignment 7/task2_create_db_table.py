import psycopg2

# Step 1: connect to default database to create our new database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="mypassword123",
    database="postgres"
)
conn.autocommit = True
cur = conn.cursor()

cur.execute("SELECT 1 FROM pg_database WHERE datname = 'employee_db';")
if cur.fetchone() is None:
    cur.execute("CREATE DATABASE employee_db;")
    print("Database employee_db created!")
else:
    print("Database employee_db already exists.")

cur.close()
conn.close()

# Step 2: connect to employee_db and create the table
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="mypassword123",
    database="employee_db"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(100),
        salary NUMERIC(10,2)
    );
""")
conn.commit()
print("Table employees created!")

cur.close()
conn.close()

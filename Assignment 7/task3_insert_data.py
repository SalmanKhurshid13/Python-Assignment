import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="mypassword123",
    database="employee_db"
)
cur = conn.cursor()

# list of employees to insert
employees = [
    ("Aarav Sharma", "Engineering", 65000),
    ("Priya Verma", "Marketing", 52000),
    ("Rohan Gupta", "Engineering", 70000),
    ("Sneha Reddy", "HR", 48000)
]

for emp in employees:
    cur.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", emp)
    print("Inserted:", emp)

conn.commit()
print("All records inserted successfully!")

cur.close()
conn.close()

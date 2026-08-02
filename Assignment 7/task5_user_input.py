import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="mypassword123",
    database="employee_db"
)
cur = conn.cursor()

# take input from the user
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

# parameterized query keeps this safe from SQL injection
cur.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)",
            (name, department, salary))
conn.commit()

print("Employee", name, "added successfully!")

cur.close()
conn.close()

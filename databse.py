import mysql.connector

try:

    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='kavya',
        database='tweak'
    )


    if con.is_connected():
        print('Connected successfully')


    cursor = con.cursor()


    query = 'INSERT INTO students (id, name, marks) VALUES (%s, %s, %s)'


    data = [(101, 'kavya', 88), (102, 'sri', 85), (103, 'nandini', 89)]


    cursor.executemany(query, data)


    con.commit()

    print(f"{cursor.rowcount} record(s) inserted.")

except mysql.connector.Error as err:

    print(f"Error: {err}")

finally:

    if con.is_connected():
        cursor.close()
        con.close()
        print("MySQL connection is closed.")

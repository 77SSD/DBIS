import psycopg2
#Function to check if an actor with a given ID already exists in the database
def actor_exists(cur, act_id):
    cur.execute("SELECT COUNT(*) FROM actor WHERE act_id = %s", (act_id,))
    count = cur.fetchone()[0]
    return count > 0

try:
    connection = psycopg2.connect(
        database='moviedb',
        user="Sakeena",
        password="1995",
        host="localhost",
        port=5432,
        
    )

    cursor = connection.cursor()

    act_id = input("Enter actor id: ")
    act_fname = input("Enter First name: ")
    act_lname = input("Enter Last name: ")
    act_gender = input("Enter act_gender: ")

    if actor_exists(cursor, act_id):
        print("Actor ID already exists")
    else:
        cursor.execute(
            "INSERT INTO actor(act_id, act_fname, act_lname, act_gender) VALUES (%s, %s, %s, %s)",
            (act_id, act_fname, act_lname, act_gender)
        )
        print("Actor details inserted into the actor table successfully")

    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error:", error)
finally:
    if connection:
        cursor.close()
        connection.close()




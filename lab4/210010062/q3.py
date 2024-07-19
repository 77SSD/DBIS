import psycopg2

try:
    connection = psycopg2.connect(database='moviedb',
                host="localhost",
                user="Sakeena",==========
                password="1995",
                port=5432) 
                        
    
    connection.autocommit = False  # Set autocommit to False to enable transactions
    mycursor = connection.cursor()
    

    no_movies=int(input("Enter the number of movies:"))
    act_id=131
    movieID=[]
    roles=[]
    for i in range(no_movies):
        movie_id=int(input(f"Enter movie id of movie number {i+1}:"))
        role=input(f"Enter role of the actor in movie number {i+1}:")
        movieID.append(movie_id)
        roles.append(role)

    for i in range(no_movies):
        #print(f"{movieID[i]}\n")
        mycursor.execute("SELECT * FROM movie WHERE mov_id = %s", (movieID[i],))
        existing_movie = mycursor.fetchone()

        if existing_movie:
            line = "INSERT INTO movie_cast VALUES (" + str(act_id) + "," + str(movieID[i]) + ",\'" + roles[i] + "\');"
            mycursor.execute(line)
            
        else:
            print("Movie number {i+1} is not present in the database. Database is not updated")
            conn.rollback()
            print("ROLLBACK")
            break
                
    else:
            # Commit the transaction if all movies are inserted successfully
            connection.commit()
            print("Transaction committed successfully.")

except (Exception, psycopg2.DatabaseError) as error:
    # If an error occurs, roll back the transaction
    if connection:
        connection.rollback()
        print("ROLLBACK")
    print("Error:", error)    

connection.commit()
connection.close()
mycursor.close()

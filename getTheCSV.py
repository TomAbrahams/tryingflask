import math
import psycopg2
import csv
import secret
import os
#Menu program.
def makeCSV(myEmail):

    email = myEmail
    query = """
        select picpoints.*, scores.score, scores.email
        FROM picpoints
        INNER JOIN scores ON (picpoints.imgName = scores.imagename and scores.email =
        """

    numOfRowsRequested = 50

    #Deals with if their is a number of rows requested.


    query += " '" + email + "') "
    query += " ORDER BY scores.id desc "
    query += " LIMIT "
    query += str(numOfRowsRequested)
    #print(query)   #Debug purposes.
    myMail = " '" + email + "') "
    #print(myMail)  #Debug purposes.
    connection = "host = 'localhost' dbname = 'learningflask' user='utkeitaro' password='" + secret.theSecret + "'"
    print("Connecting to database...")
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    #cursorX = conn.cursor()
    flag = False
    try:
        cursor.execute(query)
        print("\nAttempt Successful\n")
        flag = True
    except:
        print("\nNo Query available\n")
        flag = False
    rows = cursor.fetchall()
    print("Number of rows\n")
    print(len(rows))
    numberOfRows = len(rows)
    if(numberOfRows):
        output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
        email = email.replace("@","_")
        saveFileName = email + '-' + 'resultsfile.csv'
        direct = os.getcwd()
        os.chdir('..')
        print(direct)
        goBackDir = os.getcwd()
        print(goBackDir)
        path = os.path.join(goBackDir+"/dlibtesting/fileRecords/", saveFileName)

        with open(path,'w') as f:
            cursor.copy_expert(output,f)
    else:
        print("No Data to report.")

    conn.close()

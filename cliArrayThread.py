import socket, json

def sendingArray(myArray, myEmail):
    IP = 'localhost'
    PORT = 5019
    socko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = (IP, PORT)
    socko.connect(serverAddress)
    data = json.dumps({"email" : myEmail, "results" : myArray})
    print("Preparing to send data", data)
    print(len(data))
    #Set up the size of the data.
    sizeOfData = len(data)
    sizeOfData = str(sizeOfData)
    for i in range(20):
        sizeOfData = '0' + sizeOfData
        if len(sizeOfData) == 20:
            break
    #Sending size of 20
    print("Size of the data", int(sizeOfData))
    socko.sendall(sizeOfData.encode('utf-8'))
    print("Send json...")
    socko.sendall(data.encode('utf-8'))
    #Then I should have sent the info to the serverself.
    socko.close()
#Gets array.
def getingArray(connection, address):
    print("Connected by ", address)
    print("Beginning Data Retrieval....")
    print("Client, what is the address...")
    #Gets the data
    msgSize = connection.recv(20)
    msgSize = int(msgSize)
    data = connection.recv(msgSize)

    connection.close()
    data = data.decode('utf-8')
    print("Data Printing...")
    print(data)
    print("Data Finished...")
    data = json.loads(data)
    myEmail = data.get("email")
    myArray = data.get("results")
    print("Email", myEmail)
    print("Results",myArray)
    return myArray

def frontendSide(email):
    IP = 'localhost'
    PORT = 5101
    serverAddress = (IP, PORT)
    A = [0,1,2,3]
    email = "pd@gmail.com"
    sendingArray(A, email)
    serverSocko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocko.bind(serverAddress)
    print("Setup binding.")
    serverSocko.listen(1)
    print("listening for results")
    conn, addr = serverSocko.accept()
    testResults = getingArray(conn, addr)
    if testResults[0] == -999:
        print("error.")
    else:
        print(testResults)
    return testResults

if __name__ == '__main__':
    IP = 'localhost'
    PORT = 5101
    serverAddress = (IP, PORT)
    A = [0,1,2,3]
    email = "pd@gmail.com"
    sendingArray(A, email)
    serverSocko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocko.bind(serverAddress)
    print("Setup binding.")
    serverSocko.listen(1)
    print("listening for results")
    conn, addr = serverSocko.accept()
    testResults = getingArray(conn, addr)
    if testResults[0] == -999:
        print("error.")
    else:
        print(testResults)

import getpass #Here we are using the getpass module instead of the input function to make sure that the user doesn’t get to see what he/she write in the password field.
database = {"r.garudkar": "123456", "garudkar.r": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("INCORRECT Enter Your Password Again : ")
        break
print("Verified")
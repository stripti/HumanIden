
myfile = open("admininfo.csv", "a+")
myfile.write(str("Username" + "," + "Userid" + "," + "Password"))
myfile.write("\n")
for counter in range(5):
    print("")
    print("Next account")
    name = input("Enter user name: ")
    userid = input("Enter user id: ")
    password = input("Enter password: ")
    newdata = name + "," + userid + "," + password
    myfile.write(str(newdata))
    myfile.write("\n")
myfile.close()
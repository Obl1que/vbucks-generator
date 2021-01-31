amount = int(input("how many vubkccs you want????? (max 10000000) "))
if amount >= 10000000:
    print("no!!!!")
    quit()
import time
print("generating vcubcks")
for i in range(amount):
    print("vbuck number " + str(i + 1) + " generated")
print("all generated!")
password = str(input("enter your fortnite password to confirm!! "))
username = str(input("cannot verify password! enter username to verify!! "))
print("ok confirmed with password " + password + " and username " + username)
print("check your cbucks!!")
file1 = open("generatedlist.txt","a")
file1.writelines([str(amount)])
file1.close()


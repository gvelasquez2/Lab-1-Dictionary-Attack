# Gilbert Velasquez
# CS 4351 Assignment # 1
# Date of Last Edit : 9/18/2020
# Edit Purpose : Added comments 

# This is part 1 from Assignment # 1. This code is independent and can be ran alone using the command line by using:  python Lab1part1.py
# This portion of the assingment uses md5_crypt from the passlib library, which will need to be downloaded if not already installed.
# The purpose of this program is to try and crack as many passwords as possible given the shadowfile and list of common passwords.
 
from passlib.hash import md5_crypt
import time


##### This method reads the shadowFile.txt file and returns a list of all the users, thier salt values, and hashed passwords  #####
def createUserList():
    shadowFile = open("shadowFile.txt", encoding = "ISO-8859-1")
    listOfUsers =[]

    for line in shadowFile.readlines()[2:]: # we skipp the first two lines to save time becasue we arent trying to crack those 
        line = line.strip()
        newLine = line.split(":")
        user = newLine[0] # get username
        encryptedStr = newLine[1] # get encrypted string 
        splitEncryptedStr = encryptedStr.split("$")
        salt = splitEncryptedStr[2] #get salt from the encrypted string 
        list1 = [user,salt,encryptedStr]
        listOfUsers.append(list1)
        
    return listOfUsers
            
##### This method retruns a list created from all the passwords in the commonPasswordFile2.txt file #####
def createPasswordList():
    passwordList = []
    passwordFile = open("commonPasswordFile2.txt",encoding = "ISO-8859-1")
    
    for line in passwordFile.readlines():
        line = line.strip()
        passwordList.append(line)
        
    return passwordList

##### This method runs the dictionary attack and writes results to the Results1.txt file #####
def dictionaryAttack(passwordList, listOfUsers):
    resultsFile = open("Results1.txt","w")

    for user in listOfUsers:
        for password in passwordList[:10000]: # I put this limitation on the program so that the runtime wouldnt be as long. We can extend the range or remove it to raise teh chances of finding a password hidden deeper in the file 
                attempt = md5_crypt.using(salt = user[1]).hash(password) # using the salt to encrypt the password from the passwordlist to attempt and match to user password 
                if(attempt == user[2]):
                    resultsFile.write("Username: " + user[0] + "  Password:" + password +"\n") 
                    break


    
    
start_time = time.time()
print("Starting Attack")    
users = createUserList()
passwords = createPasswordList()
dictionaryAttack(passwords,users)
print("Finished Cracking Passwords, please review Results1.txt to see list of cracked passwords")
print ("Program took:", time.time() - start_time, "to run")

# program runs in about 102 seconds 
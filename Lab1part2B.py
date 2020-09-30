# Gilbert Velasquez
# CS 4351 Assignment # 1
# Date of Last Edit : 9/18/2020
# Edit Purpose : Added comments 

# This is part 2B from Assignment # 1. This code is currently programmed to be run after Lab1part2A
# This code can be run independently by using the command line by using:  python Lab1part2B.py after lines 199 - 205 are uncommmented
# This code requires the hashlib library and time library. 
# This code generates different files containing possbile passwords for users, as per the types of passwords users can make given the Assingment 
# The code generates the three files and in addition the the words.txt file which contains the 10,000 most common words, will run a dictionary attack for each file 
# Cracked Passwords are output in the Results2B.txt file

import hashlib
import time

##### This method generates all numbers from 0 - 99999999 and stores them in a file #####
def generateNumbersFile():
    NumbersFile = open("Numbers.txt","w") # create file 
    
    for i in range(0,10000000):
        NumbersFile.write(str(i)+"\n") # write every number to file 
    NumbersFile.close() #close file 
    
    
##### This method concatenates every combination of words whose combined length is greater than 5 #####
def generateCombinedWordsFile():
    WordplusWordFile = open("combinedWords.txt","w") # create file 
    passwordFile = open("words.txt",encoding = "ISO-8859-1") #read 10,000 most popular words 
    words = [] # make a list to store all words 
    
    for line in passwordFile.readlines(): # with this loop store all words in the file into the list 
        line = line.strip()
        words.append(line) 
    
    for word in words: # loop for first word
        for word2 in words: # loop to concatenate word with each and eery other word 
            string = (word + word2)
            if len(string) >= 5: # if length is greater than 5
                WordplusWordFile.write(string+"\n") # append concatenated word to file 
                
    WordplusWordFile.close() #close files 
    passwordFile.close()
            

##### This method generates all the combinations of words and numbers whose length is atmost 10
def generateWordsWithNumbersFile():
    wordsWithNumbersFile = open("WordsWithNumbers.txt","w") # create file 
    passwordFile = open("words.txt",encoding = "ISO-8859-1") # open words file 
    
    for line in passwordFile.readlines():
        line = line.strip()
        if(len(line) >= 4  and len(line)<= 9): # if we widen this range we potentially can guess more passwords but even this range took a toll on my pc 
            for i in range(0,9999): # same with this one, we can increase 9999 to something like 999999 and potentially guess more passwords 
                stringToWrite = (line+str(i))
                if(len(stringToWrite) >= 5 and len(stringToWrite) <= 10): # only save passwords whose length is larger than 5 
                    wordsWithNumbersFile.write(stringToWrite + "\n") # write those passwords into the file
                    
    wordsWithNumbersFile.close() #close files
    passwordFile.close()


##### This Method uses the words.txt file to attempt to crack every password in the userDataArray #####
def dictionaryAttack(userDataArray):
    passwordFile = open("words.txt",encoding = "ISO-8859-1")
    crackedPasswordsFile = open("crackedPasswordsPart2B.txt","w") # used to sotre cracked passwords
   
    for line in passwordFile.readlines():
        line = line.strip()
        
        for user in userDataArray:
            encryptedPass = user[2]
            salt = user[1]
            PasswordToTest = salt + line
            password = hashlib.md5(PasswordToTest.encode('utf-8')).hexdigest()
            
            
            if(password == encryptedPass):
                crackedPasswordsFile.write(str(user[0])+ ":"+str(line) + ":"+ str(user[3])+"\n") # if found append info to the cracked password file
                userDataArray.remove(user) # remove the used since we have it's password 
    
    passwordFile.close()
    return userDataArray # return list of uncracked passwords  


#####This method uses the wordsWithNumbers.txt file created by running generateWordsWithNumbersFile() to attempt to crack Passwords #####
def WordsWithNumbersAttack(userDataArray):
    passwordFile = open("wordsWithNumbers.txt",encoding = "ISO-8859-1")
    crackedPasswordsFile = open("crackedPasswordsPart2B.txt","a")
    
    for line in passwordFile.readlines():
        line = line.strip()
        
        for user in userDataArray:
            encryptedPass = user[2]
            salt = user[1]
            PasswordToTest = salt + line
            password = hashlib.md5(PasswordToTest.encode('utf-8')).hexdigest()
            
            
            if(password == encryptedPass):
                crackedPasswordsFile.write(str(user[0])+ ":"+str(line) + ":"+ str(user[3])+"\n") # if found append info to the cracked password file
                userDataArray.remove(user) # remove the used since we have it's password 
    
    passwordFile.close()
    return userDataArray # return list of uncracked passwords  



##### This method uses the Numbers.txt file created by running generateNumbersFile() to attempt to crack passwords #####
def numbersAttack(userDataArray):
    passwordFile = open("Numbers.txt",encoding = "ISO-8859-1")
    crackedPasswordsFile = open("crackedPasswordsPart2B.txt","a") # we will now append to the file since this method is called after another attack
        
    for line in passwordFile.readlines():
        line = line.strip()
        
        for user in userDataArray:
            encryptedPass = user[2]
            salt = user[1]
            PasswordToTest = salt + line
            password = hashlib.md5(PasswordToTest.encode('utf-8')).hexdigest()
            
            
            if(password == encryptedPass):
                crackedPasswordsFile.write(str(user[0])+ ":"+str(line) + ":"+ str(user[3])+"\n") # if found append info to the cracked password file
                userDataArray.remove(user) # remove the used since we have it's password 
    
    passwordFile.close()
    return userDataArray # return list of uncracked passwords  



##### This method uses the combinedWords.txt file created by running generateCombinedWordsFile() to attampt to crack passwords #####
def combinedWordsAttack(userDataArray):
    passwordFile = open("combinedWords.txt",encoding = "ISO-8859-1")
    crackedPasswordsFile = open("crackedPasswordsPart2B.txt","a")
    
    for line in passwordFile.readlines():
        line = line.strip()
        
        for user in userDataArray:
            encryptedPass = user[2]
            salt = user[1]
            PasswordToTest = salt + line
            password = hashlib.md5(PasswordToTest.encode('utf-8')).hexdigest()
            
            
            if(password == encryptedPass):
                crackedPasswordsFile.write(str(user[0])+ ":"+str(line) + ":"+ str(user[3])+"\n") # if found append info to the cracked password file
                userDataArray.remove(user) # remove the used since we have it's password 
    
    passwordFile.close()
    return userDataArray # return list of uncracked passwords  


##### This Method reads the Unsalted Passwords File and returns a list that contains information extracted from file (Username,Password,Index) #####
def createUserDataList():
    index = 0
    userDataList = [] # Used to store all user data (Username, Password, Index)
    passFile = open("SaltedPassTable.txt",encoding = "ISO-8859-1") # File with user data 
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            salt = line.split(':')[1]
            encryptedPass = line.split(':')[2].strip()
            userDataList.append([user,salt,encryptedPass,index]) # I store the index so that I can sort the data before creating the final output file
            index = index+1 
    return userDataList


##### This method reads the cracked passwords file and nicely outputs the contents to a file for easier access #####    
def formatOutput():
    crackedPasswords = open("crackedPasswordsPart2B.txt",encoding = "ISO-8859-1")
    finalResults = open("Results2B.txt","w")
    formattedResults = []
    
    for line in crackedPasswords.readlines():
        line = line.strip()
        
        splitLine = line.split(":")
        username = splitLine[0]
        password = splitLine[1]
        order = splitLine[2]
        
        formattedResults.append((username,password,int(order)))
        
    formattedResults.sort(key = lambda x : x[2]) # sort to easily see which passwords were cracked 
        
    for item in formattedResults:
        finalResults.write("Username: " + str(item[0])+ " Password: " + str(item[1] + "     " + "\n")) #write the contents to the Results.txt file 

        


start_time = time.time()

# Uncomment this section if Lab1part2B is run on it's own. I commented it out because we have created these file when running Lab1part2A

#generateNumbersFile()  # Takes about 110 seconds to generate this file 
#print("Finished generating Numbers File")
#generateCombinedWordsFile() # Takes about 128 seconds to run
#print("Finished generating Combined Words File") 
#generateWordsWithNumbersFile() # Takes 265 seconds to run
#print("Finished Generating All Files")
#print("_________________________")

data = createUserDataList()
print("In Dictionary Attack")
dataAfterDictionary = dictionaryAttack(data)
print("In Words and Numbers Attack")
dataAfterWordsAndNumbers = WordsWithNumbersAttack(dataAfterDictionary)
print("In Numbers Attack")
dataAfterNumbers = numbersAttack(dataAfterWordsAndNumbers)
print("In Combined Words Attack")
dataAfterCombinedWords = combinedWordsAttack(dataAfterNumbers)

formatOutput()

print("Password Cracking for Part 2B Complete, Please review Results2B.txt to see list of cracked passwords")
print ("Program took:", time.time() - start_time, "to run")
# Program takes 60217 seconds to run which is almost 17 hours 
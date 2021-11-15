#1. Program to
#a) take positive integer n as input from the user , where n being the number of user profiles we need to maintain a record for
#b) should prompt the user to enter the name, age , sex for 'n' number of times (users)
#c) Store the user information in a file where each line being the record for each user 
#d) Write another function that displays number of users by sex 

def userprofile():
#use input function to prompt the user to enter number of user profiles
#type cast integer as input  
  global n
  n  = int(input("Please enter the number of user profiles that you wish to maintain:"))
#initialize name array and declare it as global variable
  global name
  name = []
#initialize age array and declare it as a global variable 
  global age
  age = []
#initialize sex array and declare it as a global variable
  global sex
  sex = []
#initialize i loop counter variable
  i = 0
#use for loop to prompt entry of details n number of times
  for i in range(n):
#Prompt user to input to enter the name for ith user
   name.append(input("Please enter the name for user {}:".format(i+1)))
#Prompt user to input to enter the age for ith user
   age.append(input("Please enter the age for user {}:".format(i+1)))
#Prompt user to input to enter the sex for ith user
   sex.append(input("Please enter the sex[F,M] for user {}:".format(i+1)))
#Store the user information in a file named userinfo.txt
#open a file named userinfo.txt or create it in write mode if it does not exist
  with open("userinfo.txt","w+") as f:
# write the name age and sex of user info in each line in the file
# initialize a loop variable j
   j = 0
#use for loop to write the contents of user info to the file, use comma as a delimiter in the file contents 
   for j in range(n):
    line = name[j]+","+age[j]+","+sex[j]+"\n"
    f.write(line)
#close the file
   f.close()

#call the main function to execute all lines of code above
userprofile()
 
#Function to display number of users by sex
def userprofilebysex():
#Read the file userinfo.txt 
 sexfile = []
 content = []
 contentk = []
 with open("userinfo.txt","r") as f:
  if f.mode == 'r':
   content = f.readlines()
  for k in range(len(content)):
   contentk = content[k]
   l = len(contentk)
   sexfile = contentk[l-1]
#Read the contents of user profile by sex
  countF = sex.count("F")
  countM = sex.count("M")
  print("Number of users who are Female is:", countF)
  print("Number of users who are Male is:", countM)

userprofilebysex()
  


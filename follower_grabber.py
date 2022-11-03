import os

# WHAT DOES THIS DO???
# This script takes a twitter data download and given the file is in the right directory,
# finds following.js and converts it into a list of account links

# Following data
def following():
   print("Processing following data...")
   with open(path, 'r') as f:
      data = f.read()

   t = False
   complete = ""

   for i in range(len(data)):
      if data[i] =='h':
         t = True

      while t:
         if data[i] == "\"":
            t = False
            complete += "\n"
            break

         else:
            complete += data[i]
            i += 1

   filename = username + "_following.txt"
   with open(filename, 'w') as g:
      g.write(complete)


# Follower data
def followers():
   print("Processing follower data...")
   with open(path2, 'r') as f:
      data = f.read()

   t = False
   complete = ""

   for i in range(len(data)):
      if data[i] =='h':
         t = True

      while t:
         if data[i] == "\"":
            t = False
            complete += "\n"
            break

         else:
            complete += data[i]
            i += 1

   filename = username + "_followers.txt"
   with open(filename, 'w') as g:
      g.write(complete)

# main
# please rename downloaded folder to twitter username before running
username = input("What is your Twitter username: ")
path = username+'\\data\\following.js'
path2 = username+'\\data\\follower.js'
exist = os.path.exists(path)

if exist == False:
   print("Could not find twitter data with that username in the current directory. Please try again later\n")
   exit(1)

following()
followers()

print("Data has been processed\n")
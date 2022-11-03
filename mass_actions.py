import tweepy
import logging
import os

# debug code: please do not remove - just comment out
logger = logging.getLogger("tweepy")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="tweepy.log")
logger.addHandler(handler)

# locals
k = True
list = []   # list will only store user ids
recent = ""
fn = ""

def initialize():
   bearer_token = input("Enter your Bearer Token (Paste here): ")
   return bearer_token

# ------------------------------------------------------------------------------

# other functions
def verify():
   verify = input("Are you sure you want to do this? (y/n): ")
   if verify == "y":
      return True
   else:
      return False

def get_tid():
   return input("Enter target user id: ")

def get_tun():
   return input("Enter target username: ")

def get_filename():
   fn = input("Please enter a filename: ")

def check_filename():
   exist = os.path.exists(fn)

   if exist == False:
      print("Invalid filename. Please check file is in current directory/path is in correct format\n")
      return 0

   else:
      return 1

def list2string():
   l = []
   for o in (len(list)-1):
      l.append(list(o))

# ------------------------------------------------------------------------------

# actions
def followers(tid, tun):
   recent = "follower"
   list = client.get_list_followers(tid)
   print("Action Completed Successfully\n")

def following(tid, tun):
   recent = "following"
   list = client.get_followed_lists(tid)

def follow(tid, tun):
   for p in (len(list)-1):
      client.follow_list(list(p))

def unfollow(tid, tun):
   for p in (len(list)-1):
      client.unfollow_list(list(p))

def export_list():
   recent = "export"
   if recent == "clear":
      print("no data has been grabbed yet\n")
      return

   else:
      get_filename()
      print("Exporting " + str(recent) + " data to " + str(fn) + "...\n")

      with open(fn, 'w') as f:
         f.write(list2string())

def import_list():
   recent = "import"
   get_filename()
   check_filename

   with open(fn, 'r') as f:
      f.write()

def clear():
   recent = "clear"
   list = []
   return

def last():
   print(recent)
   return

def help():
   print("\
         \'followers\' | gets list of those target is following\n\
         \'following\' | gets list of those following target\n\
         \'follow\'    | follows list of users\n\
         \'unfollow\'  | unfollows list of users (if user not followed, will skip)\n\
         \'export\'    | exports data to text file with name of choice\n\
         \'import\'    | imports data from file (must be from this script)\n\
         \'clear\'     | removes cached list\n\
         \'last\'      | repeats last action\n\
         \'change\'    | changes auth account (paste bearer token)\n\
         \'quit\'      | quits the script\n\
      ")

# ------------------------------------------------------------------------------

def actions():
   inner = input("What would you like to do (Type 'help' for options): ")
   if inner == "help":
      help()
      return

   elif inner == "followers":
      target_user_id = get_tid()
      target_username = get_tun()
      followers(target_user_id, target_username)
      return

   elif inner == "following":
      target_user_id = get_tid()
      target_username = get_tun()
      following(target_user_id, target_username)
      return

   elif inner == "follow":
      if verify():
         follow()
      else:
         return

   elif inner == "unfollow":
      if verify():
         unfollow()
      else:
         return

   elif inner == "export":
      export_list()
      return

   elif inner == "import":
      import_list()
      return

   elif inner == "clear":
      clear()
      return
   
   elif inner == "last":
      last()
      return

   elif inner == "quit":
      k = False
      exit(0)

   else:
      print("Invalid input. Check 'help' for valid inputs\n")

# ------------------------------------------------------------------------------

def main():
   bearer_token = initialize()
   global client
   client = tweepy.Client(bearer_token)
   while k:
      actions()

if __name__=="__main__":
   main()
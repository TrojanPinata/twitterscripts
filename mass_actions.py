import tweepy
import logging
import os

# debug code: please do not remove - just comment out
logger = logging.getLogger("tweepy")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="tweepy.log")
logger.addHandler(handler)

# ------------------------------------------------------------------------------

# helper functions
def initialize():
   bearer_token = input("Enter your Bearer Token (Paste here): ")
   return bearer_token

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
   return str(input("Please enter a filename: "))

def check_filename(fn):
   exist = os.path.exists(fn)

   if exist == False:
      print("Invalid filename. Please check file is in current directory/path is in correct format\n")
      return 0

   else:
      return 1

def dict2stringlist(li):
   fid = []
   fum = []
   for a in li.data:
      fid.append(str(a.id))
   for a in li.data:
      fum.append(str(a.username)+"\n")
   return fid, fum

# ------------------------------------------------------------------------------

# actions
def followers(client, tid, tun, li, recent):
   recent = "followers"
   c = client.get_users_followers(tid)
   print("Action Completed Successfully\n")
   # if more than 100 entries, loop and add results to list, then return
   return li, recent

def following(client, tid, tun, li, recent):
   recent = "following"
   c = client.get_users_following(tid)
   print("Action Completed Successfully\n")
   return li, recent

def follow(client, li):
   for p in (len(li)-1):
      client.follow_list(li(p))
   print("Action Completed Successfully\n")

def unfollow(client, li):
   for p in (len(li)-1):
      client.unfollow_list(li(p))
   print("Action Completed Successfully\n")

def export_list(li, recent):
   recent = "export"
   if recent == "clear":
      print("no data has been grabbed yet\n")
      return recent

   else:
      fn = get_filename()
      fid, fum = dict2stringlist(li)
      print("Exporting " + str(recent) + " data to " + str(fn) + "...\n")

      f = open(fn, 'w')
      for user in fid:
         f.write(user)
      f.close()
      print("Action Completed Successfully\n")
      return recent

def import_list(li, recent):
   recent = "import"
   fn = get_filename()
   if check_filename(fn) == 0:
      return li, recent

   with open(fn, 'r') as f:
      li = f.read()

   # CONVERT TO USABLE DATA

   return li, recent

def clear(li, recent):
   recent = "clear"
   li = []
   return li, recent

def last(recent):
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

def actions(client, li, recent):
   inner = input("What would you like to do (Type 'help' for options): ")
   if inner == "help":
      help()
      return li, recent

   elif inner == "followers":
      tid = get_tid()
      tun = get_tun()
      li, recent = followers(client, tid, tun, li, recent)
      return li, recent

   elif inner == "following":
      tid = get_tid()
      tun = get_tun()
      li, recent = following(client, tid, tun, li, recent)
      return li, recent

   elif inner == "follow":
      if verify():
         follow(client, li)
         return li, recent
      else:
         return li, recent

   elif inner == "unfollow":
      if verify():
         unfollow(client, li)
         return li, recent
      else:
         return li, recent

   elif inner == "export":
      recent = export_list(li, recent)
      return li, recent

   elif inner == "import":
      li, recent = import_list(li, recent)
      return li, recent

   elif inner == "clear":
      li, recent = clear(li, recent)
      return li, recent
   
   elif inner == "last":
      li, recent = last(recent)
      return li, recent

   elif inner == "quit":
      exit(0)

   else:
      print("Invalid input. Check 'help' for valid inputs\n")

# ------------------------------------------------------------------------------

def main():
   bearer_token = initialize()
   global client
   global li
   global recent
   client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

   li = {}
   recent = ""
   while True: # bad form, do not do
      li, recent = actions(client, li, recent)

if __name__=="__main__":
   main()
import sqlite3
import random

from Account import Account
from TerminalColor import Color


def setDatabase() :
   conn = sqlite3.connect('account.db')

   conn.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT
            (ACCOUNT_ID   INT PRIMARY  KEY         NOT NULL,
             USER_ID  TEXT UNIQUE      NOT NULL,
             PASSWORD        TEXT,
             ROLE        TEXT,
             AMOUNT         REAL);''')

   if not userIdExists('Palak') :
      conn.execute("INSERT INTO ACCOUNT (ACCOUNT_ID,USER_ID,PASSWORD,ROLE, AMOUNT) \
            VALUES (1, 'Palak', 'palak', 'Admin', 5000 )")

   if not userIdExists('Navya') :
      conn.execute("INSERT INTO ACCOUNT (ACCOUNT_ID,USER_ID,PASSWORD,ROLE, AMOUNT) \
            VALUES (2, 'Navya', 'navya', 'Admin', 5000 )")


   conn.commit()

   print ( Color.BOLD  + "Records created with two Admins - Palak and Parth :" + Color.END)

   printAllUsers(1)

   conn.close()

def accountExists(account_id) :
   conn = sqlite3.connect('account.db')

   try:
      cursor = conn.execute("SELECT ACCOUNT_ID, USER_ID, PASSWORD, AMOUNT from ACCOUNT WHERE ACCOUNT_ID = '"  + str(account_id) + "'"   )
      for row in cursor:
         return 1
      return 0
   finally:
      conn.close()

def userIdExists(user_id) :
   conn = sqlite3.connect('account.db')
   try:
      query = "SELECT ACCOUNT_ID, USER_ID, PASSWORD, AMOUNT from ACCOUNT WHERE USER_ID = '"  + str(user_id) + "' COLLATE NOCASE"
      cursor = conn.execute(query)
      for row in cursor:
         return 1
      return 0
   finally:
      conn.close()

def deleteAccount(account_id) :
   conn = sqlite3.connect('account.db')

   try:
      if isUserAdmin(account_id):
         print(Color.RED + "\n Admin account cannot be deleted " + Color.END)
      elif not accountExists(account_id) :
         print(Color.RED + "\n Account Id " + str(account_id) + " does not exist!!!" + Color.END)
      else :
         query = "DELETE FROM ACCOUNT WHERE ACCOUNT_ID = '"  + str(account_id) + "'"
         conn.execute(query)
         conn.commit()
         print(Color.RED + "\n Account :" + str(account_id)  + " deleted successfully " + Color.END)
         print (Color.BOLD +  "\nRemaining accounts " + Color.END)
         printAllUsers(0)
   finally:
      conn.close()

def isUserAdmin(account_id) :
   conn = sqlite3.connect('account.db')
   try:
      query = "SELECT ACCOUNT_ID, USER_ID, PASSWORD, AMOUNT from ACCOUNT WHERE ACCOUNT_ID = '"  + str(account_id) + "' AND ROLE = 'Admin'"
      cursor = conn.execute(query)
      for row in cursor:
         return 1
      return 0
   finally:
      conn.close()

def validatePassword(account_id, password) :
   conn = sqlite3.connect('account.db')

   try:
      cursor = conn.execute("SELECT ACCOUNT_ID, USER_ID, PASSWORD, ROLE, AMOUNT from ACCOUNT WHERE ACCOUNT_ID = " + account_id  + " AND PASSWORD = '" + str(password) + "'")

      for row in cursor:
         return Account(row[0], row[1], row[2], row[3], row[4])
      return None;
   finally:
      conn.close()

def updateAccount(account) :
   conn = sqlite3.connect('account.db')
   conn.execute("UPDATE ACCOUNT set AMOUNT = " + str(account.amount) + " where ACCOUNT_ID = "+ str(account.account_id));
   conn.commit()
   conn.close()

def updatePassword(account) :
   conn = sqlite3.connect('account.db')
   conn.execute("UPDATE ACCOUNT set PASSWORD = '" + str(account.password) + "' where ACCOUNT_ID = "+ str(account.account_id));
   conn.commit()
   conn.close()

def addAccount(account) :
   conn = sqlite3.connect('account.db')
   accountid = random.randint(1000, 9999)

   while accountExists(accountid):
      accountid = random.randint(1000, 9999)

   account.account_id = accountid
   query = "INSERT INTO ACCOUNT (ACCOUNT_ID,USER_ID,PASSWORD,ROLE, AMOUNT) \
         VALUES (" + \
                "'" + str(account.account_id) + "'" + "," + \
                "'" + account.user_id  + "'" +   "," + \
                "'" + account.password  + "'"  + "," + \
                "'" + account.admin + "'" + "," + \
                account.amount + ")"
   conn.execute(query)
   conn.commit()


   try:
      print (Color.BOLD +  "\nAccount added - please remember your account id" + Color.END)
      cursor = conn.execute("SELECT ACCOUNT_ID, USER_ID, PASSWORD, ROLE, AMOUNT from ACCOUNT WHERE ACCOUNT_ID = " + str(accountid)  )
      for row in cursor:
         print ("ACCOUNT_ID = ", row[0])
         print ("USER_ID = ", row[1])
         print ("PASSWORD = ", row[2])
         print("ROLE = ", row[3])
         print ("AMOUNT = ", row[4], "\n")
      return account;
   finally:
      conn.close()

def printAllUsers(withPasswordAndAmount):
   conn = sqlite3.connect('account.db')

   try:
      cursor = conn.execute(
         "SELECT ACCOUNT_ID, USER_ID, PASSWORD, ROLE, AMOUNT from ACCOUNT")
      for row in cursor:
         print("ACCOUNT_ID = ", row[0])
         print("USER_ID = ", row[1])
         print("ROLE = ", row[3])

         if withPasswordAndAmount:
            print("PASSWORD = ", row[2])
            print("AMOUNT = ", row[4])
         print("\n")
   finally:
      conn.close()

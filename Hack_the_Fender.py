'''
Mission: Defeat The Fender
Plan of Attack (POA): Encode file containing stolen passwords
Agent: Hypo_Mac-1109
'''
import csv
import json

# this list will contain the names of users whose paswords have been compromised
compromised_users = []

# open stolen password file
with open('passwords.csv') as password_file:
  # parse object holder using csv reader and save parsed result
  password_csv = csv.DictReader(password_file)
  # iterate through each line and save results in temp var
  for row in password_csv:
    password_row = row
    # add each username to our compromised user list
    compromised_users.append(password_row['Username'])


# create fake password file
with open('compromised_users.txt', 'w') as compromised_user_file:
  # write compromised usernames to the new file
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)


# open new json file in write-mode to send mission status update to Headquarters
with open('boss_message.json', 'w') as boss_message:
  # create a dict to relay message
  boss_message_dict = {'recipient':'The Boss', 'message':'Mission Success'}
  json.dump(boss_message_dict, boss_message)

'''
  Scramble the Password
  Steps:
  1. Remove the enemy's password file completely.
  2. Incriminate Slash Null
'''
slash_null_sig = ''' _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/'''
with open('new_passwords.csv', 'w') as new_passwords_obj:
  new_passwords_obj.writelines(slash_null_sig)

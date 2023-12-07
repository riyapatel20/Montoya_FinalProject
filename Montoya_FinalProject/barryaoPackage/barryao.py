# Name: Aissatou Barry
# email: barryao@mail.uc.edu
# Assignment Title: Final Exam
# Due Date: 12/7/23
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that team Montoya has successfully decrypted the scavenger hunt code.
# Citations:
# Line 21 - https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
# Anything else that's relevant: N/A


import json


def decrypt_movie_title(fernet_key, encrypted_message_file):
   '''
   This function decrypts the movie title for Montoya.
   '''
   with open(encrypted_message_file, 'r') as file:
       encrypted_data = json.load(file)["Montoya"][0]


   decrypted_message = fernet_key.decrypt(encrypted_data.encode())
   return decrypted_message.decode()

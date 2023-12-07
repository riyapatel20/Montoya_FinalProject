# Name: Riya Patel
# email: patel5ry@mail.uc.edu
# Assignment Title: Final Exam
# Due Date: 12/7/23
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that team Montoya has successfully decrypted the scavenger hunt code.
# Citations: N/A
# Anything else that's relevant: N/A


from barryaoPackage.barryao import *
from kanoutmaPackage.kanoutma import *
from albessaaaPackage.albessaaa import *


# Montoya: Location Hint
if __name__ == "__main__":
   encrypted_location_data = ["30942", "42547", "19312", "65919", "8879", "36488", "2756", "45854", "18755", "28894", "8018", "2756", "24979", "42636"]
   english_file_path = 'english-2.txt'
   decrypted_location = decrypt_location(encrypted_location_data, english_file_path)
   print(f"Decrypted Location: {decrypted_location}")


# Montoya: Movie Title
from cryptography.fernet import Fernet


if __name__ == "__main__":
   encrypted_message_file = "TeamsAndEncryptedMessagesForDistribution.json"
   decryption_key = 'LMV69IGGTp2Gyn4TI-DTuupf0VvugeC5API5dpeoiqM='
   fernet_key = Fernet(decryption_key)
   decrypted_movie = decrypt_movie_title(fernet_key, encrypted_message_file)
   print(f"Movie Title:", decrypted_movie)
  
# Photo at the Montoya location with a quote from the Montoya movie.
if __name__ == "__main__":
   photo_path = "Final Photo.jpg"
   display_photo(photo_path)

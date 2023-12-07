# Name: Mahamadou Kanoute
# email: kanoutma@mail.uc.edu
# Assignment Title: Final Exam
# Due Date: 12/7/23
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that team Montoya has successfully decrypted the scavenger hunt code.
# Citations:
# Lines 18 & 19 - https://www.tutorialspoint.com/python_pillow/python_pillow_using_image_module.htm
# Anything else that's relevant: N/A


from PIL import Image


def display_photo(photo_path):
   '''
   This function displays the photo at the decrypted location and a quote from    the decrypted movie title.
   '''
   img = Image.open(photo_path)
   img.show()
# Name: Ana Albesa
# email: albesaaa@mail.uc.edu
# Assignment Title: Final Exam
# Due Date: 12/7/23
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that team Montoya has successfully decrypted the scavenger hunt code.
# Citations:
# Line 16 - https://stackoverflow.com/questions/59422448/with-file-openr-encoding-utf-8-as-f-attributeerror-str-object-has-no-a
# Anything else that's relevant: N/A


def decrypt_location(encrypted_location_data, english_file_path):
    '''
    This function decrypts the location data for Montoya.
    '''
    with open(english_file_path, 'r', encoding='utf-8') as file:
        english_lines = file.readlines()
        
    decrypted_location = ''
    for index in encrypted_location_data:
        decrypted_location += english_lines[int(index)].strip()
        
    return decrypted_location
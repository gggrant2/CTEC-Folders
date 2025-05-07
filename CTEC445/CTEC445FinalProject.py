#Genesis Grant
#CTEC 445: Secure Password Generation and Multi-Factor Authentication (MFA) Final Programming Project

#Importing libraries
import secrets
import string
import re
import time


##Password Generation
def password_generation(length = 12):
#Characters takes classes from string module for password creation use
    characters = string.ascii_letters + string.digits + string.punctuation
#Password function takes one character, 12x to create random password
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


##Password Strength Verification
def password_verification(password):
    #Check password criteria
    #Use re library to search for characters in password
    length_check = len(password) == 12
    uppercase_check = re.search(r'[A-Z]', password)
    lowercase_check = re.search(r'[a-z]', password)
    digits_check = re.search(r'\d', password)
    specialcharacters_check = re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/]', password)

    #Evaluate which criteria is met and present strength check
    if all([length_check, uppercase_check, lowercase_check, digits_check, specialcharacters_check]):
        return "Strong "
    elif length_check and (uppercase_check or lowercase_check) and (digits_check or specialcharacters_check):
        return "Moderate"
    else:
        return "Weak"

##Generating OTP
def generate_otp():
    otp = ''.join(secrets.choice(string.digits) for _ in range(6))  # 6-digit OTP
    return otp

##Verifying OTP & timestamp
def verify_otp(generate_otp, timeout=60):
    print("Your OTP is: ", (generate_otp))

    #Store start time variable
    start_time = time.time()
    user_input = input("Enter the OTP: ")

    #Check if OTP is correct and within the time limit
    if user_input == generate_otp and time.time() - start_time <= timeout:
        return "OTP Verified Successfully!"
    else:
        return "OTP Verification Failed (Invalid or Expired)."



print('\nWelcome to my CTEC 445 Final Programming Project')

password = password_generation()
print('Your password is:', password)

verify = password_verification(password)
print("Your password's strength was:", verify)

otp = generate_otp()

result = verify_otp(otp)
    #(result)


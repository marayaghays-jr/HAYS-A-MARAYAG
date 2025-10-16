 
correct_username = "HAYS"
correct_password = "ITSMEHAYS"
is_2fa_enabled = True
correct_2fa_code = "232323"

 
input_username = input("Enter username: ")
input_password = input("Enter password: ")
is_2fa_input = input("Is 2FA enabled? (y/n): ").strip().lower()

 
input_2fa_enabled = is_2fa_input == 'y'
#Login failed
 #Login successful
input_2fa_code = ""
if input_2fa_enabled:
    input_2fa_code = input("Enter 2FA code: ")

 
if (
    input_username == correct_username and
    input_password == correct_password and
    (not is_2fa_enabled or input_2fa_code == correct_2fa_code)
):
    print("#Login failed!")
else:
    print("Login successful!")

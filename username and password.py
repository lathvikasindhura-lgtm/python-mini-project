
print("===== USERNAME AND PASSWORD CREATION =====")

username = input("Enter your username: ")
password = input("Create your password: ")

if len(password) < 8:
    print("Password must contain at least 8 characters.")

elif not any(ch.isupper() for ch in password):
    print("Password must contain at least one uppercase letter.")

elif not any(ch.islower() for ch in password):
    print("Password must contain at least one lowercase letter.")

elif not any(ch.isdigit() for ch in password):
    print("Password must contain at least one digit.")

elif not any(not ch.isalnum() for ch in password):
    print("Password must contain at least one special character.")

else:
    print("\nAccount Created Successfully!")
    print("Username:", username)
    print("Password meets all specifications.")
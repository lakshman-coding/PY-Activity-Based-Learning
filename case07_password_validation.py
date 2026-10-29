password = input("Enter password: ")
failures = []
uppercase = False
lowercase = False
digit = False
special = False

if len(password) < 8:
    failures.append("minimum length is 8")

for character in password:
    if character >= "A" and character <= "Z":
        uppercase = True
    elif character >= "a" and character <= "z":
        lowercase = True
    elif character >= "0" and character <= "9":
        digit = True
    else:
        special = True

if uppercase == False:
    failures.append("one uppercase letter is required")
if lowercase == False:
    failures.append("one lowercase letter is required")
if digit == False:
    failures.append("one digit is required")
if special == False:
    failures.append("one special character is required")

for i in range(len(password) - 2):
    if password[i] == password[i + 1] and password[i] == password[i + 2]:
        failures.append("three consecutive repeated characters are not allowed")
        break

prohibited = ("password", "admin")
for word in prohibited:
    if word in password.lower():
        failures.append("prohibited word found: " + word)

if len(failures) == 0:
    print("Password is valid")
else:
    print("Password is invalid because:")
    for failure in failures:
        print("-", failure)

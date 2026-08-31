import random

print("*** WELCOME TO PASSWORD GENERATOR ***")
print("Help us to customize password you like!\n")

pass_len=int(input("Please enter password length you like: "))
while pass_len<=0:
  pass_len=int(input("Please enter correct password length you like: "))

upper_case=input("Should it include uppercase characters, enter yes or no : ").lower()
while upper_case not in ("yes","no"):
  upper_case=input("INVALID INPUT!\nShould it include uppercase characters? Enter only yes or no : ").lower()

lower_case=input("Should it include lowercase characters, enter yes or no : ").lower()
while lower_case not in ("yes","no"):
  lower_case=input("INVALID INPUT!\nShould it include lowercase characters? Enter only yes or no : ").lower()

num=input("Should it include numbers, enter yes or no : ").lower()
while num not in ("yes","no"):
  num=input("INVALID INPUT!\nShould it include numbers? Enter only yes or no : ").lower()

special=input("Should it include special characters, enter yes or no : ").lower()
while special not in ("yes","no"):
  special=input("INVALID INPUT!\nShould it include special character? Enter only yes or no : ").lower()

#Making characters pool
characters=""

if upper_case=="yes":
  characters+= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if lower_case == "yes":
    characters += "abcdefghijklmnopqrstuvwxyz"

if num == "yes":
    characters += "0123456789"

if special == "yes":
    characters += "!@#$%^&*"
    
if upper_case == "no" and lower_case == "no" and num == "no" and special == "no":
    print("Password must have at least one requirement allowed")
else:
  password="".join(random.choices(characters,k=pass_len))
print(f"\nPassword Suggestion: {password}")
        
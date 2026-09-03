import random
import string 


#User input function
def yes_no_input(message):

    answer = input(message).lower()

    while answer not in ("yes", "no"):
        answer = input("INVALID INPUT!\nPlease enter yes or no: ").lower()

    return answer
#password length
def pass_length():
  while True:
    try:
      pass_len=int(input("Please enter password length you like: "))
      if pass_len>0:
        return pass_len
      else:
        print("Password length should be greater than 0")
      
    except ValueError as e:
      print("Please enter a valid number.") 
      

#Making characters pool
def char_pool(upper_case,lower_case,num,special):
  characters=""
  
  if upper_case=="yes":
    characters+= string.ascii_uppercase

  if lower_case == "yes":
      characters += string.ascii_lowercase

  if num == "yes":
      characters += string.digits

  if special == "yes":
      characters += string.punctuation
  return characters
       
  

print("*** WELCOME TO PASSWORD GENERATOR ***")
print("Help us to customize password you like!\n")     
pass_len=pass_length()   
while True:
  upper_case=yes_no_input("Should it include uppercase characters, enter yes or no : ")
  lower_case=yes_no_input("Should it include lowercase characters? Enter yes or no : ")
  num=yes_no_input("Should it include numbers, enter yes or no : ")
  special=yes_no_input("Should it include special characters, enter yes or no : ")
  characters=char_pool(upper_case,lower_case,num,special)
  if characters:
    break
  else:
     print("Password must have at least one requirement allowed.")

password="".join(random.choices(characters,k=pass_len))
print(f"\nPassword Suggestion: {password}")

import random
import array

length_of_password= 12
#length_of_password is used to define the length of password...
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lowercase= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

uppercase= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

special_character= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

combined_list=numbers+ lowercase + uppercase + special_character

random_digit = random.choice(numbers)
random_upper = random.choice(uppercase)
random_lower = random.choice(lowercase)
random_symbol = random.choice(special_character)

temp_pass = random_digit + random_upper + random_lower + random_symbol

for x in range(length_of_password - 4):
	temp_pass = temp_pass + random.choice(combined_list)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
		
print(password)

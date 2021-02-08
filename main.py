import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Consting the names
len_names = len(names)

#Choosing the random person
random_person = random.randint(0, len_names - 1)

#Resolution 
print("Result is: \n")
print(f"{names[random_person]} will pay the bill today. Good luck {names[random_person]}. xD")




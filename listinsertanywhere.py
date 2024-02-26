#Write a program in python to enter a valid string at any position in a list

sent1 = ['Call', 'me', 'Ishmael', '.']
print("Enter the position where you want to enter the string")
position=int(input())
print("Enter the string")
string=str(input())
sent1.insert(position,string)
print("The updated list is")
print(sent1)
# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

a = {
    'khao' : 'eat',
    'soo' : 'sleep',
    'roo' : 'cry',
}
word = input("enter a hindi word: ")
if word in a:
    print("translation is", a[word])
else:
    print("no word found")
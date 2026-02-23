'''You need to write a program that can translate a normal English message into a secret code language and also decode it back.
The program should ask the user whether they want to encode or decode a message.
The program works word by word (so multi-word sentences are supported).

Rules for Encoding
If the word has 3 or more letters:
Take the first letter and move it to the end
Then add 3 random characters at the start and 3 at the end
If the word has less than 3 letters:
Just reverse the word

Rules for Decoding
If the word has less than 3 letters:
Just reverse it
If the word has 3 or more letters:
Remove the first 3 and last 3 characters (these were random letters)
Take the last letter and move it to the beginning'''

import random
import string

def add_random_chars(word):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(3)) + word + ''.join(random.choice(chars) for _ in range(3))

def remove_random_chars(word):
    return word[3:-3]  # remove first 3 and last 3

# Encode function
def encode(word):
    if len(word) >= 3:
        word = word[1:] + word[0]   # move first letter to end
        word = add_random_chars(word)
    else:
        word = word[::-1]           # reverse small words
    return word

# Decode function
def decode(word):
    if len(word) < 6:               # small words (less than 3 letters, plus no random chars)
        word = word[::-1]
    else:
        word = remove_random_chars(word)  # remove random chars
        word = word[-1] + word[:-1]      # move last letter to start
    return word

# Main
choice = input("Do you want to encode or decode? ").lower()
message = input("Enter your text: ")
words = message.split()

result = []
for w in words:
    if choice == "encode":
        result.append(encode(w))
    elif choice == "decode":
        result.append(decode(w))
    else:
        print("Invalid choice!")
        exit()

print("Result:", ' '.join(result))
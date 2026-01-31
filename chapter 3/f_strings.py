# non convenience method
sentence = "Hi my name is {} I am from {}"
name = "Ananya"
Country = "India"
print(sentence.format(name,Country))

# f-string method
print(f"Hi my name is {name} I am from {Country}")

# txt
price = 49.08754
print(f"for only {price: .2f} dollars!")

# by format method
txt = "for only {price: .2f} dollars!"
print(txt.format(price = 49))

# next eg
print(f"{2*30}")
print(type(f"{2*30}"))
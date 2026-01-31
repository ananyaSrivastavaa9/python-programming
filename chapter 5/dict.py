dict = {
    220 : "Priya",
    560 : "Ananya",
    698 : "Minal"
}
print(dict[560])

info = {'name' : 'Ananya', 'age' : 18, 'eligible' : True}
print(info)

# accessing single values
print(info['name'])
print(info.get('name'))

# accessing multiple values : keys
print(info.keys())
for key in info.keys():
    print(info[key])

# accessing multiple values : values
print(info.values())

# by using f string
print(info.keys())
for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")

# accessing key value pairs
print(info.items())
for key, value in info.items():
    print(f"the value corresponding to the key {key} is {value}")

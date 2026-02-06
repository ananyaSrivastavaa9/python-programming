# for uppercase characters
a = "ananya"
print(a.upper())

# for lowercase characters
b = "ANANYA"
print(b.lower())

# to remove white spaces
c = " ananya srivastava   "
print(c.strip())

# to remove trailing data
d = "Ananya...."
print(d.rstrip("."))

# to replace one string with another
e = "ananya"
print(e.replace("ananya", "gracy"))

# to separate the strings
f = "ananya srivastava btech cse AIML"
print(f.split(" "))

# to capitalize first char of string
g = "welcome home"
print(g.capitalize())

# to centeralize the string
h = "ananya"
print(h.center(75))

# to count the number of repeated words
i = "Ananya is a student Ananya works hard"
print(i.count("Ananya"))

# to check if the string ends with given value
j = "ananya!!"
print(j.endswith("!!"))

# to find the string
k = "ananya why are u so late?"
print(k.find("are"))

# index
l = "why so good?"
print(l.index("so"))

# string is alphanumeric or not
m = "Welcomeananyaa"
print(m.isalnum())

# isalpha()
n = "2ananya"
print(n.isalpha())

# islower()
o = "ananya"
print(o.islower())

# isprintable()
p = "ananya said ok\n"
print(p)
print(p.isprintable())

# isspace()
q = "             "
print(q.isspace())

# istitle()
r = "Ananya Said"
print(r.istitle())

# startswith()
s = "python is good"
print(s.startswith("python"))

# swapcase()
t = "python aIs ia very Good laNGuage"
print(t.swapcase())

# title()
u = "ananya is a very good girl she used to watch movie"
print(u.title())
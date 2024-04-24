"""string related functions"""

OG_STRING = "panda"
print(OG_STRING.title())
print(OG_STRING.lower())
print(OG_STRING.upper())

# + is can be used for concatenation
print(OG_STRING + " is me")
OG_STRING = "  " + OG_STRING + " "

# functions for striping whitespaces
print(OG_STRING.rstrip())
print(OG_STRING.lstrip())

print("\t" + OG_STRING + "\n" + "hey" + "\r")

# type casting to string
print(str(1.2))

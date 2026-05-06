#string is a sequence of characters.
#It is immutable.

name = "krish"

print(name[0]) #output: k
print(name[1]) #output: r
print(name[2]) #output: i
print(name[3]) #output: s
print(name[4]) #output: h
print(name[-1]) #output: h
print(name[-2]) #output: s
print(name[0:3]) #output: kri
print(name[1:]) #output: rish
print(name[:3]) #output: kri
print(name[:4]) #output: kris
print(name[::2]) #output: krs
print(name[1::2]) #output: rih
print(name[::-1]) #output: hsi rk
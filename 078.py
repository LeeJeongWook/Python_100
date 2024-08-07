code = input()
encoding = ""
for i in code:
    encoding += chr(ord(i)+3)
print(encoding)
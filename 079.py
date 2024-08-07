sentence = input()
result = ""
for i in sentence:
    if 97 <= ord(i) < 123:
        result += chr(ord(i)-32)
    elif 65 <= ord(i) < 91:
        result += chr(ord(i)+32)
    else:
        result += i
print(result)
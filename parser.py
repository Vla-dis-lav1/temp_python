file = open("D:\\lang.txt", "r")

data = file.read()
readBracket = False
string = ""
token_list = []
token_list_temp = []
counter = 0
token = ""
startTokenWrite = False
start = 0
escape_way = False
while counter < len(data):

    i = data[counter]
    separators = ""
    # 0
    separators += " "
    separators += "\n"
    separators += "="
    separators += "\""
    separators += "\'"
    # 5
    separators += "("
    separators += ")"
    separators += "["
    separators += "]"
    separators += "{"
    # 10
    separators += "}"
    separators += "."
    separators += ","
    separators += "+"
    separators += "-"
    # 15
    separators += "*"
    separators += "/"
    separators += "\\"

    for i2 in separators:
        if i == i2:
            startTokenWrite = True
            if i == "\\":
                escape_way = True
            break
        else:
            startTokenWrite = False

    if startTokenWrite:
        if len(token) > 0:
            token_list_temp.append(token)
            token = ""
        if escape_way:
            counter += 1
            i += str(data[counter])
            escape_way = False
        token_list_temp.append(i)
    else:
        token += i

    counter += 1
if len(token) > 0:
    token_list_temp.append(token)
    token = ""

print(token_list_temp)

counter = 0
token_list_temp2 = []
while counter < len(token_list_temp):
    i = token_list_temp[counter]
    if i == "\\n":
        i = "\n"
    elif i == "\\t":
        i = "\t"
    elif i == "\\\\":
        i = "\\"
    elif i == "\\\"":
        i = "\""
    elif i == "\\\'":
        i = "\'"
    token_list_temp2.append(i)
    counter += 1
print(token_list_temp2)
token_list_temp = token_list_temp2

counter = 0
startTokenWrite = False
token_list = []
string = ""
while counter < len(token_list_temp):
    i = token_list_temp[counter]
    if i == "\"":
        if startTokenWrite:
            startTokenWrite = False
        else:
            startTokenWrite = True
        print(startTokenWrite)
    if startTokenWrite:
        string += i
    else:
        if len(string) == 0:
            token_list.append(i)
        if len(string) > 0:
            string += i
            token_list.append(string)
            string = ""
    counter += 1
print(token_list)

counter = 0
token_list_temp = []
startTokenWrite = False
string = ""
for i in token_list:
    if i == " ":
        startTokenWrite = True
    else:
        if startTokenWrite:
            token_list_temp.append(string)
            string = ""
            startTokenWrite = False
        token_list_temp.append(i)
    if startTokenWrite:
        string += i
if len(string) > 0:
    token_list_temp.append(string)
print(token_list_temp)

token_list_result = token_list_temp
line = []
read = True
for i in token_list_result:
    if i == "\n":
        read = False
    if read:
        line.append(i)
print(line)

file.close()

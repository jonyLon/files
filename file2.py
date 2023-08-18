marks = '.,?!_-&():""'
def removePunct(line, marks=marks):
    str_ = ''
    for ch in line:
        if ch not in marks:
            str_ += ch
    return str_

def writeFile(fname, newText):
    with open(fname,"w") as file:
        file.write(newText)

def readFile(fname):
    with open(fname) as file:
        return file.read()
    
# 1
# text = readFile("text.txt")
# textWithoutPunct = removePunct(text)
# list = textWithoutPunct.split()
# filtredList = []
# for i in list:
#     if len(i) >= 7:
#         filtredList.append(i)
# filtredText = " ".join(filtredList)
# writeFile("filtred.txt", filtredText)

def readFileLines(fname):
    with open(fname) as file:
        return file.readlines()
    
# 2
# lines = "".join(readFileLines("text.txt"))
# writeFile('lines.txt', lines)
# 3
# lines2 = "".join(readFileLines("text.txt")[::-1])
# writeFile('lines2.txt', lines2)
# 4
# list = readFileLines("text.txt")[::-1]
# newList = []
# firstLineWithOutCommas = False
# for i in list:
#     if i.count(",") == 0 and not firstLineWithOutCommas:
#         firstLineWithOutCommas = True
#         newList.append(i.replace(' \n','************\n'))
#     else:
#         newList.append(i)
# newText = "".join(newList[::-1])
# writeFile("edited.txt",newText)
# 5
# symbol = input("Enter symbol: ")
# text = readFile("text.txt")
# textWithoutPunct = removePunct(text)
# list = textWithoutPunct.split()
# count = 0
# for i in list:
#     if i.find(symbol) == 0:
#         count+=1
# print(f"There are {count} words which start with {symbol}")
# 6
def changeSymbol(readFile,writeInFile,firstSym,secondSym):
    list = readFileLines(readFile)
    modifiedList = []
    for i in list:
        if i.find(firstSym) != -1:
            modifiedList.append(i.replace(firstSym,secondSym))
        else:
            modifiedList.append(i)
    line = "".join(modifiedList)
    writeFile(writeInFile, line)
# changeSymbol("edited.txt","modified.txt","*","&")
# changeSymbol("modified.txt","modified2.txt","&","*")

# 7,8
def writeFileAdd(fname, newText):
    with open(fname,"a") as file:
        file.write(newText)
rows = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Nunc quis enim suscipit, iaculis nisl vitae, eleifend elit.",
    "Donec non sapien a justo ultricies consequat.",
    "Praesent at leo varius, pulvinar ipsum sit amet, lobortis mi.",
    "Cras efficitur mi volutpat velit sodales suscipit.",
    "Ut tincidunt risus sit amet massa dignissim, vel semper sem pellentesque."
]
# for i in rows:
#     writeFileAdd('rows.txt',i+"\n")
# 9

countSym = len(readFile("text.txt"))
print(f"{countSym} symbols in this file")

countRows = len(readFileLines("text.txt"))
print(f"{countRows} rows in this file")
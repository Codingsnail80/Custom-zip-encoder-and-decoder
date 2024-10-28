#note that this currently only works if there are no enters in the text doccumant. 
#In other words it has to all be on the same line in a .txt file

#selecting and opening the file
selected = input('filename/path:')
file1 = open(file=selected)

file = file1.read()
commonPhrase = ''


#add to a list for better navigation
fileList=[]
for letter in file:
    fileList.append(letter)

#iterating over the open text file in list form
tempWord=''
isFirstTime=True

spaceCount=0

wordsList = []
for i in range(len(fileList)):
    if isFirstTime:
        tempWord += fileList[i]
        isFirstTime=False
    else:
        if fileList[i] == ' ':
            spaceCount+=1
            wordsList.append(tempWord)
            tempWord=''
        else:
            tempWord += fileList[i]
    if i == len(fileList)-1:
        wordsList.append(tempWord)


finalCommonList=[]

for i in range(len(wordsList)):
    canChange=True
    check=wordsList[i]
    for i2 in range(i+1, len(wordsList)):
        if check == wordsList[i2] and canChange==True:
            canChange=False
    if canChange==False:
        finalCommonList.append(check)


print('finalCommonList:'+ str(finalCommonList))

#excludes a and i beccuse they ccould appeare individualy in a sentance naturally
usalbleSymbols=['b','c','d','e','f','g','h','j','k', 'l','m','n','o','p', 'q', 'r', 's', 't','u','v','w','x','y','z']

dictionary=[]

count=0
tempCheck=''

#removes duplicates of finalcommonList and assigns them to the variable dictionary
dictionary=set(finalCommonList)
dictionary=list(dictionary)
print(dictionary)

#makes a new list of placeholders apropriae to the length of repeated words
tempUsableSymbols=[]
for i in range(len(dictionary)):
    try:
        tempUsableSymbols.append(usalbleSymbols[i])
    except:
        print('cannot compress, to many common words. only supports 24 common words\ndo not expect the output to be accurate or work')
print(tempUsableSymbols)

#mannagees getting the file name of the file you are converting without the file extention
#and stores it in the variable fileNameOutput
tempFileNameOutput=[]
fileNameOutput=''

for letter in selected:
    tempFileNameOutput.append(letter)

for i in range(len(tempFileNameOutput)):
    if tempFileNameOutput[i]!='.':
        fileNameOutput+=tempFileNameOutput[i]
    else:
        break

print(fileNameOutput)

#handels the creation of the new files
finalFileName=fileNameOutput + '.Dzip'
DctnryName= fileNameOutput + '.DzDctnry'

try:
    zipped = open(finalFileName,'x')
    dic = open(DctnryName,'x')
except:
    answer = input('file already exists, do you want to continue? y/n:')
    if answer=='y':
        zipped = open(finalFileName,'w')
        dic = open(DctnryName,'w')
    else:
        print('Exiting, expect an error. No harm will be done to your files')


#replacing the repeated words with the symbols
newZipString=''
for i in range(len(dictionary)):
    for i2 in range(len(wordsList)):
        if dictionary[i]==wordsList[i2]:
            wordsList.pop(i2)
            wordsList.insert(i2, tempUsableSymbols[i])

#writing the new string to the new Dzip file
for word in wordsList:
    newZipString+=word+' '
print(newZipString)

zipped.write(newZipString)

#writting the dictionary file as two strings of the neccesary lists. Converted to string to save space
line1=''
line2=''
for word in tempUsableSymbols:
    line1 += word + ' '

for word in dictionary:
    line2 += word + ' '

dicString=line1 + '\n' + line2

dic.write(dicString)

print('***IMPORTANT NOTE: KEEP BOTH THE .Dzip AND THE .DzDctnry FILE BOTH ARE IMPORTANT FOR UNZIPPING***')
zipped.close()
dic.close()
file1.close()
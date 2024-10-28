#getting file name without extention for extracting the files
fileName = input('what is the name of the file, without the file extention (also make sure the DzDctnry is in the same directory and has the same name):')
zipFileName = fileName + '.Dzip'
dicFileName = fileName + '.DzDctnry'

#opening the files and reeading them
zipFileOpen=open(zipFileName)
dicFileOpen=open(dicFileName)
zipFile = zipFileOpen.read()
dicFile = dicFileOpen.read()


#adding letters/sybols to a list for better navigation
zipList=[]
dicList1=[]
dicList2=[]

#zip list of letters
for letter in zipFile:
    zipList.append(letter)

indexOfBreak=0
#first line of letters in dictionary
for i in range(len(dicFile)):
    if dicFile[i] != '\n':
        dicList1.append(dicFile[i])
    else:
        indexOfBreak=i
        break

#second line of letters
hasHitEnter=False
for i in range(indexOfBreak+1, len(dicFile)):
    dicList2.append(dicFile[i])


#makeing the wordLists from the letter lists

#zipList first
tempWord=''
isFirstTime=True
spaceCount=0
zipWordsList = []
for i in range(len(zipList)):
    if isFirstTime:
        tempWord += zipList[i]
        isFirstTime=False
    else:
        if zipList[i] == ' ':
            spaceCount+=1
            zipWordsList.append(tempWord)
            tempWord=''
        else:
            tempWord += zipList[i]
    if i == len(zipList)-1:
        zipWordsList.append(tempWord)
zipWordsList.pop()

print(zipWordsList)

#first dictionary line
tempWord=''
isFirstTime=True
spaceCount=0
dicLine1 = []
for i in range(len(dicList1)):
    if isFirstTime:
        tempWord += dicList1[i]
        isFirstTime=False
    else:
        if dicList1[i] == ' ':
            spaceCount+=1
            dicLine1.append(tempWord)
            tempWord=''
        else:
            tempWord += dicList1[i]
    if i == len(dicList1)-1:
        dicLine1.append(tempWord)
dicLine1.pop() #gets rid of the extra space at the end of the list

print(dicLine1)

#dictionary line 2 words
tempWord=''
isFirstTime=True
spaceCount=0
dicLine2 = []
for i in range(len(dicList2)):
    if isFirstTime:
        tempWord += dicList2[i]
        isFirstTime=False
    else:
        if dicList2[i] == ' ':
            spaceCount+=1
            dicLine2.append(tempWord)
            tempWord=''
        else:
            tempWord += dicList2[i]
    if i == len(dicList2)-1:
        dicLine2.append(tempWord)
dicLine2.pop() #gets rid of the extra space at teh end of the list

print(dicLine2)


#decoding by looking for the symbols (from dictionary line 1) in the zipped words list and if it finds one
#it will replace it with the real word of the corresponding index in the dictionary line 2
decodedList=zipWordsList
for i in range(len(dicLine1)):
    check=dicLine1[i]
    for i2 in range(len(decodedList)):
        if decodedList[i2]==check:
            decodedList[i2]=dicLine2[i]

print()
print(decodedList)


#makeing the decoded list into a string so that we can write it to a file.
#Also I made it so that it doesn't add an extra space to the end of the file.
decodedString=''
for i in range(len(decodedList)):
    if i != len(decodedList)-1:
        decodedString+=decodedList[i] + ' '
    else:
        decodedString+=decodedList[i]
print(decodedString)

#Creating the actual file and asking the user for a name for it
newFileName = input('What do you want the name of your unziped file to be(without file extention):')
try:
    generatedFile=open(newFileName + '.txt', 'x')
except:
    answer = input('File already exists, do you want to continue? y/n:')
    if answer=='y':
        generatedFile=open(newFileName + '.txt', 'w')
    else:
        print('Exiting, expect an error. No harm will be done to your files')

generatedFile.write(decodedString)

#closing files
generatedFile.close()
zipFileOpen.close()
dicFileOpen.close()
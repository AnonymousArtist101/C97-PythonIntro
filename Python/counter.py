counter=input("type an sentence here:")
print(counter)

characterCount=0

wordCount=1

for i in counter:
    characterCount=characterCount+1
  
    if i==" ":
        wordCount=wordCount+1

print(characterCount)
print(wordCount)
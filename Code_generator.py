"""Beginner:
Create a "Code" Generator that takes text as input and replaces each letter
with another letter, and outputs the "encoded" message.
Intermediate:
Build an Upgraded Code Generator. Starting with the project mentioned in the
beginner section, see what you can do to make it more sophisticated.
Can you make it generate different kinds of codes.
Can you create a "decoder" app that reads encoded messages if the user inputs
a secret key? Can you create a more sophisticated code that goes beyond simple letter-replacement?"""

alphabet=['01','0','1','2','3', '4', '5', '6', '7', '8', '9', ' ','a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', ',',
'^', '_', '{', '|', '}', '~', ',', '\t', '\n', '\r', '\x0b', '\x0c', '`']

text=input("Please type or paste the text to be coded > ")
ltext=text.lower()
length=len(text)
inalist=[]
letter_alph=[]
for i in range(0, length):
    a=ltext[i]
    if a in alphabet:
        # first find the index of each string of text in alphabet list
        ina=alphabet.index(a)
        # then replace that index with index+1 in alphabet list, Coding Method
        ina=ina+1
        # then add that new index corresponding letter to a list
        inalist.append(ina)
        bbb=alphabet[ina]
        letter_alph.append(bbb)
    else:
        continue
#then join the strings in the list/strip to form words
joined=''.join(letter_alph)
print(f"The coded text is: {joined}")


#decoder
textcod=input("Please type or paste the coded text to be decoded > ")
ltextcod=textcod.lower()

listj=[]
listfj=[]
for j in ltextcod:
    #decoding Method
    find_indexj=alphabet.index(j)-1
    listj.append(j)
    listfj.append(find_indexj)

inverse=[]
for k in listfj:
    inverse.append(alphabet[k])

joinedcod=''.join(inverse)
print(f"The decoded message is: {joinedcod}")
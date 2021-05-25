"""Beginner:
Create a "Code" Generator that takes text as input and replaces each letter
with another letter, and outputs the "encoded" message.
Intermediate:
Build an Upgraded Code Generator. Starting with the project mentioned in the
beginner section, see what you can do to make it more sophisticated.
Can you make it generate different kinds of codes.
Can you create a "decoder" app that reads encoded messages if the user inputs
a secret key? Can you create a more sophisticated code that goes beyond simple letter-replacement?"""

alphabet=['0','1','2','3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'az']
text=input("Please type or paste the text > ")
ltext=text.lower()
length=len(text)
find_index=text.find("e")
find_index_in_alph=alphabet.index("e")
inalist=[]
letter_alph=[]
for i in range(0, length):
    a=ltext[i]
    if a in alphabet:
        # first find the index of each string of text in alphabet list
        ina=alphabet.index(a)
        # then replace that index with index+1 in alphabet list
        ina=ina+1
        # then add that new index coresponding letter to a list
        inalist.append(ina)
        bbb=alphabet[ina]
        letter_alph.append(bbb)
    else:
        continue
#print(inalist)
#print(letter_alph)
#then join the strings in the list/strip to form words
joined=''.join(letter_alph)
print(f"The coded text is: {joined}")

#spaces and punctuation need to be left in place, not sorted yet.
#decoder needs to be done
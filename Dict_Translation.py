import string
num_word = int(input())

persian_word = []
english_word = []
germany_word = []
french_word = []
trans_sentence = ""
Dictionary = {}
for i in range(num_word):
    persian, english, french, germany = input().split(' ')
    
    persian_word.append(persian)
    english_word.append(english)
    germany_word.append(germany)
    french_word.append(french)


for n in range(num_word):
    Dictionary[persian_word[n]] = [english_word[n], french_word[n], germany_word[n]]

sentence = input()


#for persian, translation in Dictionary.items():
for word in sentence.split(' '):
    counter = 0
    for persian, translation in Dictionary.items():
        
        if word == translation[0]: 
            trans_sentence = trans_sentence + persian + " "
            #print(trans_sentence)
        elif word == translation[1]:
            trans_sentence = trans_sentence + persian + " "
            #print(trans_sentence)
        elif word == translation[2]:
            trans_sentence = trans_sentence + persian + " "
            #print(trans_sentence)
        else:
            #trans_sentence = trans_sentence + word + " "
            #print(trans_sentence)
            counter += 1
    if counter == num_word:
        trans_sentence = trans_sentence + word + " "

print(trans_sentence)

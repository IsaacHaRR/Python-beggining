

correct_word = "PASSWORD"
word_type = ""
count = 0
fail = False

print("Digite a senha")

while(input(word_type) != correct_word):
    if(count == 2):
        fail = True
        break
    
    print("Digite a senha")
    count += 1

if(fail):
    print("Voce errou")
else:
    print("Conseguiu")




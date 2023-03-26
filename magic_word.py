

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




  def pow(base, pow_number):
    count = 0
    result
    while (count == pow_number):
        result = result * base
        count *= count 
    return result

print(pow(3,2))
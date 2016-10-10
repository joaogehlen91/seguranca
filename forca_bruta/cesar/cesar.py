from sys import argv

data = open(argv[1], 'rb').read()


words_english = open('../all_words.txt', 'rb').read()
words_english = words_english.split()

for chave in range(1, 10**6):
    string = bytes((l + chave*-1) % 256 for l in data)
    lista_palavras = string.split()
    
    words = []
    for word in lista_palavras:
        if word in words_english:
            words.append(word)
    
    if(len(words) > 0):
        open('output_original', 'wb').write(bytes((l + chave*-1) % 256 for l in data))
        print(chave)
        break
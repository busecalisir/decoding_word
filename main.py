
alphabet = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o",
            16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
decoded_list = []

def decoding(word):
    for i in range(len(word)):
        for j in alphabet.keys():
            if word[i] == alphabet[j]:
                a = len(alphabet) - j + 1
                decoded_list.append(alphabet[a])
        if word[i] == " ":
            decoded_list.append(" ")
        else:
            continue

    print("".join(decoded_list))

decoding("svool yfhv")

#Python Script For Hacking the Caesar Cipher With the Brute Force
#Programming By : Ahmed Kamal
#caesar_cipher_hacking

cipher = input("Cipher Text > ").lower()
keys_number = int(input("Number of brute force keys > "))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
f =0
key =0
while f <= keys_number:
    for i in cipher:
        alpha_index = alphabet.index(i)
        if alpha_index - key < 0:
            plain_text_index = 26 - abs(alpha_index - key)
            print(alphabet[plain_text_index], end="")
        if alpha_index - key >= 0:
            print(alphabet[alpha_index - key], end="")
    key = key + 1
    f = f + 1
    print("\n")

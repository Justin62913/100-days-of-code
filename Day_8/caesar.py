# Caesar Cipher

Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
Max_key_size = len(Symbols)


def get_mode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'e']:
            return mode
        else:
            print('Enter either "encrypt" or "e" "decrypt" "d". ')


def get_message():
    print('Enter your message: ')
    return input()


def get_key():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (Max_key_size))
        key = int(input())
        if (key >= 1 and key <= Max_key_size):
            return key


def get_translated_message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = Symbols.find(symbol)
        if symbolIndex == -1: # Symbol not found in Symbols.
            # just add this symbol without any change.
            translated += symbol
        else:
            #Encrypt or decrypt.
            symbolIndex += key

            if symbolIndex >= len(Symbols):
                symbolIndex -= len(Symbols)
            elif symbolIndex < 0:
                symbolIndex += len(Symbols)

            translated += Symbols[symbolIndex]
    return translated


mode = get_mode()
message = get_message()
key = get_key()
print(f'Your translated text is: {get_translated_message(mode, message, key)}')

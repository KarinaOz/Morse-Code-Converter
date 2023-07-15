import time

morse_list = ['·−', '−···', '−·−·', '−··', '·', '··−·', ' −−·', '····', '··', '·−−−', '−·−', '·−··', '−−', '−·', '−−−',
              '·−−·', '−−·−', '·−·', '···', '−', '··−', '···−', '·−−', '−··−', '−·−−', '−−··', '−−−−−', '·−−−−',
              '··−−−', '···−−', '····−', '·····', '−····', '−−···', '−−−··', '−−−−·', '.-.-.-', '--..--', '..--..',
              '.----.', '-..-.', '-.--.', '-.--.-', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '.--.-.']

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '?', "'",
                '/', '(', ')', ':', ';', '=', '+', '-', '@']

morse_string = []

decoded_string = []


def encryption():
    string_for_encryption = input('Please, provide the text for encryption: ').lower()

    for character in string_for_encryption:
        if character in letters_list:
            index = letters_list.index(character)
            morse_string.append(morse_list[index])
        elif character == " ":
            morse_string.append("")

    print(f'Here is your encripted text: {" ".join(str(x) for x in morse_string)}')


def decoding():
    string_for_decoding = input('Please, provide the text for decoding: ')
    list_for_decoding = list(string_for_decoding.split(" "))
    for character in list_for_decoding:
        if character in morse_list:
            index = morse_list.index(character)
            decoded_string.append(letters_list[index])
        elif character == '':
            decoded_string.append(" ")
    print(f'Here is your decoded text: {"".join(str(x) for x in decoded_string)}')


def morse_convector():

    query = input('Type "e" to encrypt the text and "d" to decipher the text: ')

    if query == "e":
        encryption()
    elif query == 'd':
        decoding()
    else:
        "There is no such option, try again"
        morse_convector()


print("Hello there! This is Morse code translator.")
time.sleep(1)
morse_convector()

while input(f"Do you want to give a new encryption/decoding assignment? Type 'y' or 'n': ") == 'y':
    morse_convector()

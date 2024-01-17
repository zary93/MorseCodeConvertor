MORSE_DIC = {'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-',
             'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----', ',': '--..--', '.': '.-.-.-',
             '?': '..--..', '/': '-..-.', '-': '-....-',
             '(': '-.--.', ')': '-.--.-'}


text = input("Write a text here: ")
upper_text = text.upper()
morse_message = []
text_into_list = list(upper_text)
for word in text_into_list:
    if word == " ":
        morse_word = "|"
    else:
        morse_word = MORSE_DIC[word]
    morse_message.append(morse_word)

print(morse_message)  # Return the text into a list
# print(''.join(morse_message)) # Return the text into a string

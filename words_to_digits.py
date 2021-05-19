"""
  This takes a file words.txt and reads each line as a word.
  Each letter is replaced by the corresponding digit from 
  a standard telephone keypad.
  Words and digits are rewritten to digits.txt
"""
with open("words.txt") as wordsfile:
    words_content = wordsfile.readlines()
words_content = [x.strip() for x in words_content]
letterswitch = {'a':'2',
                'b':'2',
                'c':'2',
                'd':'3',
                'e':'3',
                'f':'3',
                'g':'4',
                'h':'4',
                'i':'4',
                'j':'5',
                'k':'5',
                'l':'5',
                'm':'6',
                'n':'6',
                'o':'6',
                'p':'7',
                'q':'7',
                'r':'7',
                's':'7',
                't':'8',
                'u':'8',
                'v':'8',
                'w':'9',
                'x':'9',
                'y':'9',
                'z':'9',}

with open('digits.txt', 'w') as digitsfile:
    for word in words_content:
        digits = []
        for letter in word:
            try:
                digits.append(letterswitch[letter.lower()])
            except:
                pass
        word_as_number = ''.join(digits)
        print(word + " = " + word_as_number)
        digitsfile.write(word + " = " + word_as_number + '\n')


"""
Author: Stephanie Pittman
CSCI 220

Certificate of Authenticity: I hear by certify that this is my own work and I discussed this with Tutor Brooke Duvall

Input: Keyword and Message from user
Output: Encoded Message

"""
from graphics import *

def code(message, keyword):

    alphabet_table = []

    for row in range(26):
        temp = []
        for col in range(26):
            a_value = ord('A')
            new_value = (row + col) % 26
            temp.append(chr(a_value + new_value))
        alphabet_table.append(temp)
    extend_key = ""
    for i in range(len(message)):
        extend_key += keyword[i % len(keyword)]

    cipher_text = ''
    for i in range(len(message)):
        cipher_text += alphabet_table[(ord(extend_key[i]) - 65) % 26][(ord(message[i]) - 65) % 26]
    return cipher_text

def main():
    win = GraphWin("Encoder", 500, 500)
    message_text = Text(Point(100, 50), "Message to code")
    message_text.draw(win)
    code_box = Entry(Point(300, 50), 20)
    code_box.setText("")
    code_box.draw(win)
    keyword_text = Text(Point(100, 100), "Enter Keyword")
    keyword_text.draw(win)
    key_box = Entry(Point(300, 100), 20)
    key_box.setText("")
    key_box.draw(win)
    button = Text(Point(250, 250), "Encode")
    button.draw(win)
    border = Rectangle(Point(200, 225), Point(300, 275))
    border.draw(win)
    win.getMouse()

    coded_message = str(code_box.getText()).upper().replace(" ", "")
    keyword_message = str(key_box.getText()).upper().replace(" ", "")

    cipher_text = code(coded_message, keyword_message)

    win.getMouse()

    button.undraw()
    border.undraw()

    result_text = Text(Point(200, 225), "Resulting Message \n" + cipher_text)
    result_text.draw(win)

    click = Text(Point(250, 450), "Click Anywhere To Close Window")
    click.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()







#dictionaries of characters
# letter_index = dict(zip(characters, range(len(characters))))
# index_letter = dict(zip(range(len(characters)), characters))

# def encrypt(message, keyword):
#     split message to length of key
    # split_message = []
    # for i in message:
    #     cipher = message[i:i + len(keyword)]
    #     split_message.append(cipher)
    #
    # convert the message to index and add key
    # write encrypted text

"""
possible code
"""

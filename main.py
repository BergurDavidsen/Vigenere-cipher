from tkinter import *
import smtplib
from email.message import EmailMessage

# variables, lists, and dictionaries
numbToLet = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
             12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w',
             23: 'x', 24: 'y', 25: 'z'}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
word = ""
wordArr = []


def mailSender():
    sender_email = "encryption.decryption.app@gmail.com"
    rec_email = recieverEntry.get()
    password = "eiqdwexydsjmobux"

    newMessage = EmailMessage()

    newMessage['Subject'] = "Secret Message"
    newMessage['From'] = sender_email
    newMessage['To'] = rec_email
    newMessage.set_content(f'the secret word is: {wordArr[-1]}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        print('login succes')
        smtp.send_message(newMessage)

    print("email has been sent to ", rec_email)
    sentStatus.insert(0, 'message has succefully been sent to {}'.format(rec_email))


def encryption():
    cipherWord = textIp.get().lower()
    keyword = keywordIp.get().lower()

    textIp.delete(0, 'end')
    keywordIp.delete(0, 'end')
    resultText.delete(0, 'end')

    if len(cipherWord) > len(keyword):
        k = len(cipherWord) - len(keyword)
        for i in range(k):
            keyword += keyword[i]

    print(keyword)
    print(cipherWord)

    keywordArr = []
    for i in keyword:
        keywordArr.append(i)
    print(keywordArr)

    word = ''
    n = 0
    for i in cipherWord:
        letter = alphabet.index(i) + alphabet.index(keywordArr[n])
        word += numbToLet[letter % 26]
        n += 1

    resultText.insert(0, word)

    print(word)

    wordArr.append(word)


def decryption():
    word = ""

    encrWord = textIp.get().lower()
    keyword = keywordIp.get().lower()
    textIp.delete(0, 'end')
    keywordIp.delete(0, 'end')
    resultText.delete(0, 'end')

    if len(encrWord) > len(keyword):
        k = len(encrWord) - len(keyword)
        for i in range(k):
            keyword += keyword[i]
    print(encrWord)
    print(keyword)

    keywordArr = []
    for i in keyword:
        keywordArr.append(i)

    n = 0
    for i in encrWord:
        letter = alphabet.index(i) - alphabet.index(keywordArr[n])
        word += numbToLet[letter % 26]
        n += 1

    resultText.insert(0, word)

    print(word)
    wordArr.append(word)


def clear():
    textIp.delete(0, 'end')
    keywordIp.delete(0, 'end')
    resultText.delete(0, 'end')


def backButton():
    messageEntry.delete(0, 'end')
    sentStatus.delete(0, 'end')

    for l in elements2:
        l.pack_forget()

    for i in elements:
        i.pack()


def messageButton():
    for i in elements:
        i.pack_forget()

    for l in elements2:
        l.pack()

    if len(wordArr) > 0:
        messageEntry.insert(0, wordArr[-1])


# screen window
root = Tk()
root.geometry('700x550')

space1 = Label(text=' ')
space2 = Label(text=' ')
space3 = Label(text=' ')
space4 = Label(text=' ')
space5 = Label(text=' ')
space6 = Label(text=' ')
space7 = Label(text=' ')
space8 = Label(text=' ')

infoLb = Label(text='Hello, this is an applecation that uses the vigenère cipher to encrypt and decrypt messages.')
# infoLb.pack()
info2Lb = Label(
    text='This only works for the letters in the english alphabet. It will NOT work with symbols or numbers.')
# info2Lb.pack()

instructLb = Label(text='You can choose to either encrypt or decrypt a sentance.')
# instructLb.pack()
# space1.pack()

encrLb = Label(text='The word you want to encrypt/decrypt: ')
# encrLb.pack()

textIp = Entry(root, width=50)
# textIp.pack()
# space2.pack()

keywordLb = Label(text='The given keyword: ')
# keywordLb.pack()

keywordIp = Entry(root, width=50)
# keywordIp.pack()
# space3.pack()

resultLb = Label(text='Result: ')
# resultLb.pack()

resultText = Entry(root, width=50)
# resultText.pack()
# space4.pack()

encrBt = Button(text='Encrypt', bg='yellow', command=encryption)
# encrBt.pack()

decrBt = Button(text='Decrypt', bg='yellow', command=decryption)
# decrBt.pack()

clearBt = Button(text='Clear', bg='red', command=clear)
"""clearBt.pack()
space5.pack()
space6.pack()
space7.pack()"""

messageBt = Button(text='Send messsage via mail', bg='orange', command=messageButton)
# messageBt.pack()

elements = [infoLb, info2Lb, instructLb, space1, encrLb, textIp, space2, keywordLb, keywordIp, space3, resultLb,
            resultText, space4, encrBt, decrBt, clearBt, space5, space6, space7, messageBt]

for i in elements:
    i.pack()

# screen 2
space9 = Label(text=' ')
space10 = Label(text=' ')
space11 = Label(text=' ')
space12 = Label(text=' ')
space13 = Label(text=' ')

recieverLb = Label(text='Put in the email you want to send to: ')
recieverEntry = Entry(root, width=50)

messageLb = Label(text='The message you want to send: ')
messageEntry = Entry(root, width=50)

sendBt = Button(text='Send message', command=mailSender)

backBt = Button(text='Back', command=backButton)

statusLb = Label(text='Message status: ')
sentStatus = Entry(root, width=65)

elements2 = [recieverLb, recieverEntry, space9, messageLb, messageEntry, space10, space11, sendBt, space12, backBt,
             space13, statusLb,
             sentStatus]

root.mainloop()

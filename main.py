from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from PIL import ImageTk,Image
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

#pyttsx3 for audio msgs
engine = pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0 ].id)

def Speak(word):
    engine.say(word)
    engine.runAndWait()

My_bot = ChatBot("My ChatBot")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."

]
trainer = ListTrainer(My_bot)

trainer.train(conversation)


# response = My_bot.get_response("Good morning!")
# print(response)



# print("Talk to Chatbot")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = My_bot.get_response(query)
#     print("bot: ",answer)



main = Tk()

main.geometry("500x650")
main.title("UET Administrative ChatBot")

# img = PhotoImage(file="uet.png")
# photo = Label(main , image=img)
# photo.pack(pady=5)


# canvas = Canvas(main, width = 300, height = 300)
# canvas.pack()
# img=ImageTk.PhotoImage(Image.open("uet.png"))
# canvas.create_image(20, 20, anchor=NW, image=img)

#take query and convert into string
def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold=1
    print("your bot is lesstning tyr to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='en-US')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            Ask_from_Bot()
        except Exception as e:
            print(e)
            print("Not Recogonized")





def Ask_from_Bot():
    query = textF.get()
    ans = My_bot.get_response(query)
    msgs.insert(END,"You: " + query)
    msgs.insert(END,"Bot: " + str(ans))
    Speak(ans)
    msgs.yview(END)


frame = Frame(main)




sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

#Creating text Field
textF = Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)

#Button
btn = Button(main,text="Send",font=("Verdana",20),command=Ask_from_Bot)
btn.pack()

#Creating a Function
def enter_function(event):
    btn.invoke()

#Binding the window with enter key
main.bind('<Return>',enter_function)


def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)
t.start()

main.mainloop()
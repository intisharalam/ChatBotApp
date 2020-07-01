# Import tkinter for GUI
from tkinter import *
from Brain import Brain
from Trainer import Trainer

# Access of Chatbot and Trainer modules
bot = Brain.bot
trainer = Trainer

#Training the bot
trainer.Train()

# GUI For ChatBot
base = Tk()
base.title("Aria The ChatBot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

# Create Chat window
ChatLog = Text(base, bd=0, bg="#8AC7B3", height="8", width="50", font=("Roboto", 12), fg="#351509")
ChatLog.config(state=DISABLED)


# Button function to send message to EntryBox
def send():
    message = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if message != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + message + '\n\n')
        res = bot.get_response(message)
        ChatLog.insert(END, "Aria: " + str(res) + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        if message == 'Bye':
            exit()


# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set


# Create Button to send message
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#20B687", activebackground="#458F77", fg='#D8F8EE',
                    command=send)


# Create the box to enter message
EntryBox = Text(base, bd=0, bg="#458F77", width="29", height="5", font=("Roboto", 25), fg="#474747")


# Place all components on the screen
scrollbar.place(x=390, y=0, height=450)
ChatLog.place(x=0, y=0, height=450, width=400)
EntryBox.place(x=100, y=450, height=50, width=300)
SendButton.place(x=0, y=450, height=50, width=100)
base.mainloop()

# Import trainer

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from datetime import datetime
from Brain import Brain

class Trainer:
    def Train():
        # Access of Chatbot modules
        bot = Brain().bot

        # Bot Training
        trainer_Corpus = ChatterBotCorpusTrainer(bot)
        trainer_List = ListTrainer(bot)
        trainer_List.train([
                "good",
                "That's good to hear!"
        ])
        trainer_List.train([
            "what is your name",
            "I'm Aria the chatbot ;)",
            "what do i call you",
            "Call me Aria, your personal chatbot!!!",
            "your name",
            "I'm Aria the chatbot ;)",
            "could you please tell me your name",
            "I'm Aria the chatbot ;)",
        ])
        trainer_List.train([
            "how are you",
            "I am good.",
            "That is good to hear.",
            "It is.",
            "im doing good",
            "Nice"
        ])
        trainer_List.train([
            "what time is it",
            "It is " + datetime.now().strftime('%I:%M %p'),
            "what is the time",
            "It is " + datetime.now().strftime('%I:%M %p'),
            "do you know the time",
            "It is " + datetime.now().strftime('%I:%M %p'),
            "do you have the time",
            "It is " + datetime.now().strftime('%I:%M %p'),
            "hey what time is it",
            "It is " + datetime.now().strftime('%I:%M %p'),
        ])
        trainer_List.train([
            "no",
            "Ok",
            "whats up",
            "All is well.",
            "bye",
            "Bye",
            "good bye",
            "See you later!",
            "cya",
            "Nice to meet you!"
        ])

        trainer_Corpus.train(
            "chatterbot.corpus.english",
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
        )

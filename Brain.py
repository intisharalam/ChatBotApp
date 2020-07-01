# Import modules
from chatterbot import ChatBot


class Brain:
    # Bot naming access declaration
    bot = ChatBot(
        'Aria',
        logic_adapters=
        [
            'chatterbot.logic.MathematicalEvaluation',
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )

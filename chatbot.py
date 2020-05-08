from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('BetsBi')

bot = ChatBot(
    'BetsBi',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(bot)

# trainer.train(
#     "chatterbot.corpus.english"
# )

trainer = ListTrainer(bot)

# Train the chat bot with a few responses
trainer.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
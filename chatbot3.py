# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Igor',
    trainer = 'chatterbot.trainers.ListTrainer'
)

conversation = [
    "Salut epta",
    "Salut Igor! Gde dengi?",
    "Cho s dengami?",
    "Kotorye ya vnes v kapital",
    "PAPA"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

# Get a response to the input text
response1 = chatbot.get_response('Salut Igor! Gde dengi?')
response2 = chatbot.get_response('Kotorye ya vnes v kapital')


while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

# print(response1)

# print(response2)
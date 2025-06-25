import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I help you?", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name\??",
        ["I'm a chatbot created using NLTK.", "You can call me NLTK Bot."]
    ],
    [
        r"how are you\??",
        ["I'm just a program, but I'm doing fine!", "I'm always good!"]
    ],
    [
        r"what can you do\??",
        ["I can chat with you, answer simple questions, and keep you company!", "Right now, I'm learning to answer more things!"]
    ],
    [
        r"who created you\??",
        ["I was created by a student using Python and NLTK.", "Someone who's learning to code made me!"]
    ],
    [
        r"where are you from\??",
        ["I live inside your computer.", "From the magical world of Python!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Glad to help!", "No problem!"]
    ],
    [
        r"(bye|exit|quit)",
        ["Goodbye!", "See you later!", "Bye!"]
    ],
    [
        r"(.*)",
        ["Hmm... interesting.", "Can you say that another way?", "I'm not sure I understand, but I'm learning!"]
    ]
]



def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

start_chat()

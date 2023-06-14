
def store(chat: str):
    with open("Data/chats", 'a') as file:
        file.write(chat + '\n')

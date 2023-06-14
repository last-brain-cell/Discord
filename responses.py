import random
from Data import contact_info, calculate, prompt


def handle_response(message) -> str:
    p_message = message.lower()

    toggle_cmd = 'bot'
    if p_message[:3] == toggle_cmd and p_message[3] == ' ':
        p_message = p_message[4:]
        print(p_message)
        if p_message == 'hello' or p_message == 'hii' or p_message == 'hey': return random.choice(['Hey there!', 'Heyy sup?', 'yoooo', 'Hello!'])

        if p_message == 'roll': return str(random.randint(1, 6))

        if p_message == 'toss': return str(random.choice(["heads, tails"]))

        if 'help' in p_message:
            with open("Data/help", 'r') as file:
                return str("".join(file.readlines()))

        if p_message[:7] == 'contact':
            name = p_message[8:]
            print(name)
            return contact_info.contact(name)

        if p_message[:6] == 'search':
            from googlesearch import search
            query = p_message[7:]

            for link in search(query, tld="co.in", num=10, stop=10, pause=2):
                return link

        if p_message[:9] == 'calculate':
            expression = p_message[10:]
            operators = ['+', '-', '*', '/', '%']
            for operator in operators:
                if operator in expression:
                    exp = expression.split(operator)
                    return calculate.calc(int(exp[0]), int(exp[1]), operator)

        if p_message[:4] == 'tell':
            p_message = p_message[5:].split(" ")
            r, prepos = p_message[0], p_message[1]
            p_message.remove(r)
            p_message.remove(prepos)
            msg = " ".join(p_message)
            return f"{msg}, {r}"

        # if p_message[:6] == 'prompt':
        #     p = p_message[7:]
        #     return prompt.generate(p)

        else:
            return "I didn't get that, maybe try again??"


contacts = {
    'mother': ['9823807410'],
    'father': ['9225508858', '9225508858'],
    'yasho': ['7507084497'],
    'sahil': ['8956106290'],
    'aditya': ['7741978797'],
}

def contact(name: str):
    if name in contacts.keys():
        out = f"{name}\n{' / '.join(contacts[name])}"
        return out
    else:
        return f"Contact '{name}' not found."

from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Hmm? Don\'t be shy !'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you?' in lowered:
        return 'Good, thanks! <3'
    elif 'bye' in lowered:
        return 'Sayonara!~'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)} :game_die:'
    else:
        return choice(['Eh..?',
                       'I don\'t understand...',
                       'Sorry? I\'m not quite following...'])
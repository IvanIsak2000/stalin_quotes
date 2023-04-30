import secrets


def stalin(language: str, person: str):
    if person == 'S':
        if language == 'ru':
            with open('stalin_ru.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                text = text.split('\n')
                full = 0
                for c in text:
                    full += 1
                print(f'\n{secrets.choice(text)}\n--И.В.Сталин.', full)
        if language == 'en':
            with open('stalin_en.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                text = text.split('\n')
                print(f'\n{secrets.choice(text)} \n--J.V.Stalin.')


stalin('ru', 'S')

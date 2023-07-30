from random import choice


def stalin(language: str, person: str):
    if person != 'S':
        return
    if language == 'ru':
        with open('stalin_ru.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.split('\n')
            print(f'\n{choice(text)}\n--И.В.Сталин.', len(text))
    if language == 'en':
        with open('stalin_en.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.split('\n')
            print(f'\n{choice(text)} \n--J.V.Stalin.')


if __name__ == "__main__":
    stalin('ru', 'S')

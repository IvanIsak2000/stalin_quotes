from random import choice


def get_quote(language: str, person: str) -> str | None:
    if person != 'S':
        return None
    if language == 'ru':
        with open('stalin_ru.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.split('\n')
            random_quotes = choice(text)
            return print(f'\n{random_quotes}\n--И.В.Сталин. \n{text.index(random_quotes)}')
           
    if language == 'en':
        with open('stalin_en.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            text = text.split('\n')
            random_quotes = choice(text)
            return print(f'\n{choice(text)} \n--J.V.Stalin.\n{text.index(random_quotes)}')


if __name__ == "__main__":
    get_quote('en', 'S')

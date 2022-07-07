from requests import get
from bs4 import BeautifulSoup

def print_animals():

    def parse_page(tags, alphabet):
        is_animals = False
        for tag in tags:
            if tag.text == "Животные":
                break
            if is_animals:
                if tag.text[0] not in alphabet.keys():
                    alphabet[tag.text[0]] = 0
                alphabet[tag.text[0]] += 1
            if tag.text == " Породы собак по алфавиту‎ (405: 405 с.)":
                is_animals = True

    alphabet = {}
    url_head = "https://ru.wikipedia.org"
    url = url_head + "/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
    soup = BeautifulSoup(get(url).text, 'lxml')
    while not soup.find(text='Следующая страница') is None:
        parse_page(soup.find_all('li'), alphabet)
        url = url_head + soup.find(text='Следующая страница').parent.get('href')
        soup = BeautifulSoup(get(url).text, 'lxml')
    for letter in alphabet.keys():
        print(f"{letter}: {alphabet[letter]}")

print_animals()

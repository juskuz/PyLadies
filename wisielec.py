from random import *


def game():
    lista = ["kot", "pies", "mysz", "szczur", "chomik", "rybki"]
    used_letters = []

    chosen_word = lista[randrange(0, len(lista))]  # choose word from list
    print("_ " * len(chosen_word))  # print hidden letters

    counter = 0
    won = True
    while len(chosen_word) != counter:
        l = (input("\nPodaj literę: "))
        if len(l) > 1:
            won = False
            break
        used_letters.append(l)
        counter = 0
        word_to_print = ''
        for let in chosen_word:
            if let in used_letters:
                word_to_print += (let + " ")
                counter += 1
            else:
                word_to_print += "_ "
        print(word_to_print)

    if (won):
        print("\nGratulacje! Wygrałeś! Liczba potrzebnych tur: {}".format(len(used_letters)))
    else:
        print("Uuuu.... Przegrałeś. Hasło to: {}. Liczba tur: {}".format(chosen_word, len(used_letters)))


game()

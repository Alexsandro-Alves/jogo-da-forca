from random import shuffle


class Game:
    def __init__(self):
        self.list_words = []
        self.secret_word = self.get_random_word()
        self.win = False
        self.lose = False
        self.errors = 0
        self.correct_letters = ["_" for letter in self.secret_word]

    @staticmethod
    def welcome_to_game() -> None:
        print('*********************************')
        print('***Bem vindo ao jogo da Forca!***')
        print('*********************************')

    def get_random_word(self) -> str:
        file = open('words.txt', 'r')
        for line in file:
            self.list_words.append(line.strip().upper())
        shuffle(self.list_words)
        return self.list_words[0]

    def start_game(self) -> None:
        while not self.win and not self.lose:
            index = 0
            user_letter = input('Qual a letra ? ').strip().upper()

            if user_letter in self.secret_word:
                for letter in self.secret_word:
                    if user_letter == letter:
                        self.correct_letters[index] = letter
                    index = index + 1
            else:
                self.errors = self.errors + 1
            self.lose = self.errors == 6
            self.win = '_' not in self.correct_letters
            print(self.correct_letters)

        if self.win:
            print('Parabéns você acertou!!')
        else:
            print('Você errou!!')
        print('Fim de jogo!!')
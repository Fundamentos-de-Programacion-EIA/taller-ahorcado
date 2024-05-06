import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = random.choice(word_list)
        self.guessed_letters = []
        self.attempts_remaining = 6

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return False, "Ya has adivinado esta letra."
        self.guessed_letters.append(letter)
        if letter not in self.secret_word:
            self.attempts_remaining -= 1
            return False, "Incorrecto."
        return True, "Correcto."

    def get_display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        return display_word

    def is_game_over(self):
        if self.attempts_remaining <= 0:
            return True, "¡Juego terminado! Perdiste."
        elif "_" not in self.get_display_word():
            return True, "¡Felicitaciones! Ganaste."
        return False, ""

    def play_game(self):
        print("Bienvenido al juego del Ahorcado!")
        while True:
            print("\nPalabra:", self.get_display_word())
            print("Intentos restantes:", self.attempts_remaining)
            print("Letras adivinadas:", ", ".join(self.guessed_letters))
            guess = input("Adivina una letra: ").lower()
            valid, message = self.guess_letter(guess)
            print(message)
            game_over, result_message = self.is_game_over()
            if game_over:
                print(result_message)
                if "_" not in self.get_display_word():
                    print("La palabra era:", self.secret_word)
                break

if __name__ == "__main__":
    word_list = ['python', 'hangman', 'computadora', 'programacion', 'codigo']
    game = Hangman(word_list)
    game.play_game()

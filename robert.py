import random
import time
from colorama import init
from colorama import Fore, Back, Style
import emoji

init()


class Core:

    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value: int = min_value
        self.max_value: int = max_value
        self.operations: list = ['+', '-']
        self.operations_time: list = [1, 2, 3]
        self.negative_number: bool = False
        self.colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.RESET]

    def practise(self):
        while True:
            self.random_question()
            time.sleep(1)

    def random_question(self):
        answer, title = self.generate_operation()
        while answer < 0 or answer >= 20:
            answer, title = self.generate_operation()
        print(random.choice(self.colors) + title)
        try:
            input_value = int(input())
        except Exception as ex:
            pass
        if input_value == answer:
            print(emoji.emojize('Emilie ist :red_heart:'))
        else:
            print(emoji.emojize('Emilie ist :thumbs_down:'))

    def generate_operation(self):
        final_answer = None
        final_title = ""
        start_value = random.randint(self.min_value, self.max_value)
        end_value = random.randint(self.min_value, self.max_value)
        operation = random.choice(self.operations)
        if operation == "+":
            final_answer = start_value + end_value
        elif operation == "-":
            final_answer = start_value - end_value
        elif operation == "*":
            final_answer = start_value * end_value
        elif operation == "/":
            final_answer = start_value / end_value
        final_title = f'{start_value} {operation} {end_value} = '
        return final_answer, final_title


if __name__ == "__main__":
    core = Core(min_value=0, max_value=20)
    core.practise()

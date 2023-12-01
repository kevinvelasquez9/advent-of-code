from abc import ABC, abstractmethod


class AbstractDay(ABC):
    def __init__(self, year, day):
        self.input_file_path = f"./{year}/inputs/input{day}.txt"
        self.input = self._read_input()
        self.lines = self.input.splitlines()

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

    def _read_input(self):
        with open(self.input_file_path, "r") as file:
            return file.read()

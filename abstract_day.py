from abc import ABC, abstractmethod


class AbstractDay(ABC):
    def __init__(self, year, day, ex):
        self.year = year
        self.day = day
        self.ex = ex

        self.input_file_path = self._get_input_file_path()
        self.input = self._read_input()
        self.lines = self.input.splitlines()

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

    def _get_input_file_path(self):
        if self.ex:
            return f"./{self.year}/exs/ex{self.day}.txt"
        else:
            return f"./{self.year}/inputs/input{self.day}.txt"

    def _read_input(self):
        try:
            return open(self.input_file_path, "r").read()
        except FileNotFoundError:
            return ""

from abc import ABC, abstractmethod


class AbstractDay(ABC):
    def __init__(self, year: int, day: int, ex: bool):
        self.year = year
        self.day = day
        self.ex = ex

        self.input_file_path = self._get_input_file_path()
        self.data = self._read_data()
        self.lines = self.data.splitlines()

    def __str__(self) -> str:
        return f"-- Day {self.day} | {self.part1()} | {self.part2()}"

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

    def _get_input_file_path(self) -> str:
        if self.ex:
            return f"./{self.year}/exs/ex{self.day}.txt"
        else:
            return f"./{self.year}/inputs/input{self.day}.txt"

    def _read_data(self) -> str:
        try:
            return open(self.input_file_path, "r").read()
        except FileNotFoundError:
            return ""

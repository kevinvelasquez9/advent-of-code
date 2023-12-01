import argparse


def main():
    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--year", type=int, default=2023)
    parser.add_argument("--day", type=int)

    args = parser.parse_args()

    if args.day:
        run_day(args.year, args.day)
    else:
        run_days(args.year)


def run_day(year, day):
    print(f"day {day}")
    module_name = f"{year}.days.day_{day}"
    class_name = f"Day{day}"

    try:
        day_module = __import__(module_name, fromlist=[class_name])
        day_class = getattr(day_module, class_name)
        day_instance = day_class()
        print(f"  part 1: {day_instance.part1()}")
        print(f"  part 2: {day_instance.part2()}")
    except ModuleNotFoundError:
        print(f"  part 1: not found")
        print(f"  part 2: not found")


def run_days(year):
    for day in range(1, 26):
        run_day(year, day)
        print()


if __name__ == '__main__':
    main()

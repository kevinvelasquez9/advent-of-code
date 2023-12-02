import argparse


def main():
    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--year", type=int, default=2023)
    parser.add_argument("--day", type=int)
    parser.add_argument("--ex", action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    if args.day:
        run_day(args.year, args.day, args.ex)
    else:
        run_days(args.year, args.ex)


def run_day(year, day, ex):
    module_name = f"{year}.days.day_{day}"
    class_name = f"Day{day}"

    try:
        day_module = __import__(module_name, fromlist=[class_name])
        day_class = getattr(day_module, class_name)
        day_instance = day_class(year, day, ex)
        if day > 1:
            print()
        print(f"day {day}")
        print(f"  part 1: {day_instance.part1()}")
        print(f"  part 2: {day_instance.part2()}")
    except ModuleNotFoundError:
        pass


def run_days(year, ex):
    for day in range(1, 26):
        run_day(year, day, ex)


if __name__ == '__main__':
    main()

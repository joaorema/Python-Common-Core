import sys
from logging import exception


class ErrorClass(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message


def command_quest(args):
    print(f"===Command Quest===")
    if len(args) == 1:
        try:
            if len(args) < 1:
                raise ErrorClass("No arguments provided!")
            print(f"Program Name: {args[0]} ")
        except ImportError as e:
            print(e)
        finally:
            print(f"Total arguments: {len(args)}")
    else:
        try:
            print(f"Program Name: {args[0]} ")
            print(f"Arguments Received: {len(args) - 1}")
            for i  in range(1,len(args)):
                print(f"Argument {i}: {args[i]}")
        except (IndexError, TypeError) as e:
            print(e)
        finally:
            print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    command_quest(sys.argv[0:])
    pass






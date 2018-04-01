import sys
from rectangle import LittleGame


def main():
    """
    Start Pygane example

    :return: -
    :rtype: -
    """
    spped = 5
    my_game = LittleGame(spped)
    my_game.start_game()


if __name__ == "__main__":
    main()
    sys.exit(0)

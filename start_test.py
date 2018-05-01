import sys
from src import rectangle


def main():
    """
    Start Pygane example

    @return: True if start game is successful, otherwise False
    @rtype: bool
    """
    speed = 5
    my_game = rectangle.LittleGame(speed)
    return my_game.start_game()


if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)

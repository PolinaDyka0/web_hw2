"""C H A T B O T"""

from addressbook import main as ab_main
from notes import main as nb_main
from sort import main as sr_main
from information import start_info_menu
from logger import get_logger


def main():
    """Main function"""

    while True:

        print(start_info_menu())
        user_input = input(f"\nEnter command {chr(10151)*3} ")
        logger.info(f"User input: {user_input}")
        if user_input == "1":
            ab_main()
        elif user_input == "2":
            nb_main()
        elif user_input == "3":
            sr_main()
        elif user_input == "0":
            print(f"\n{chr(128075)} Good bay!")
            break
        else:
            print(f"\n{chr(129400)}I don't understand you!")


logger = get_logger(__name__)

if __name__ == "__main__":
    logger.debug("Start program")
    main()

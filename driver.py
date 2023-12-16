from store import Store


class Driver:
    """ Drives the user menu. """
    store_menu = Store()
    store_menu.display_user_menu()


def main():
    """
    Driver the User Menu.
    """
    Driver()


if __name__ == "__main__":
    main()

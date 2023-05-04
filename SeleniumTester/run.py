import sys
from superhero.superhero import SuperHero
import superhero.constants as const

try:
    with SuperHero(const.LOCALHOST_URL) as bot:
        # test 1
        bot.open_page()

        print("test create hero", end=" ")
        if bot.test_create_hero():
            print("\u2714".encode('utf-8').decode(sys.stdout.encoding))
        else:
            print("\u2717".encode('utf-8').decode(sys.stdout.encoding))

        bot.wait(const.FINISHED_TEST_WAITING_TIME)

        # test 2
        bot.open_page()

        bot.create_hero()
        bot.create_hero()
        print("test update heros with name", end=" ")
        if bot.test_update_heros_with_name():
            print("\u2714".encode('utf-8').decode(sys.stdout.encoding))
        else:
            print("\u2717".encode('utf-8').decode(sys.stdout.encoding))

        bot.wait(const.FINISHED_TEST_WAITING_TIME)

        # test 3
        bot.open_page()

        print("test delete heros with a particular name", end=" ")
        if bot.test_delete_heros_with_name():
            print("\u2714".encode('utf-8').decode(sys.stdout.encoding))
        else:
            print("\u2717".encode('utf-8').decode(sys.stdout.encoding))

        bot.wait(const.FINISHED_TEST_WAITING_TIME)

        # test 4
        bot.open_page()

        print("test edit-form initial input values", end=" ")
        if bot.test_edit_form_initial_input_values():
            print("\u2714".encode('utf-8').decode(sys.stdout.encoding))
        else:
            print("\u2717".encode('utf-8').decode(sys.stdout.encoding))

        bot.wait(const.FINISHED_TEST_WAITING_TIME)

        # test 5
        bot.open_page()

        print("test change background color", end=" ")
        if bot.test_change_color():
            print("\u2714".encode('utf-8').decode(sys.stdout.encoding))
        else:
            print("\u2717".encode('utf-8').decode(sys.stdout.encoding))

        bot.wait(const.FINISHED_TEST_WAITING_TIME)
        
except Exception as e:
    print(e)
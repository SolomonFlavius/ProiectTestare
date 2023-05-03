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

        print("test edit-form initial input values", end=" ")
        if bot.test_edit_form_initial_input_values():
            print("\u2714".encode('utf-8').decode(sys.stdout.encoding))
        else:
            print("\u2717".encode('utf-8').decode(sys.stdout.encoding))

        bot.wait(const.FINISHED_TEST_WAITING_TIME)
        
except Exception as e:
    print(e)
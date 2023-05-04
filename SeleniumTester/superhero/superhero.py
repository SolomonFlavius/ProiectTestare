import time
import superhero.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class SuperHero(webdriver.Chrome):
    def __init__(self, url: str, full_window = False):
        self.url = url
        super(SuperHero, self).__init__()
        self.implicitly_wait(const.IMPLICITE_WAITING_TIME)
        if full_window:
            self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        self.quit()

    def open_page(self):
        self.get(self.url)

    def wait(self, seconds: float):
        time.sleep(seconds)

    def create_hero(self, name_value="NameTest", first_name_value="FirstNameTest", last_name_value="LastNameTest", place_input_value="PlaceTest"):
        button = self.find_element(By.ID, "create-hero-button")
        button.click()

        new_table = self.find_element(By.CSS_SELECTOR, "app-edit-hero")
    
        name_input = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
        name_input.send_keys(name_value)
        
        first_name_input = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
        first_name_input.send_keys(first_name_value)
        
        last_name_input = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
        last_name_input.send_keys(last_name_value)
        
        place_input  = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='Place']")
        place_input.send_keys(place_input_value)

        create_button = self.find_element(By.XPATH, "//button[text()='Create']")
        create_button.click()
        time.sleep(2)

    def test_create_hero(self):
        row_value = "NameTest FirstNameTest LastNameTest PlaceTest Edit"
        
        initial_count = 0
        table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
        for row in table_rows:
            if row.text == row_value:
                initial_count += 1

        self.create_hero()

        finished_count = 0
        table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
        for row in table_rows:
            if row.text == row_value:
                finished_count += 1

        return finished_count == initial_count + 1

    def test_update_heros_with_name(self):
        initial_row_value = "NameTest FirstNameTest LastNameTest PlaceTest Edit"
        initial_count = 0
        edited_row_value = "NameTest - edited FirstNameTest - edited LastNameTest - edited PlaceTest - edited Edit"
        equal_to_edited_count = 0

        table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
        for row in table_rows:
            if row.text == initial_row_value:
                initial_count += 1
            elif row.text == edited_row_value:
                equal_to_edited_count += 1

        search = True
        while search:
            table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
            search = False

            for row in table_rows:
                if row is not None:
                    td = row.find_element(By.CSS_SELECTOR, "td")

                    if td.text ==  "NameTest":
                        edit_button = row.find_element(By.CSS_SELECTOR, "button")
                        edit_button.click()

                        name_input = self.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
                        name_input.send_keys(" - edited")
                        
                        first_name_input = self.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
                        first_name_input.send_keys(" - edited")
                        
                        last_name_input = self.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
                        last_name_input.send_keys(" - edited")
                        
                        place_input = self.find_element(By.CSS_SELECTOR, "input[placeholder='Place']")
                        place_input.send_keys(" - edited")

                        delete_button = self.find_element(By.XPATH, "//button[text()='Save']")
                        delete_button.click()

                        search = True
                        break

            time.sleep(2)

        table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
        after_edit_count = 0
        for row in table_rows:
            if row.text == edited_row_value:
                after_edit_count += 1

        return after_edit_count == initial_count + equal_to_edited_count

    def test_delete_heros_with_name(self):
        search = True
        while search:
            table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
            search = False

            for row in table_rows:
                if row is not None:
                    td = row.find_element(By.CSS_SELECTOR, "td")

                    if td.text ==  "NameTest - edited":
                        edit_button = row.find_element(By.CSS_SELECTOR, "button")
                        edit_button.click()

                        delete_button = self.find_element(By.XPATH, "//button[text()='Delete']")
                        delete_button.click()

                        search = True
                        break

            time.sleep(2)

        return True

    def test_edit_form_initial_input_values(self):
        valid = True
        elements = self.find_elements(By.CSS_SELECTOR, "button")
        row = 0
        table_rows = self.find_elements(By.CSS_SELECTOR, "tr")

        for element in elements:
            if(element.text == "Edit"):
                element.click()
                edit_form = self.find_element(By.CSS_SELECTOR, "app-edit-hero")
                
                name_input = edit_form.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
                name_value_initial = name_input.get_attribute("value")
                name_input.send_keys(" - tested")
                
                first_name_input = edit_form.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
                first_name_value_initial = first_name_input.get_attribute("value")
                first_name_input.send_keys(" - tested")
                
                last_name_input = edit_form.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
                last_name_value_initial = last_name_input.get_attribute("value")
                last_name_input.send_keys(" - tested")
                
                place_input = edit_form.find_element(By.CSS_SELECTOR, "input[placeholder='Place']")
                place_input_value_initial = place_input.get_attribute("value")
                place_input.send_keys(" - tested")

                if(table_rows[row].text != name_value_initial + " - tested "
                    + first_name_value_initial + " - tested " 
                    + last_name_value_initial + " - tested " 
                    + place_input_value_initial + " - tested Edit"):
                    valid = False

                row += 1
        
        return valid
    
    def test_change_color(self):
        color = 'blue'
        select_button = self.find_element(By.CSS_SELECTOR, "select")
        select = Select(select_button)

        select.select_by_value(color)
        WebDriverWait(self, timeout=const.EXPLICITE_WAITING_TIME).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"body[style*='background-color: {color}']"))
        )

        return True
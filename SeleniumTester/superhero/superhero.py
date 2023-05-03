import time
import superhero.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

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

    def test_create_hero(self): 
        button = self.find_element(By.ID, "create-hero-button")
        button.click()

        new_table = self.find_element(By.CSS_SELECTOR, "app-edit-hero")
    
        name_input = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
        name_value = "NameTest"
        name_input.send_keys(name_value)
        
        first_name_input = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
        first_name_value = "FirstNameTest"
        first_name_input.send_keys(first_name_value)
        
        last_name_input = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
        last_name_value = "LastNameTest"
        last_name_input.send_keys(last_name_value)
        
        place_input  = new_table.find_element(By.CSS_SELECTOR, "input[placeholder='Place']")
        place_input_value = "PlaceTest"
        place_input.send_keys(place_input_value)

        row_value = name_value + " " + first_name_value + " " + last_name_value + " " + place_input_value + " Edit"
        initial_count = 0
        table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
        for row in table_rows:
            if row.text == row_value:
                initial_count += 1

        create_button = self.find_element(By.XPATH, "//button[text()='Create']")
        create_button.click()
        time.sleep(3)

        finished_count = 0
        table_rows = self.find_elements(By.CSS_SELECTOR, "tr")
        for row in table_rows:
            if row.text == row_value:
                finished_count += 1

        return finished_count == initial_count + 1

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
                
                place_input  = edit_form.find_element(By.CSS_SELECTOR, "input[placeholder='Place']")
                place_input_value_initial = place_input.get_attribute("value")
                place_input.send_keys(" - tested")

                if(table_rows[row].text != name_value_initial + " - tested "
                    + first_name_value_initial + " - tested " 
                    + last_name_value_initial + " - tested " 
                    + place_input_value_initial + " - tested Edit"):
                    valid = False

                row += 1
        
        return valid
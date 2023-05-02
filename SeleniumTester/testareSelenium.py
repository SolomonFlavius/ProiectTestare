from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:4200/")

#testam salvarea
print("Incepe testarea pentru edit")

valid = True

elemente = driver.find_elements(By.CSS_SELECTOR, "button")

row = 0

for element in elemente:
	if(element.text == "Edit"):
		element.click()
		time.sleep(2)
		tabel_nou = driver.find_element(By.CSS_SELECTOR, "app-edit-hero")
		
		name_input = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
		name_value_initial = name_input.get_attribute("value")
		name_input.send_keys("test")
		time.sleep(2)
		
		first_name_input = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
		first_name_value_initial = first_name_input.get_attribute("value")
		first_name_input.send_keys("test")
		time.sleep(2)
		
		last_name_input = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
		last_name_value_initial = last_name_input.get_attribute("value")
		last_name_input.send_keys("test")
		time.sleep(2)
		
		place_input  = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='Place']")
		place_input_value_initial = place_input .get_attribute("value")
		place_input.send_keys("test")
		time.sleep(2)

		randuri = driver.find_elements(By.CSS_SELECTOR, "tr")
		if(randuri[row].text != name_value_initial+"test" + " " +first_name_value_initial+"test"+ " " +last_name_value_initial+"test"+ " " +place_input_value_initial+"test"+ " " +"Edit"):
			valid = False
		row += 1	
		time.sleep(2)


if valid == True:
	print("Testul pentru edit a reusit!")
else:
	print("Testul pentru edit a esuat!")

time.sleep(2)

if(valid == True):
	print("Incepe testul pentru creare!")
	elemente = driver.find_elements(By.CSS_SELECTOR, "button")
	time.sleep(2)
	for element in elemente:
		if(element.text == "Create New Hero"):
			element.click()
			time.sleep(2)
			tabel_nou = driver.find_element(By.CSS_SELECTOR, "app-edit-hero")
			time.sleep(2)
		
			name_input = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
			name_value = "NameTest"
			name_input.send_keys(name_value)
			time.sleep(2)
			
			first_name_input = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
			first_name_value = "FirstNameTest"
			first_name_input.send_keys(first_name_value)
			time.sleep(2)
			
			last_name_input = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
			last_name_value = "LastNameTest"
			last_name_input.send_keys(last_name_value)
			time.sleep(2)
			
			place_input  = tabel_nou.find_element(By.CSS_SELECTOR, "input[placeholder='Place']")
			place_input_value = "PlaceTest"
			place_input.send_keys(place_input_value)
			time.sleep(2)

			elemente = driver.find_elements(By.CSS_SELECTOR, "button")
			time.sleep(2)
			for element in elemente:
				if(element.text == "Create"):
					element.click()
					gasit = False
					randuri = driver.find_elements(By.CSS_SELECTOR, "tr")
					time.sleep(2)
					if(randuri[row].text == name_value+ " " +first_name_value+ " " +last_name_value+ " " +place_input_value+ " " +"Edit"):
						gasit = True
					valid = gasit
		if valid == True:
			print("Testul pentru creare a reusit!")
		else:
			print("Testul pentru creare a esuat!")

time.sleep(5000)
driver.quit()

from selenium import webdriver
from time import sleep
from os import path

user_mock = {
    "profileObj": {
            "email": "viictor.ivan@gmail.com",
            "familyName": "Ivan",
            "givenName": "Victor",
            "imageUrl": "https://lh3.googleusercontent.com/a-/AOh14GghH4MSHi7Vd8Axa8HpqmJw96wNbRuMYN4-9AD5Gw=s96-c",
            "name": "Victor Ivan"
    }
}

set_item = f"localStorage.setItem('@bycoders-desafio-dev', JSON.stringify({user_mock}));"
cnab_file_path = path.join(path.dirname(__file__),'files/CNAB.txt')

# Open browser
driver = webdriver.Chrome()
# Go to homepage
driver.get("http://localhost:3001")
# Wait 1 second
sleep(1)
# Mock a user on localStorage
driver.execute_script(set_item)
# Refresh this page
driver.refresh()
# Upload an file to input
upload_area = driver.find_element_by_xpath('//*[@id="file"]')
upload_area.send_keys(cnab_file_path)
# Click on the button for send the file to the api
send_file = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button')
send_file.click()
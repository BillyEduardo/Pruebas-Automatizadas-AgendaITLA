from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")  
driver = webdriver.Chrome(service=service)

try:
    
    driver.get("file:///C:/Users/Billi/OneDrive/Escritorio/ITLA/P3/Proyecto%20Final/Agenda%20ITLA/Register.html")

    # Encuentra los elementos del formulario
    username = driver.find_element(By.ID, "registerUsername")
    password = driver.find_element(By.ID, "registerPassword")
    confirm_password = driver.find_element(By.ID, "confirmPassword")
    register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    
    username.send_keys("testuser")
    password.send_keys("password123")
    confirm_password.send_keys("password123")
        
    register_button.click()

    time.sleep(3)
    modal_message = driver.find_element(By.ID, "modalMessage").text
    print(f"Mensaje recibido: {modal_message}")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    time.sleep(3)
    driver.quit()

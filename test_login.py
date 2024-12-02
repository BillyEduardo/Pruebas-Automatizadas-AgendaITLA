from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del servicio y driver
service = Service(executable_path="chromedriver.exe")  
driver = webdriver.Chrome(service=service)

try:
    print("Cargando la página...")
    driver.get("file:///C:/Users/Billi/OneDrive/Escritorio/ITLA/P3/Proyecto%20Final/Agenda%20ITLA/login.html")

    
    print("Buscando elementos del formulario...")
    username = driver.find_element(By.ID, "loginUsername")
    password = driver.find_element(By.ID, "loginPassword")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    print("Elementos encontrados, interactuando...") 
    username.send_keys("Billy")
    password.send_keys("Diamante")
    
   
    login_button.click()

    print("Esperando que aparezca el modal...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "modalMessage"))
    )

    modal_message = driver.find_element(By.ID, "modalMessage").text
    print(f"Mensaje recibido: {modal_message}")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    time.sleep(5)
    driver.quit()

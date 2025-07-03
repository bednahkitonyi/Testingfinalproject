from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_donate_button():
    # Initialize the Chrome driver
    driver = webdriver.Edge()

    try:
        driver.get("https://www.powerlearnprojectafrica.org/")
        
        donate_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div[1]/div/div/div/a[1]/div")))

        donate_button.click()

        #condition 2
        support_learner_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div[3]/div/div/div[2]/div[1]/div[2]/div[3]/button")))
        support_learner_button.click()
        time.sleep(5)

        firstname = driver.find_element(By.ID, "firstName")
        firstname.send_keys("Bednah")

        lastname = driver.find_element(By.ID, "lastName")
        lastname.send_keys("Kitonyi")  

        email = driver.find_element(By.ID, "email")
        email.send_keys("bednahkitonyi@gmail.com")  

        studentsnumber = webdriver.find_element(By.ID, "numberOfStudents")
        studentsnumber.clear()
        studentsnumber.send_keys("5") 

        print("Current URL:", driver.current_url)

        assert "donate" in driver.current_url, "The URL does not contain 'donate'"
        time.sleep(5)  # Wait for 5 seconds to observe the result

    except Exception as e:
        print("An error occurred:", e)
        raise  # Re-raise the exception for further handling if needed 
    
     #condition 3


    finally:
        # Close the driver
        driver.quit()  

test_donate_button()


# def test_support_learner_button():
#     # Initialize the Chrome driver
#     driver = webdriver.Edge()

#     try:
#         driver.get("https://www.powerlearnprojectafrica.org/invalid-url")
        
#         support_learner_button = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div[3]/div/div/div[2]/div[1]/div[2]/div[3]/button")))

#         support_learner_button.click()

#         print("Current URL:", driver.current_url)

        
#         time.sleep(10)  # Wait for 5 seconds to observe the result

#     except Exception as e:
#         print("An error occurred:", e)
#         raise  # Re-raise the exception for further handling if needed 

#     finally:
#         # Close the driver
#         driver.quit()

# test_support_learner_button()
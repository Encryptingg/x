from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    form_url = "https://www.facebook.com/help/contact/606967319425038"

    driver = webdriver.Chrome("path/to/chromedriver.exe")

    driver.get(form_url)

    try:
        full_name = driver.find_element(By.ID, "full_name_field")
        email = driver.find_element(By.ID, "email_field")
        instagram_username = driver.find_element(By.ID, "instagram_username_field")
        mobile_number = driver.find_element(By.ID, "mobile_number_field")
        appeal_reason = (
            "I am appealing the decision to permanently deactivate my account "
            "because I believe there has been a misunderstanding or mistake."
        )

        full_name.send_keys("John Doe")
        email.send_keys("john@example.com")
        instagram_username.send_keys("johndoe")
        mobile_number.send_keys("1234567890")

        send_button = driver.find_element(By.ID, "send_button")
        send_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "confirmation_message")))
        print("Appeal submitted successfully!")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

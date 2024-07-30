import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import regex


def fetch_marks(usn, day, month, year):
    options = Options()
    options.add_argument("--headless")
    service = Service(executable_path="D:\\chromedriv\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://parents.msrit.edu/parentseven/")
    marks_and_sub = {}
    # Initialize an empty dictionary
    result_dict = {}
    student_name = ""
    cgpa = 0
    sgpa_list = []

    try:
        # Fill in the username
        driver.find_element(By.NAME, "username").send_keys(usn)

        # Fill in the date, month, and year
        driver.find_element(By.ID, "dd").send_keys(day)
        driver.find_element(By.ID, "mm").send_keys(month)
        driver.find_element(By.ID, "yyyy").send_keys(year)

        # Click the login button (ensure the CSS selector is correct)
        login_btn = driver.find_element(By.CSS_SELECTOR,
                                        ".uk-button.uk-button-primary.uk-button-large.uk-width-1-1.cn-login-btn.cn-submit1.cn-landing-login1")
        login_btn.click()

        print("Login successful")

        # Click on a specific coordinate (e.g., x=100, y=200)
        action = ActionChains(driver)
        action.move_by_offset(100, 200).click().perform()
        # print("Clicked at specific coordinates (100, 200)")

        time.sleep(2)

        student_name = driver.find_element(By.XPATH, "//*[@id='page_bg']/div[1]/div/div/div[2]/div/div/div[1]/div/h3").text
        # Locate the script tag containing the chart data
        script_element = driver.find_element(By.XPATH, "//*[@id='page_bg']/div[1]/div/div/div[4]/div[1]/div/script")

        # Extract the JavaScript content
        script_content = script_element.get_attribute("innerHTML")
        script_content = script_content.strip()

        exam_history = driver.find_element(By.XPATH,
                                           "/html/body/div/div/div/div[1]/div/div[2]/nav/div/div/ul/li[5]/a").click()
        # print("clicked exam history")
        time.sleep(4)
        cgpa = driver.find_element(By.XPATH,
                                   "//*[@id='page_bg']/div/div/div/div[5]/div/div/div[1]/div/div[3]/div/p").text
        sem1_sgpa = driver.find_element(By.XPATH,
                                        "//*[@id='page_bg']/div/div/div/div[5]/div/div/div[3]/div/div/div/div/table/caption/span[3]").text
        sem2_sgpa = driver.find_element(By.XPATH,
                                        "//*[@id='page_bg']/div/div/div/div[5]/div/div/div[4]/div/div/div/div/table/caption/span[3]").text
        sem3_sgpa = driver.find_element(By.XPATH,
                                        "//*[@id='page_bg']/div/div/div/div[5]/div/div/div[5]/div/div/div/div/table/caption/span[3]").text
        sgpa = sem1_sgpa + sem2_sgpa + sem3_sgpa

        sgpa_list = regex.extract_sgpa(sgpa)
        sgpa_list = [float(num) for num in sgpa_list]
        cgpa = float(cgpa)

        # extracting each subject code and marks as array of strings
        marks_and_sub = regex.extract_marks(script_content)

        # Loop through each string in the list
        for item in marks_and_sub:
            # Convert the string representation of the list to an actual list
            code, number = eval(item)  # Using eval to parse the string safely
            result_dict[code] = number  # Store in dictionary

        # print subjects and marks
        for key, value in marks_and_sub:
            if value > 50:
                value = 50



    except Exception as e:
        print(f"An error occurred: {e}")

    #time.sleep(5)

    driver.quit()
    #print(type(result_dict))
    return result_dict, student_name, cgpa, sgpa_list

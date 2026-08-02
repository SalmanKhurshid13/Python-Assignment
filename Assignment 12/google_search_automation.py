"""
Assignment - Automation using Selenium - Getting Data
Script 1: Google Search Automation

This script:
- Creates a WebDriver instance using webdriver.Chrome()
- Opens Google using driver.get()
- Maximizes the browser window using driver.maximize_window()
- Locates the search box using By.NAME
- Performs a search operation using send_keys()
- Clicks a search result link using By.LINK_TEXT / By.XPATH and click()
- Uses time.sleep() for wait handling
- Refreshes the page using driver.refresh()
- Extracts multiple search result elements using find_elements()
- Displays the extracted data in the console using print()
- Closes the browser using driver.quit()
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    # 1. Create WebDriver instance
    driver = webdriver.Chrome()

    try:
        # 2. Open Google
        driver.get("https://www.google.com")

        # 3. Maximize the browser window
        driver.maximize_window()

        # Wait for the page to load
        time.sleep(2)

        # 4. Locate the search box using By.NAME and perform search
        search_box = driver.find_element(By.NAME, "q")
        search_query = "TuteDude Selenium automation course"
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(2)

        # 5. Extract multiple result heading elements using find_elements()
        result_headings = driver.find_elements(By.XPATH, "//h3")

        print("----- Google Search Results (Before Refresh) -----")
        for index, heading in enumerate(result_headings, start=1):
            text = heading.text.strip()
            if text:
                print(f"{index}. {text}")

        # 6. Try to click on the first available result link using By.XPATH
        try:
            first_result = driver.find_element(
                By.XPATH, "(//div[@class='yuRUbf']//a) | (//h3/ancestor::a)"
            )
            first_result.click()
            time.sleep(2)
            print("\nClicked on the first search result.")
            print("Current page title:", driver.title)
        except Exception as click_error:
            print("\nCould not click a result link:", click_error)

        # Go back to the search results page
        driver.back()
        time.sleep(2)

        # 7. Refresh the web page
        driver.refresh()
        time.sleep(2)

        # 8. Extract data again after refresh using find_elements()
        refreshed_headings = driver.find_elements(By.XPATH, "//h3")

        print("\n----- Google Search Results (After Refresh) -----")
        for index, heading in enumerate(refreshed_headings, start=1):
            text = heading.text.strip()
            if text:
                print(f"{index}. {text}")

    finally:
        # 9. Close the browser
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()

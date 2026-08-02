"""
Assignment - Automation using Selenium - Getting Data
Script 2: Amazon Data Extraction Automation

This script:
- Creates a WebDriver instance using webdriver.Chrome()
- Opens Amazon using driver.get()
- Maximizes the browser window using driver.maximize_window()
- Locates elements using By.NAME, By.CLASS_NAME, By.LINK_TEXT, and By.XPATH
- Performs a search operation using send_keys()
- Clicks elements using click()
- Uses time.sleep() for wait handling
- Refreshes the web page using driver.refresh()
- Extracts multiple elements (product names & prices) using find_elements()
- Displays the extracted data in the console using print()
- Closes the browser using driver.quit()
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def extract_products(driver, label):
    """Helper function to extract and print product titles and prices."""
    product_titles = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    if not product_titles:
        # Fallback locator in case Amazon's layout uses a different class
        product_titles = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")

    product_prices = driver.find_elements(By.CLASS_NAME, "a-price-whole")

    print(f"\n----- Extracted Amazon Products ({label}) -----")
    max_items = min(len(product_titles), 10) if product_titles else 0

    if max_items == 0:
        print("No products found (page layout may have changed or elements not loaded).")
        return

    for i in range(max_items):
        title = product_titles[i].text.strip()
        price = product_prices[i].text.strip() if i < len(product_prices) else "N/A"
        print(f"{i + 1}. {title} - Price: {price}")


def main():
    # 1. Create WebDriver instance
    driver = webdriver.Chrome()

    try:
        # 2. Open Amazon
        driver.get("https://www.amazon.in")

        # 3. Maximize the browser window
        driver.maximize_window()
        time.sleep(2)

        # 4. Locate the search box using By.NAME and perform search
        search_box = driver.find_element(By.NAME, "field-keywords")
        search_query = "laptop"
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # 5. Extract product data before refresh
        extract_products(driver, "Before Refresh")

        # 6. Locate an element using By.CLASS_NAME and click it (e.g. first product link)
        try:
            first_product_link = driver.find_element(
                By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']/ancestor::a"
            )
            first_product_link.click()
            time.sleep(3)
            print("\nClicked on the first product listing.")
            print("Current page title:", driver.title)
        except Exception as click_error:
            print("\nCould not click a product link:", click_error)

        # Go back to the search results page
        driver.back()
        time.sleep(2)

        # 7. Refresh the web page
        driver.refresh()
        time.sleep(3)

        # 8. Extract product data again after refresh using find_elements()
        extract_products(driver, "After Refresh")

        # 9. Example use of By.LINK_TEXT - navigate to "All" categories link if present
        try:
            all_link = driver.find_element(By.LINK_TEXT, "All")
            all_link.click()
            time.sleep(2)
            print("\nClicked on 'All' categories link.")
        except Exception:
            print("\n'All' categories link not found on this page.")

    finally:
        # 10. Close the browser
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()

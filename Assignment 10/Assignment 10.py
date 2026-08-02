import requests
from bs4 import BeautifulSoup
import os

# Product URLs
urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
]

target_price = 55

# Create folder for images
if not os.path.exists("Images"):
    os.mkdir("Images")

for url in urls:

    # Get webpage
    response = requests.get(url)

    # Convert HTML into BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Get title
    title = soup.find("h1").text

    # Get price
    price = soup.find("p", class_="price_color").text

    # Convert price into number
    price_value = float(price.replace("Â£", "").replace("£", ""))

    # Get image link
    image = soup.find("img")["src"]

    image_url = "https://books.toscrape.com/" + image.replace("../", "")

    # Download image
    image_data = requests.get(image_url).content

    file_name = title.replace(" ", "_") + ".jpg"

    with open("Images/" + file_name, "wb") as file:
        file.write(image_data)

    # Display details
    print("-----------------------------------")
    print("Title :", title)
    print("Price :", price)
    print("Image URL :", image_url)

    # Compare price
    if price_value <= target_price:
        print("Price is below target price.")
    else:
        print("Price is above target price.")

    print("Image downloaded successfully.")
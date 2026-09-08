import requests
# BeautifulSoup is used to parse and extract information from HTML code.
from bs4 import BeautifulSoup

# Store the URL of the website that we want to scrape.
URL = "https://codegnan.com/"

# This asks the website's server to send us its webpage content.
page = requests.get(URL)

# Check the HTTP status code of the response.
# 200 means the request was successful and the webpage was retrieved successfully.
page.status_code

# The '.text' attribute contains the HTML content returned by the server.
htmlCode = page.text
print(htmlCode)

# 'html.parser' tells BeautifulSoup to use Python's built-in HTML parser.
soup = BeautifulSoup(htmlCode, 'html.parser')

# Print the website title.
title = soup.title.text
print("Website Title:", title)

# Find all <h3> heading tags from the webpage.
headings = soup.find_all('h3')

for heading in headings:
    # Get only the text inside the <h3> tag.
    print(heading.text.strip())

# Find all <h1> heading tags from the webpage.
headings = soup.find_all('h1')

for heading in headings:
    # Extract and print the heading text.
    print(heading.text.strip())

# Find all <h2> heading tags from the webpage.
headings = soup.find_all('h2')

for heading in headings:
    # Extract and print the text inside each <h2> tag.
    print(heading.text.strip())

# Find all <a> tags from the webpage..
links = soup.find_all('a')

# Take only the first 11 links from the list.
for link in links[:11]:
    print(link.get("href"))

# Find all <img> tags from the webpage.
images = soup.find_all("img")

# Take only the first 10 images from the webpage.
for image in images[:10]:
    print(image.get("src"))

# Search for a <meta> tag whose 'name' attribute is 'description'.
description = soup.find(
    "meta",
    attrs={"name": "description"}
)

if description:
    # Print a heading to identify the information being displayed.
    print("Description")
    print(description.get("content"))

# Find every HTML tag present on the webpage.
for tag in soup.find_all():
    # Check whether the current HTML tag has a 'class' attribute.
    if tag.get("class"):
        # Print the class/classes assigned to the HTML tag.
        print(tag.get("class"))

# Find all <script> tags from the webpage.
scripts = soup.find_all("script")

for script in scripts:
    # Get the value of the 'src' attribute.
    print(script.get("src"))

# Find the first <img> tag on the webpage.
logo = soup.find("img")
print(logo.get("src"))

# Find the <meta> tag used for the Open Graph image.
# og:image is commonly used to specify the image shown when a webpage is shared
# on social media platforms.
og_image = soup.find(
    "meta",
    property="og:image"
)

# Get the 'content' attribute of the og:image tag.
print(og_image["content"])

# Find all <li> elements from the webpage..
menus = soup.find_all("li")

# Take only the first 20 list items.
for menu in menus[:20]:
# Extract and print the text inside each list item.
    print(menu.text.strip())

# Find all <p> tags from the webpage.
paragraphs = soup.find_all("p")

# Take only the first 10 paragraphs.
for p in paragraphs[:10]:
    # Extract and print the text inside each paragraph.
    print(p.text.strip())

# Find all <button> elements from the webpage.
buttons = soup.find_all("button")

for b in buttons:
# Extract and print the text displayed inside each button.
    print(b.text.strip())
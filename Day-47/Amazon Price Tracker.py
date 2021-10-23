from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

url= "https://www.amazon.com/Acer-A515-46-R14K-Quad-Core-Processor-Backlit/dp/B08VKNVDDR/ref=sr_1_3?dchild=1&keywords=Laptop&qid=1634808365&sr=8-3&th=1"
header = {
"Accept-Language": "YOUR SYSTEMs ACCEPTLANGUAGE",
"User-Agent": "Your System Heade"
}
response=requests.get(url,headers= header)

soup = BeautifulSoup(response.text, "lxml")

price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price_without_currency = float(price.split("$")[1])
title = soup.find(id="productTitle").get_text()
print(title)

MYPRICE = 400

if price_without_currency < MYPRICE:
    message = f"{title} is now {price}. Nishi"

    with smtplib.SMTP("smtp.mail.yahoo.com",port=587) as connection:
        connection.starttls()
        result=connection.login("YourMAILID", "Password")
        connection.sendmail(
            from_addr = "YOURMAILID",
            to_addrs="MAILId_TO_WHICH_YOU_WANNA_SEND",
            msg=f"Subject: Amazon Price Alert!{message} go and shop immediately: {url}"
        )

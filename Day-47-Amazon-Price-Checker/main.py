from bs4 import BeautifulSoup
import smtplib
import requests
import os

# get response from our amazon link and return the text
response = requests.get('https://www.amazon.ca/Apple-Cancellation-Transparency-Personalized-High-Fidelity/dp/B0CHWRXH8B/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.KMgLWCW2IVo_3D8pvFXujr35CxjhGtGoevrs6xE88kEFRocBFVEBX9H63G1gRnzZEKy59fMpPFdWBSIFiSLAZFNDMZqzGRGpiwC_9IjzTKIkV2dJ0DOvu0Gc8VvBr5OoFIAN6cGAKLdNYiID_s2CughPkKgTO4J-8B7HVNjGXdmPe5eHCVkBEeXK7w3qV2RF2vsgUJEYaMRbyHGPTsj9CLFhbmnclPkiTxA3D5obP_Oopzw0LeCuik5FPW7b1St3da2Ii5FGQuwWWbY0rkVCYnGaUlZ2Zx2W77hId47XAlc.DdtyJXMxpY3rLxPFP0PoGi1pbNgsB6Q07o7OeOQ9fgg&dib_tag=se&keywords=AirPods+pro&qid=1731800512&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1' ,
                        headers={"Accept-Language":"en-US",
                                 "User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
                                 })
amazon_text = response.text

# sorts through the response to find relevant html information
soup = BeautifulSoup(amazon_text, 'html.parser')

# selects the price from the html info using an html selector and converts it to a floating point number
Price = float(soup.find(class_="a-offscreen").get_text().split('$')[1])
print(Price)

if Price < 260:
    print("sending email...")
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        # secures connection
        connection.starttls()
        connection.login(user=os.environ["EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL"],
                            to_addrs='jaganlidder40@gmail.com',
                            msg=f"Subject:Price Drop!\n\nThe price for your AirPods Pro 2 is now {Price}. "
                                f"Buy them here: https://www.amazon.ca/Apple-Cancellation-Transparency-Personalized-High-Fidelity/dp/B0CHWRXH8B/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.KMgLWCW2IVo_3D8pvFXujr35CxjhGtGoevrs6xE88kEFRocBFVEBX9H63G1gRnzZEKy59fMpPFdWBSIFiSLAZFNDMZqzGRGpiwC_9IjzTKIkV2dJ0DOvu0Gc8VvBr5OoFIAN6cGAKLdNYiID_s2CughPkKgTO4J-8B7HVNjGXdmPe5eHCVkBEeXK7w3qV2RF2vsgUJEYaMRbyHGPTsj9CLFhbmnclPkiTxA3D5obP_Oopzw0LeCuik5FPW7b1St3da2Ii5FGQuwWWbY0rkVCYnGaUlZ2Zx2W77hId47XAlc.DdtyJXMxpY3rLxPFP0PoGi1pbNgsB6Q07o7OeOQ9fgg&dib_tag=se&keywords=AirPods+pro&qid=1731800512&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1  "
                            )
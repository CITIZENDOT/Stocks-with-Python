from bs4 import BeautifulSoup as BS
import requests
import datetime

url = "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI"             # Reliance Industries | Source: moneycontrol.com 
API_KEY = "API_KEY_HERE"                                                                                # Here I am using fast2sms API, Enter your API Key.
mobile_no = "YOUR_MOBILE_NUMBER"
threshold = 1600                                                                                        # Choose your Threshold Value Here

while True:
    r = requests.get(url)
    d = datetime.datetime.now()
    soup = BS(r.text, features="html.parser")
    li = soup.findAll("span", {"class": "span_price_wrap stprh grn_hilight grnclr"})                    # Scraping the Stock price from Source
    
    if d.weekday() == 5 or d.weekday() == 6:                                                            # Saturday and Sunday
        last_checked = soup.findAll("span", {"class": "display_lastupd"})
        print("Stocks don't operate today")
        print("Giving you the Last checked price: ")
        print("₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹")
        print("|")
        print("--> BSE: ₹", li[0].text, "  | Last checked at  ", last_checked[0].text, sep='')          # Bombay Stock Exchange
        print("|")
        print("--> NSE: ₹", li[1].text, "  | Last checked at  ", last_checked[1].text, sep='')          # National Stock Exchange
        print("|")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Bye, See you on Monday")
        exit(0)
    
    print("₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹")
    print("|")
    print("-->", d.strftime("%B %d, %Y | %I:%M:%S %p"))
    print("|")
    print("-->BSE: ", li[0].text)                                                                       # Bombay Stock Exchange
    print("|")
    print("-->NSE: ", li[1].text)                                                                       # National Stock Exchange
    print("|")
    if min(float(li[0].text), float(li[1].text)) <= threshold:
        message_string = "%0aCurrent Price of Reliance Industries stock is ₹" + str(min(float(li[0].text), float(li[1].text))) + "%0aHurry Up!!!" + "%0aPrice at " + d.strftime("%B %d, %Y | %I:%M:%S %p")
        message_url = "https://www.fast2sms.com/dev/bulk?authorization=" + API_KEY + "&sender_id=FSTSMS&message=" + message_string + "&language=unicode&route=p&numbers=" + mobile_no + "&flash=0"
        message_request = requests.get(message_url)
        print("Stock Price lowered down to Threshold")
        print("Message Sent")
        print("The Program is terminated, Since It had given you the result")
        print("Rerun it again, to get notified about updates")
        break                                                                                           # Program Stops After getting Stock Price less than or equal to Threshold. So You have to rerun the program, After getting a message.
    else:
        print("Price is higher than Required Value")
        print("Rechecking...")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

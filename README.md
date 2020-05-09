# Trade Stocks with the help of Python

## Introduction

Ever Thought of Buying Shares of your Dream Company, When their share price got down?
But It is not that simple, to keep looking at stock prices all the time for the whole Business Week. Right?

And Also, If that particular company is reliable, Then that Low price wouldn't last long enough(atleast even for 1 day)

So, You want to get notified very fastly, whenever the stock is lowered down than a particular value.(Threshold)

This script helps you exacty in that situation.

## Regarding Sources of the Script

* This Script gives the share price according to [MoneyControl](https://www.moneycontrol.com/) Website.

* This Script uses [FAST2SMS](https://www.fast2sms.com/) API to send SMS to your Mobile Phone.
    *FAST2SMS is not a free SMS service, But still It had attractive features for new subscribers. It gives ₹55 as bonus credit. And It charges as less as 20 paise for each SMS. So, I recommend to use this API.*

## Code Construction

Install bs4 from pip package.

```bash
pip3 install bs4
```

**url**

Open [MoneyControl](https://www.moneycontrol.com/) Website and search for your desired company.
Now change the value of "url" variable(in the code) to URL of the page.

**API_KEY**

Change the "API_KEY" variable to your [FAST2SMS](https://www.fast2sms.com/) API Key.

It can be found [here](https://www.fast2sms.com/dashboard/dev-api)
    *Only If you logged in.*

**mobile_no**

Change this variable to your Mobile Number to recieve SMS Notifications.

**threshold**

Remember that Threshold in Introduction?
Change it with that value.

------------------------------

You are ready to go!

Run this program on a mobile phone or server continuously to monitor stocks realtime. The program will do the work for you.

*You can get rid of print statements by commenting them.*

```sh
python3 main.py
```

## Screenshots

Example:

Company:    Reliance Industries
Threshold:  ₹1000

__*On Working Days(Monday to Friday):*__
![Normal Working Day](https://user-images.githubusercontent.com/52322531/81465020-5e5dd480-91e4-11ea-811e-4f7309207013.png)

Consider It has reached less than or equal to threshold Value:
*I am changing Threshold to ₹1600*

![Recieved the Message](https://user-images.githubusercontent.com/52322531/81465647-08d7f680-91e9-11ea-909e-1b91e6a8a024.png)

And, Here is the Message

![Message](https://user-images.githubusercontent.com/52322531/81465760-ea262f80-91e9-11ea-9e75-b18e839f06f5.png)

__*On Weekends(Saturday and Sunday):*__

![On Holdays](https://user-images.githubusercontent.com/52322531/81465829-9c5df700-91ea-11ea-81e2-b89eb7f6a075.png)

### Don't Forget to star this repository.
from requests_html import HTMLSession
import smtplib
import time
import secure

def getInfo():
    s = HTMLSession()
    r=s.get('secure.website')
    r.html.render(timeout = 0)

    title_full = r.html.xpath(secure.title,first = True).text
    title_short = title_full[:23]
    price_str = r.html.xpath(secure.price,first=True).text
    price = float(price_str.strip('$'))
    #print(price)
    if price < 190.00:
        sendMail()
    else:
        print(f"Sorry but you dont have enough money to purchase the {title_short} :'(.")


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',secure.num)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('secure.email','secure.password')

    subject = 'HEY! PRICE OF Jabra Elite Earbuds FELL DOWN'
    body = f'Check new price at:{secure.newPrice}'

    msg = f'Subject = {subject}\n\n{body}' 

    server.sendmail(
        'secure.email',
        'secure.email',
        msg
    )
    
    print('Email has been sent')

    server.quit()


getInfo()

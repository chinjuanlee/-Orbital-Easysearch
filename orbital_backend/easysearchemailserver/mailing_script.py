# Python code to illustrate Sending mail from 
# your Gmail account 
from smtplib import SMTP
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import functools

def send_email(receiver_email, mailing_items):
    #Creates SMTP session
    s = SMTP('smtp.gmail.com', 587)
  
    #Start TLS for security
    s.starttls()

    #Authentication
    s.login("noreplyeasysearch@gmail.com", "@Easysearch123")
    
    #Email details
    msg = MIMEMultipart('alternative')
    msg['From'] = "noreplyeasysearch@gmail.com"
    msg['To'] = receiver_email
    msg['Subject'] = "[EasySearch] WishList Notification Update"
    #Message to be content
    def textIterator(item_details):
        text = "The product [ {} ] on your wishlist has dropped in price!\n".format(item_details["title"])
        return text
    def htmlIterator(item_details):
        html = """
            <img src={} alt="product image" width="100" height="100"><br>
            <p>The product [ {} ] is on sale at {}!<br>
        """.format(item_details["image"],item_details["title"], item_details["price"] )
        return html
    text = "Hi!\n"+ functools.reduce(lambda a,b: a + b, map(textIterator, mailing_items)) + "Link to easysearch:\nhttps://easysearch.vercel.app"

    html = """
        <html>
        <head><h1>Products on your wishlist have dropped in price!</h1></head>
        <body>""" + functools.reduce(lambda a,b: a + b, map(htmlIterator, mailing_items)) + """Click <a href="https://easysearch.vercel.app/wishlist">link</a> to access your wishlist.
            </p>
        </body>
        </html>"""
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    #Sending the mail
    s.send_message(msg)
  
    #Terminating the session
    s.quit()

test_dict = {'image': 'https://i.ezbuy.sg/Fpi-JkR3dire2fqsF5lDQtFhqCBt',
             'item': 'airpods',
             'price': '$264.00',
             'ratings': '5 stars',
             'store': 'ezbuy',
             'url': 'www.ezbuy.sg/product/427301306',
             'title': '[On Sale] Apple AirPods Pro | 1 Year Local Singapore Warranty'}


#send_email('chinjuan1999@gmail.com', [test_dict, test_dict, test_dict])

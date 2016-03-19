import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.Utils import COMMASPACE, formatdate

# me == my email address
# you == recipient's email address
#assert type(to)==list
def send_mail(to,fro,sub,html,html_text=None):
    #to = ['Chacha <sakhawat.sobhan@gmail.com>', 'mohua <mohua.amin@gmail.com>']
    #fro = "mohua@finder-lbs.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = sub
    msg['From'] = fro #formataddr((str(Header(u'Finder Tracking', 'utf-8')), fro)) #fro
    msg['To'] = COMMASPACE.join(to)

    # Create the body of the message (a plain-text and an HTML version).
    #text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    
    # html = """\
    # <html>
    #   <head>
    #   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    #   <title>html title</title>
    #   <style type="text/css" media="screen">
    #     table{
    #         background-color: #FFFFFF;
    #         empty-cells:hide;
    #     }
    #     td.cell{
    #         background-color: white;
    #     }
    #   </style>
    #   </head>
    #   <body>
    #   Hi there, <br>
    #   I am glad that you have recieved this mail. No need to Reply.<br> 
    #   <table style="border: none;">
    #         <tr><td><img src="https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-xap1/v/t1.0-9/10653783_630992580346934_4425113809694913086_n.png?oh=3d14f24f768faa3304007efec66a491f&oe=554977A4&__gda__=1431036280_82a9361e9479848e96037d3e19055afd" alt="Sample Image" style="float:left;width:45px;height:35px"></td></tr> 
    #   </table><br>
    #   <br>Regards<br>The Finder Team <br>Stay in touch ^_^<br>
    #   </body>
    # </html>
    # """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(html_text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('localhost')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(fro, to, msg.as_string())
    s.quit()

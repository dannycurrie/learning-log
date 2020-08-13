import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import config


def createMsg(logs, addr):
    today = datetime.today().strftime('%Y-%m-%d')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Learning Logs {today}"
    msg['From'] = addr
    msg['To'] = addr
    html = f"""\
        <html>
        <head></head>
        <body>
            <ul>
        """
    for log in logs:
        if(log.startswith('Tag:')):
            html = html + f'<h4>{log}</h4>'
        else:
            html = html + f'<li>{log}</li>'
    html = html + """
        </ul>
    </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))
    return msg


def sendMail(logs):
    server = smtplib.SMTP(host=config.HOST, port=config.PORT)
    server.starttls()
    server.login(config.ADDR, config.PWD)
    msg = createMsg(logs, config.ADDR)
    server.sendmail(config.ADDR, config.ADDR, msg.as_string())

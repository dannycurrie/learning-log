import smtplib
import config


def sendMail(msg):
    server = smtplib.SMTP(host=config.HOST, port=config.PORT)
    server.starttls()
    server.login(config.ADDR, config.PWD)
    server.sendmail(config.ADDR, config.ADDR, msg)

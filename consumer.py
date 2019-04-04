#!/usr/bin/env python
import pika
import traceback, sys, time
import smtplib
from secret import login, password
import time
import json

def callback(ch, method, properties, body):
    body_ = {}
    body_ = dict(eval(body))
    email = body_['email']
    text = body_['text']
    print(email)
    print()
    print(text)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(login,password)
    smtpObj.sendmail(login, email, text)
    smtpObj.quit()

params = pika.ConnectionParameters('localhost', 5672)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='random_queue')
channel.basic_consume(callback, queue='random_queue', no_ack=True)

while True:
    try:
        channel.start_consuming()
    except pika.exceptions.ConnectionClosed:
        channel.stop_consuming()
    except Exception as ex:
        channel.stop_consuming()
print(ex)

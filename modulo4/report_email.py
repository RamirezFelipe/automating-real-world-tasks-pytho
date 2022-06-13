#!/usr/bin/env python3
import os
import datetime
import reports
import email.message
import mimetypes
import emails

def read_descriptions(folder):
    body = "<br/>"
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder,file), 'r') as texto:
                lineas = texto.readlines()
                body +="name: " + lineas[0].strip() + "<br/>"
                body += "weight: " + lineas[1].strip() + "<br/>"
                body += "<br/>"
    return body


if __name__ == "__main__":
    body = read_descriptions("supplier-data/descriptions/")
    # crear titulo con el formato Processed Update on {date}
    title = "Processed Update on " + datetime.datetime.now().strftime("%B %d, %Y")
    reports.generate_report("/tmp/processed.pdf", title, body)
    # crear email
    message = emails.generate_mail(send = "automation@example.com",
                            recipient = "student-04-7a032a992120@example.com",
                            subject = "Upload Completed - Online Fruit Store",
                            body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                            attachment_path = "/tmp/processed.pdf")
    #enviar email
    emails.send(message)
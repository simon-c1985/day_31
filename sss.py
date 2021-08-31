import smtplib

my_email = 'ardels@mail.ru'
password = 'mszRqaOPdVxXLVVxQsBf'

connection = smtplib.SMTP('smtp.mail.ru')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs='simon-c@yandex.ru',
                    msg="Subject: Python tes\n\nHello my friend")
connection.close()

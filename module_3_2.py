def send_email (message, recipient, sender = "university.help@gmail.com"):
    a = recipient. find("@")
    a_1 = recipient.endswith(".com")
    a_2 = recipient.endswith(".ru")
    a_3 = recipient.endswith(".not")
    b   = sender. find("@")
    b_1 = sender. endswith(".com")
    b_2 = sender.endswith(".ru")
    b_3 = sender.endswith(".not")
    checking = 0

    if b_1 == True or b_2 == True or b_3 == True or b > 0:
        checking = 1
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

    if checking == 0:
        if a_1 == True or a_2 == True or a_3 == True:
            if a > 0:
                if recipient == sender:
                    print("Нельзя отправить письмо самому себе!")
                else:
                    print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
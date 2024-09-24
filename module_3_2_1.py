
def send_emal(message, recipient, sender = "university.help@gmail.com"):

    if "@" not in recipient or ".com" not in recipient or ".ru" in recipient or ".net" in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif "@" not in sender or ".com" not in sender or ".ru" in sender or ".net" in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        if sender == recipient:
            print("Нельзя отправлять письмо самому себе!")
        else:
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

            else:
                print("Нестандартный отправитель")

send_emal("Это сообщение для проверки связи", "vasyok1337@gmail.com", sender = "university.help@gmail.com")

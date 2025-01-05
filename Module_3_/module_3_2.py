def send_email (message, recipient, *, sender = 'university.help@gmail.com'):
    b = [ ".com", ".ru", ".net"]
    if ('@' in sender) and ('@' in recipient):
        b.append('костыль')
    if any(x in sender for x in b) and any(x in recipient for x in b):
        b.append('костыль')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif (sender != 'university.help@gmail.com') and any(x in sender for x in b):
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

def send_email(massage, recipient, sender = 'university.help@mail.com'):
    if ('@' and ('.com' or '.ru' or '.net')) not in recipient and ('@' and ('.com' or '.ru' or '.net')) not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@mail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print()
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print()
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print()
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
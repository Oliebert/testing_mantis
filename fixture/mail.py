import poplib # для анализа тектса мыла
import email
import time

class MailHelper:


    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password,subject):
        for i in range(5):# 5 попыток для прочтения мыла
            pop =poplib.POP3(self.app.config["james"]["host"])# устанавливаем соединение
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0] # статистич инфа о мылах , [0]- количество писем
            if num >0 :
                for n in range(num):# смотрим письма и сравниваем тему письма с заданной
                    msglines=pop.retr(n+1)[1]#текст письма во втором элементе кортежа
                    msgtext = "\n".join(map(lambda x: x.decode("utf-8"), msglines)) #строчки склеиваем вместе и получаем текст, но мы имеем дело с байтовыми строками,
                                                    # которые нужно перекодировать в обыкновенные
                    msg=email.message_from_string(msgtext) #Return a message object structure from a string
                    if msg.get("Subject")==subject: # если тема письма равна заданной
                        pop.dele(n+1)# помечаем письмо на удаление
                        pop.quit()# закрытие с сохранением, письма помеченные на удаление удалятся только при закрытии
                        return msg.get_payload()# возвращаем тело письма

            pop.close()
            time.sleep(3)

        return None # письмо не пришло (


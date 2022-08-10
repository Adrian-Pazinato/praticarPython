import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587, local_hostname='Adrian')
server.starttls()
server.login("envia.com", "?")
server.sendmail("envia.com", "recebe.com",
                "Subject: Teste de email \n\n SALVE SALVE https://www.youtube.com/watch?v=dQw4w9WgXcQ \r\n Ta tudo certo nessa porra Python do krl tmj \r\n TESTE 123 nn")

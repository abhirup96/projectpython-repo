import smtplib #
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls() #encryption
s.login("abhipython4@gmail.com","Abcd@123456")
s.ehlo() #client establishment
s.sendmail("abhipython4@gmail.com","abhirup.fifa09@gmail.com","helloworld")

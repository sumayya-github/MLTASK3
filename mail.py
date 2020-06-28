import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s = login("sumayyakhatoon58@gmail.com", "summaiya@26")

message = "YOUR ACCURACY IS LESS THAN 90%.TRY AGAIN"

s.sendmail("sumayyakhatoon58@gmail.com","s8355827840@gmail.com", message)

s.quit()

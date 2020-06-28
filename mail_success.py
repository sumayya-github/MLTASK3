import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s = login("sumayyakhatoon58@gmail.com", "summaiya@26")

message_success = "ACHIEVED YOUR DESIRED ACCURACY .CONGRATS!!!!!"

s.sendmail("sumayyakhatoon58@gmail.com", "s8355827840@gmail.com", message_success)

s.quit()

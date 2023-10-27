# import smtplib
#
# my_email = "codewithshrini52@gmail.com"
#
# password = "aeggvjyhimzmkrgl"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                     to_addrs="shrirajnaik58@gmail.com",
#                     msg="Subject:Hello\n\n Your the best ")

# import datetime as dt
#
# now = dt.datetime.now()

# import smtplib
# import datetime as dt
# import random
#
# now = dt.datetime.now()
# weekday = now.weekday()
#
# My_email = "codewithshrini52@gmail.com"
# Password = "dejnnimpwubedehb"
#
# if weekday == 5:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(My_email, Password)
#         connection.sendmail(from_addr=My_email, to_addrs=My_email, msg= f"Monday Motivation\n\n{quote}")

import smtplib, ssl, sys


if sys.argv[1] == "help":
    print("\n[USAGE]\n  python3 massph1sher.py {Your email} {File with target emails} {File with message}\n")
    sys.exit()
senderpass = input("Enter your mail password: ")
senderemail = sys.argv[1]
smtp_server = "smtp.gmail.com"
port = 587
context = ssl.create_default_context()
message = open(sys.argv[3],"r").read()
targetemails = (open(sys.argv[2],"r").read()).splitlines()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo()
    server.login(senderemail, senderpass)
    for i in targetemails:
        server.sendmail(senderemail, i, message)
        print(f"[+] Sent message to {i}")
except Exception as e:
    print(e)
finally:
    server.quit() 

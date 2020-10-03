import yagmail, random

def otp(receiver_email):
    n=str(random.randint(10000,99999))
    s=''
    for i in n:
        s=s+i+"\u0332"
    sender_email= "testdevelop12@gmail.com"
    subject="Verification code"
    password="good_work7"
    yag=yagmail.SMTP({sender_email:"Continental Bank"},password=password)
    contents="Your otp for verification of Continental Bank account is "+s+".\n Do not share this with anyone."
    yag.send(receiver_email,subject,contents)


'''Instruction:
1)To use yagmail module u need to install it:
type "pip install yagmail" in your command prompt
2)Need an active internet connection to run this program'''


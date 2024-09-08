import yagmail
import os
import datetime

date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)

# Define the recipient's email address
receiver = "chandanchand769@gmail.com"  # Replace with the actual recipient's email

# mail information
yag = yagmail.SMTP("Ankitroycr103@gmail.com", "hsav fknv hzww ejia")

# sent the mail
yag.send(
    to=receiver,
    subject=sub,
    contents="Attendance report attached.",
    attachments=filename
)
print("Email Sent!")

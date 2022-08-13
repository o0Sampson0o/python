from winotify import Notification, audio
import csv
import datetime
import time
import schedule


############################################### function definition


icon_path = r"C:\Users\User\Everything\Coding\vscode\projects\python\scdl\img\icon.ico"

def Noti(Title, Msg):
    toast = Notification(   app_id = "Reminder",
                            title = Title,
                            msg = Msg,
                            duration = "short",
                            icon = icon_path)
                        
    toast.set_audio(audio.SMS, loop=False)
    toast.show()


######################################## reading activities from csv


file = "task.csv"
header = []
rows = []

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)


############################################## appending Work to schedule


today = datetime.datetime.now()
now_h = int(today.strftime('%H'))
now_m = int(today.strftime('%M'))
now_d = '{}-{}'.format(today.strftime('%d'), today.strftime('%b'))

for content in rows:
    d = content[header.index("Date")]
    h = int(content[header.index("Time")][0:-3])
    m = int(content[header.index("Time")][-2:])
    if (d == now_d and h >= now_h and m >= now_m):
        schedule.every().day.at(content[header.index("Time")]).do(  Noti,
                                                                    content[header.index("Title")],
                                                                    content[header.index("Description")])


############################################## start loop


while True:
    schedule.run_pending()
    time.sleep(1)
token = '1869807556:AAHpj1MB4uoGRcghHNAyiMGMUj_XoyXJ3HM'
import requests
import json
import os
import matplotlib.pyplot as plt
url = f'https://api.telegram.org/bot{token}/'
from flask import Flask
from flask import request
from flask import Response
app = Flask(__name__)
def get_all_updates():
    response = requests.get(url+'getUpdates')
    return response.json()
def get_last_update(allupdates):
    return allupdates['result'][-1]
def get_chat_id(update):
    return update['message']['chat']['id']
def sendMessage(chat_id,text):
    sendData={
        'chat_id':chat_id,
        'text':text
    }
    response=requests.post(url+'sendMessage',sendData)
    return response
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        msg = request.get_json()   # dict
        chat_id = get_chat_id(msg)
        text = msg['message'].get('text','')
        if text =='/start':
            sendMessage(chat_id,'سلام، امیدواریم به کمک این بات گام مثبتی در جهت بهبود زندگی خود بردارید')
            sendMessage(chat_id,' اهمیت شناخت تله‌های زندگی: در طول زندگی تحت تاثیر ژنتیک، نوع تربیت خانواده، رخدادهای محیطی که برای ما اتفاق می‌افتد باعث می‌شود طرحواره‌هایی در شخصیت ما شکل بگیرد‌ به این طرحواره‌ها تله‌های زندگی ‌می‌گوییم که رفتارهای ما را در موقعیت‌های مختلف تعیین می‌کند که اکثر آن‌ها ناسالم و غیرانطباقی هستند، ولی چون فرد از کودکی به ‌آن عادت کرده با آن احساس راحتی می‌کند اما وجود آن باعث تحریف واقعیت‌های زندگی می‌شود و این مهم‌ترین دلیل برای شناخت و درمان طرحواره‌هاست')
            sendMessage(chat_id,'برای ورود به تست عبارت "ورود"را ارسال کنید و برای خروج از بات عبارت"خروج"را ارسال کنید')
        elif text =='ورود':
            sendMessage(chat_id,'عدد تست موردنظرتان را ارسال بفرمائید,\n1. تله زندگی رهاشدگی,\n2. تله زندگی بی‌اعتمادی و بدرفتاری,\n3. تله زندگی محرومیت هیجانی,\n4. تله زندگی طرد اجتماعی,\n5. تله زندگی وابستگی,\n6. تله زندگی آسیب‌پذیری,\n7. تله زندگی تقص/شرم,\n8. تله زندگی اطاعت,\n9. تله زندگی معیارهای سخت‌گیرانه,\n10. تله زندگی استحقاق')
        elif text=='خروج':
            sendMessage(chat_id,'موفق باشید، خدانگهدار')
        elif text=='1': #سوال اول
            javabsoal =read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('1')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='2': #سوال اول
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('2')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='3': #سوال اول
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('3')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='4':
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('4')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='5':
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('5')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='6':
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('6')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='7':
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('7')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='8':
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('8')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='9':
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('9')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='10':
            javabsoal = read_json()
            if len(javabsoal)==0:
                username = msg['message']['from']['username']
                javabsoal[username]=[]
                javabsoal[username].append('10')
                write_json(javabsoal)
                sendMessage(chat_id,'برای شروع تست "+" را ارسال کنید')
            else:
                pass
        elif text=='+': #soal2
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==1:
                sendMessage(chat_id,'به سوالات زیر از 1 تا 5 امتیاز بدهید')
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'هیچ زن یا مردی مرا دوست ندارد، مخصوصا اگر مرا بشناسد.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'احساس می‌کنم که دیگران می‌خواهند به من صدمه بزنند یا از من سوءاستفاده کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'من به عشق بیشتری در زندگی‌ام نیاز دارم.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'در موقعیت‌های اجتماعی، خیلی کم رو و خجالتی هستم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'زمانی که می‌خواهم مسئولیت انجام کارهای زندگی روزمره ام را بر عهده بگیرم، احساس می‌کنم بچه‌ام تا آدم بزرگسال.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نمی توانم خودم را از این فکر خلاص کنم که هر لحظه ممکن است اتفاق بدی بیفتد.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'هیچ زن یا مردی مرا دوست ندارد، مخصوصا اگر مرا بشناسد.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'اجازه می‌دهم که دیگران مرا کنترل کنند.')
                elif javabsoal[username][0]=='9':
                    sendMessage(chat_id,'همیشه باید در رتبه اول باشم. باید در حداکثر کارها بهترین باشم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'برای من خیلی سخت که دیگران در مقابل درخواست‌هایم جواب منفی بدهند.')
                else:
                    pass
                write_json(javabsoal)
#................................................................................................................
        elif text=='1': #soal2 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==1:
                javabsoal[username].append('1') #dovomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'در طول زندگی، افرادی که به من نزدیک شده‌اند، از من سوءاستفاده کرده‌اند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'واقعا هیچ‌کس مرا درک نمی‌کند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,' در مهمانی‌ها و در حضور دیگران، احساس می‌کنم کودن و خسته کننده هستم انگار نمی‌داند که چی می‌خواهم بگویم. ')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'در انجام کارهای شخصی‌ام توانایی لازم را ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'احساس می‌کنم هر لحظه می‌تواند حادثه‌ای ناگوار رخ بدهد.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'می‌ترسم اگر مطابق میل دیگران عمل نکنم، دست به تلافی و انتقام‌جویی بزنند یا از دست من عصبانی شوند و مرا طرد کنند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' کمتر کاری مورد رضایت و قبول من قرار می‌گیرد.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'وقتی که نتوانم به خواسته‌هایم برسم، عصبانی می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal2 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==1:
                javabsoal[username].append('2') #dovomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'در طول زندگی، افرادی که به من نزدیک شده‌اند، از من سوءاستفاده کرده‌اند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'واقعا هیچ‌کس مرا درک نمی‌کند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,' در مهمانی‌ها و در حضور دیگران، احساس می‌کنم کودن و خسته کننده هستم انگار نمی‌داند که چی می‌خواهم بگویم. ')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'در انجام کارهای شخصی‌ام توانایی لازم را ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'احساس می‌کنم هر لحظه می‌تواند حادثه‌ای ناگوار رخ بدهد.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'می‌ترسم اگر مطابق میل دیگران عمل نکنم، دست به تلافی و انتقام‌جویی بزنند یا از دست من عصبانی شوند و مرا طرد کنند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' کمتر کاری مورد رضایت و قبول من قرار می‌گیرد.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'وقتی که نتوانم به خواسته‌هایم برسم، عصبانی می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal2 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==1:
                javabsoal[username].append('3') #dovomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'در طول زندگی، افرادی که به من نزدیک شده‌اند، از من سوءاستفاده کرده‌اند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'واقعا هیچ‌کس مرا درک نمی‌کند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,' در مهمانی‌ها و در حضور دیگران، احساس می‌کنم کودن و خسته کننده هستم انگار نمی‌داند که چی می‌خواهم بگویم. ')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'در انجام کارهای شخصی‌ام توانایی لازم را ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'احساس می‌کنم هر لحظه می‌تواند حادثه‌ای ناگوار رخ بدهد.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'می‌ترسم اگر مطابق میل دیگران عمل نکنم، دست به تلافی و انتقام‌جویی بزنند یا از دست من عصبانی شوند و مرا طرد کنند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' کمتر کاری مورد رضایت و قبول من قرار می‌گیرد.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'وقتی که نتوانم به خواسته‌هایم برسم، عصبانی می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal2 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==1:
                javabsoal[username].append('4') #dovomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'در طول زندگی، افرادی که به من نزدیک شده‌اند، از من سوءاستفاده کرده‌اند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'واقعا هیچ‌کس مرا درک نمی‌کند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,' در مهمانی‌ها و در حضور دیگران، احساس می‌کنم کودن و خسته کننده هستم انگار نمی‌داند که چی می‌خواهم بگویم. ')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'در انجام کارهای شخصی‌ام توانایی لازم را ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'احساس می‌کنم هر لحظه می‌تواند حادثه‌ای ناگوار رخ بدهد.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'می‌ترسم اگر مطابق میل دیگران عمل نکنم، دست به تلافی و انتقام‌جویی بزنند یا از دست من عصبانی شوند و مرا طرد کنند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' کمتر کاری مورد رضایت و قبول من قرار می‌گیرد.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'وقتی که نتوانم به خواسته‌هایم برسم، عصبانی می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal2 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==1:
                javabsoal[username].append('5') #dovomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'در طول زندگی، افرادی که به من نزدیک شده‌اند، از من سوءاستفاده کرده‌اند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'واقعا هیچ‌کس مرا درک نمی‌کند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,' در مهمانی‌ها و در حضور دیگران، احساس می‌کنم کودن و خسته کننده هستم انگار نمی‌داند که چی می‌خواهم بگویم. ')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'در انجام کارهای شخصی‌ام توانایی لازم را ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'احساس می‌کنم هر لحظه می‌تواند حادثه‌ای ناگوار رخ بدهد.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ذاتا آدم مشکل‌دار و بی‌ارزشی هستم، لیاقت عشق دیگران را ندارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'می‌ترسم اگر مطابق میل دیگران عمل نکنم، دست به تلافی و انتقام‌جویی بزنند یا از دست من عصبانی شوند و مرا طرد کنند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' کمتر کاری مورد رضایت و قبول من قرار می‌گیرد.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'وقتی که نتوانم به خواسته‌هایم برسم، عصبانی می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
                
#......................................................................................................
        elif text=='1': #soal3 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==2:
                javabsoal[username].append('1') #sevomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'دیگران دیر یا زود به من خیانت می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' اغلب تمایل دارم با کسانی رابطه برقرار کنم که بی‌عاطفه و مهرگسل هستند و نیازهای عاطفی مرا بر‌آورده نمی‌سازند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'دوستانم از هر نظر مثل (قیافه، محبوبیت، ثروت، منزلت اجتماعی، تحصیلات و شغل) از من بهترند.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم از پس انجام کارها برآیم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که آواره خیابان‌ها شوم یا بی‌خانمان گردم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'احساس می‌کنم تصمیم‌های مهم زندگی‌ام را من نگرفته‌ام.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'هرکاری را باید طبق نظم خاص خودم و در حد عالی انجام بدهم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'من آدمی خاص هستم و نباید از قواعد و مقررات متداول، پیروی کنم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal3 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==2:
                javabsoal[username].append('2') #sevomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'دیگران دیر یا زود به من خیانت می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' اغلب تمایل دارم با کسانی رابطه برقرار کنم که بی‌عاطفه و مهرگسل هستند و نیازهای عاطفی مرا بر‌آورده نمی‌سازند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'دوستانم از هر نظر مثل (قیافه، محبوبیت، ثروت، منزلت اجتماعی، تحصیلات و شغل) از من بهترند.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم از پس انجام کارها برآیم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که آواره خیابان‌ها شوم یا بی‌خانمان گردم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'احساس می‌کنم تصمیم‌های مهم زندگی‌ام را من نگرفته‌ام.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'هرکاری را باید طبق نظم خاص خودم و در حد عالی انجام بدهم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'من آدمی خاص هستم و نباید از قواعد و مقررات متداول، پیروی کنم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal3 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==2:
                javabsoal[username].append('3') #sevomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'دیگران دیر یا زود به من خیانت می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' اغلب تمایل دارم با کسانی رابطه برقرار کنم که بی‌عاطفه و مهرگسل هستند و نیازهای عاطفی مرا بر‌آورده نمی‌سازند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'دوستانم از هر نظر مثل (قیافه، محبوبیت، ثروت، منزلت اجتماعی، تحصیلات و شغل) از من بهترند.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم از پس انجام کارها برآیم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که آواره خیابان‌ها شوم یا بی‌خانمان گردم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'احساس می‌کنم تصمیم‌های مهم زندگی‌ام را من نگرفته‌ام.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'هرکاری را باید طبق نظم خاص خودم و در حد عالی انجام بدهم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'من آدمی خاص هستم و نباید از قواعد و مقررات متداول، پیروی کنم.')
                else:
                    pass 
                write_json(javabsoal)
        elif text=='4': #soal3 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==2:
                javabsoal[username].append('4') #sevomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'دیگران دیر یا زود به من خیانت می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' اغلب تمایل دارم با کسانی رابطه برقرار کنم که بی‌عاطفه و مهرگسل هستند و نیازهای عاطفی مرا بر‌آورده نمی‌سازند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'دوستانم از هر نظر مثل (قیافه، محبوبیت، ثروت، منزلت اجتماعی، تحصیلات و شغل) از من بهترند.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم از پس انجام کارها برآیم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که آواره خیابان‌ها شوم یا بی‌خانمان گردم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'احساس می‌کنم تصمیم‌های مهم زندگی‌ام را من نگرفته‌ام.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'هرکاری را باید طبق نظم خاص خودم و در حد عالی انجام بدهم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'من آدمی خاص هستم و نباید از قواعد و مقررات متداول، پیروی کنم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal3 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==2:
                javabsoal[username].append('5') #sevomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'دیگران دیر یا زود به من خیانت می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' اغلب تمایل دارم با کسانی رابطه برقرار کنم که بی‌عاطفه و مهرگسل هستند و نیازهای عاطفی مرا بر‌آورده نمی‌سازند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'دوستانم از هر نظر مثل (قیافه، محبوبیت، ثروت، منزلت اجتماعی، تحصیلات و شغل) از من بهترند.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم از پس انجام کارها برآیم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که آواره خیابان‌ها شوم یا بی‌خانمان گردم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'رازهای سر به مُهرم را با هیچ‌کس، حتی عزیزان خودم، در میان نمی‌گذارم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'احساس می‌کنم تصمیم‌های مهم زندگی‌ام را من نگرفته‌ام.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'هرکاری را باید طبق نظم خاص خودم و در حد عالی انجام بدهم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'من آدمی خاص هستم و نباید از قواعد و مقررات متداول، پیروی کنم.')
                else:
                    pass
                write_json(javabsoal)
#..................................................................................................................
        elif text=='1': #soal4 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==3:
                javabsoal[username].append('1') #chaharomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'احساس می‌کنم که باید در برابر دیگران از خودم سخت محافظت کنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'احساس می‌کنم حتی صمیمی‌ترین افراد زندگی‌ام نیز پاسخگوی نیازهای عاطفی من نیستند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'ترجیح میدهم بیخیال اکثر فعالیت‌های اجتماعی شوم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'معتقدم که دیگران بهتر از خودم می‌توانند از من مراقبت کنند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا مورد حمله جیب‌برها، دوست‌ها یا جنایتکاران قرار بگیرم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت توقع دارم که دیگران به حقوق من احترام بگذارند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'باید از تمام وقت‌هایم، بهترین استفاده را ببرم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'نیازهای من در اولویت است.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal4 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==3:
                javabsoal[username].append('2') #chaharomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'احساس می‌کنم که باید در برابر دیگران از خودم سخت محافظت کنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'احساس می‌کنم حتی صمیمی‌ترین افراد زندگی‌ام نیز پاسخگوی نیازهای عاطفی من نیستند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'ترجیح میدهم بیخیال اکثر فعالیت‌های اجتماعی شوم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'معتقدم که دیگران بهتر از خودم می‌توانند از من مراقبت کنند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا مورد حمله جیب‌برها، دوست‌ها یا جنایتکاران قرار بگیرم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت توقع دارم که دیگران به حقوق من احترام بگذارند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'باید از تمام وقت‌هایم، بهترین استفاده را ببرم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'نیازهای من در اولویت است.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal4 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==3:
                javabsoal[username].append('3') #chaharomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'احساس می‌کنم که باید در برابر دیگران از خودم سخت محافظت کنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'احساس می‌کنم حتی صمیمی‌ترین افراد زندگی‌ام نیز پاسخگوی نیازهای عاطفی من نیستند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'ترجیح میدهم بیخیال اکثر فعالیت‌های اجتماعی شوم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'معتقدم که دیگران بهتر از خودم می‌توانند از من مراقبت کنند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا مورد حمله جیب‌برها، دوست‌ها یا جنایتکاران قرار بگیرم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت توقع دارم که دیگران به حقوق من احترام بگذارند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'باید از تمام وقت‌هایم، بهترین استفاده را ببرم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'نیازهای من در اولویت است.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal4 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==3:
                javabsoal[username].append('4') #chaharomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'احساس می‌کنم که باید در برابر دیگران از خودم سخت محافظت کنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'احساس می‌کنم حتی صمیمی‌ترین افراد زندگی‌ام نیز پاسخگوی نیازهای عاطفی من نیستند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'ترجیح میدهم بیخیال اکثر فعالیت‌های اجتماعی شوم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'معتقدم که دیگران بهتر از خودم می‌توانند از من مراقبت کنند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا مورد حمله جیب‌برها، دوست‌ها یا جنایتکاران قرار بگیرم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت توقع دارم که دیگران به حقوق من احترام بگذارند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'باید از تمام وقت‌هایم، بهترین استفاده را ببرم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'نیازهای من در اولویت است.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal4 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==3:
                javabsoal[username].append('5') #chaharomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'احساس می‌کنم که باید در برابر دیگران از خودم سخت محافظت کنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'احساس می‌کنم حتی صمیمی‌ترین افراد زندگی‌ام نیز پاسخگوی نیازهای عاطفی من نیستند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'ترجیح میدهم بیخیال اکثر فعالیت‌های اجتماعی شوم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'معتقدم که دیگران بهتر از خودم می‌توانند از من مراقبت کنند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا مورد حمله جیب‌برها، دوست‌ها یا جنایتکاران قرار بگیرم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'تقصیر من است که والدینم دوستم ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت توقع دارم که دیگران به حقوق من احترام بگذارند.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'باید از تمام وقت‌هایم، بهترین استفاده را ببرم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'نیازهای من در اولویت است.')
                else:
                    pass
                write_json(javabsoal)
#...........................................................................................
        elif text=='1': #soal5 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==4:
                javabsoal[username].append('1') #panjomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر در برابر دیگران از خودم محافظت نکنم از من سوءاستفاده می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'هیچ فرد خاصی در زندگی‌ام ندارم که بخواهد احساس‌هایش را با من درمیان بگذارد و واقعا نگران حال من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم هیچ‌کس از من خوشش نمی‌آید. خیلی چاق، لاغر، بلند، کوتاه یا زشت هستم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'اگر با مسئولیت جدیدی روبرو شوم به دردسر می‌افتم مگر اینکه کسی من را راهنمایی کند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا دچار بیماری علاج‌ناپذیر شوم، حتی زمانی که پزشکان مشکلی را تشخیص نداده‌اند')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت نگران پذیرش و تایید دیگران هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'چنان مشغول کار هستم که فرصتی برای استراحت و آرامش ندارم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از رفتارهای اعتیادی (مثل سیگار کشیدن، پرخوری) یا مشکلات رفتاری بردارم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal5 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==4:
                javabsoal[username].append('2') #panjomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر در برابر دیگران از خودم محافظت نکنم از من سوءاستفاده می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'هیچ فرد خاصی در زندگی‌ام ندارم که بخواهد احساس‌هایش را با من درمیان بگذارد و واقعا نگران حال من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم هیچ‌کس از من خوشش نمی‌آید. خیلی چاق، لاغر، بلند، کوتاه یا زشت هستم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'اگر با مسئولیت جدیدی روبرو شوم به دردسر می‌افتم مگر اینکه کسی من را راهنمایی کند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا دچار بیماری علاج‌ناپذیر شوم، حتی زمانی که پزشکان مشکلی را تشخیص نداده‌اند')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت نگران پذیرش و تایید دیگران هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'چنان مشغول کار هستم که فرصتی برای استراحت و آرامش ندارم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از رفتارهای اعتیادی (مثل سیگار کشیدن، پرخوری) یا مشکلات رفتاری بردارم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal5 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==4:
                javabsoal[username].append('3') #panjomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر در برابر دیگران از خودم محافظت نکنم از من سوءاستفاده می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'هیچ فرد خاصی در زندگی‌ام ندارم که بخواهد احساس‌هایش را با من درمیان بگذارد و واقعا نگران حال من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم هیچ‌کس از من خوشش نمی‌آید. خیلی چاق، لاغر، بلند، کوتاه یا زشت هستم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'اگر با مسئولیت جدیدی روبرو شوم به دردسر می‌افتم مگر اینکه کسی من را راهنمایی کند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا دچار بیماری علاج‌ناپذیر شوم، حتی زمانی که پزشکان مشکلی را تشخیص نداده‌اند')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت نگران پذیرش و تایید دیگران هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'چنان مشغول کار هستم که فرصتی برای استراحت و آرامش ندارم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از رفتارهای اعتیادی (مثل سیگار کشیدن، پرخوری) یا مشکلات رفتاری بردارم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal5 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==4:
                javabsoal[username].append('4') #panjomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر در برابر دیگران از خودم محافظت نکنم از من سوءاستفاده می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'هیچ فرد خاصی در زندگی‌ام ندارم که بخواهد احساس‌هایش را با من درمیان بگذارد و واقعا نگران حال من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم هیچ‌کس از من خوشش نمی‌آید. خیلی چاق، لاغر، بلند، کوتاه یا زشت هستم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'اگر با مسئولیت جدیدی روبرو شوم به دردسر می‌افتم مگر اینکه کسی من را راهنمایی کند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا دچار بیماری علاج‌ناپذیر شوم، حتی زمانی که پزشکان مشکلی را تشخیص نداده‌اند')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت نگران پذیرش و تایید دیگران هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'چنان مشغول کار هستم که فرصتی برای استراحت و آرامش ندارم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از رفتارهای اعتیادی (مثل سیگار کشیدن، پرخوری) یا مشکلات رفتاری بردارم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal5 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==4:
                javabsoal[username].append('5') #panjomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر در برابر دیگران از خودم محافظت نکنم از من سوءاستفاده می‌کنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'هیچ فرد خاصی در زندگی‌ام ندارم که بخواهد احساس‌هایش را با من درمیان بگذارد و واقعا نگران حال من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم هیچ‌کس از من خوشش نمی‌آید. خیلی چاق، لاغر، بلند، کوتاه یا زشت هستم.')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'اگر با مسئولیت جدیدی روبرو شوم به دردسر می‌افتم مگر اینکه کسی من را راهنمایی کند.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که مبادا دچار بیماری علاج‌ناپذیر شوم، حتی زمانی که پزشکان مشکلی را تشخیص نداده‌اند')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'شخصیت واقعی‌ام را پنهان می‌کنم. شخصیت واقعی‌ام غیرقابل پذیرش است. سعی می‌کنم شخصیت کاذب خودم را به دیگران نشان بدهم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'سخت نگران پذیرش و تایید دیگران هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'چنان مشغول کار هستم که فرصتی برای استراحت و آرامش ندارم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از رفتارهای اعتیادی (مثل سیگار کشیدن، پرخوری) یا مشکلات رفتاری بردارم.')
                else:
                    pass
                write_json(javabsoal)
#......................................................................................................................
        elif text=='1': #soal6 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==5:
                javabsoal[username].append('1') #shishomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'برای پی بردن به صداقت دیگران دست به امتحان انها می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'در زندگی‌ام کسی نیست که مررا دوست بدارد، به من محبت کند و با من صادقانه رفتار کند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم با دیگران تفاوت‌های جدی دارم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم هیچ کاری را درست انجام دهم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'دست به هرکاری می‌زنم و دردسر زیادی تحمل می‌کنم تا از تعارض و ستیزه‌جویی جلوگیری کنم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه تمام فکر و ذهنم سخت به کار مشغول است، از روابط بین فردی غافل شده‌ام.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'انجام کارهای معمولی و کسل‌کننده، عذاب‌آور است. اصلاً آدم این جور کارها نیستم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal6 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==5:
                javabsoal[username].append('2') #shishomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'برای پی بردن به صداقت دیگران دست به امتحان انها می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'در زندگی‌ام کسی نیست که مررا دوست بدارد، به من محبت کند و با من صادقانه رفتار کند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم با دیگران تفاوت‌های جدی دارم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم هیچ کاری را درست انجام دهم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'دست به هرکاری می‌زنم و دردسر زیادی تحمل می‌کنم تا از تعارض و ستیزه‌جویی جلوگیری کنم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه تمام فکر و ذهنم سخت به کار مشغول است، از روابط بین فردی غافل شده‌ام.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'انجام کارهای معمولی و کسل‌کننده، عذاب‌آور است. اصلاً آدم این جور کارها نیستم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal6 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==5:
                javabsoal[username].append('3') #shishomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'برای پی بردن به صداقت دیگران دست به امتحان انها می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'در زندگی‌ام کسی نیست که مررا دوست بدارد، به من محبت کند و با من صادقانه رفتار کند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم با دیگران تفاوت‌های جدی دارم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم هیچ کاری را درست انجام دهم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'دست به هرکاری می‌زنم و دردسر زیادی تحمل می‌کنم تا از تعارض و ستیزه‌جویی جلوگیری کنم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه تمام فکر و ذهنم سخت به کار مشغول است، از روابط بین فردی غافل شده‌ام.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'انجام کارهای معمولی و کسل‌کننده، عذاب‌آور است. اصلاً آدم این جور کارها نیستم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal6 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==5:
                javabsoal[username].append('4') #shishomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'برای پی بردن به صداقت دیگران دست به امتحان انها می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'در زندگی‌ام کسی نیست که مررا دوست بدارد، به من محبت کند و با من صادقانه رفتار کند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم با دیگران تفاوت‌های جدی دارم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم هیچ کاری را درست انجام دهم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'دست به هرکاری می‌زنم و دردسر زیادی تحمل می‌کنم تا از تعارض و ستیزه‌جویی جلوگیری کنم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه تمام فکر و ذهنم سخت به کار مشغول است، از روابط بین فردی غافل شده‌ام.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'انجام کارهای معمولی و کسل‌کننده، عذاب‌آور است. اصلاً آدم این جور کارها نیستم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal6 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==5:
                javabsoal[username].append('5') #shishomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'برای پی بردن به صداقت دیگران دست به امتحان انها می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'در زندگی‌ام کسی نیست که مررا دوست بدارد، به من محبت کند و با من صادقانه رفتار کند.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم با دیگران تفاوت‌های جدی دارم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'نمی‌توانم هیچ کاری را درست انجام دهم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب به سمت افرادی کشیده می‌شوم (والدین، دوستان و نامزد) که دست رد به سینه من می‌زنند یا مدام از من ایراد می‌گیرند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'دست به هرکاری می‌زنم و دردسر زیادی تحمل می‌کنم تا از تعارض و ستیزه‌جویی جلوگیری کنم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه تمام فکر و ذهنم سخت به کار مشغول است، از روابط بین فردی غافل شده‌ام.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'انجام کارهای معمولی و کسل‌کننده، عذاب‌آور است. اصلاً آدم این جور کارها نیستم.')
                else:
                    pass
                write_json(javabsoal)
#.............................................................................................................
        elif text=='1': #soal7 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==6:
                javabsoal[username].append('1') #haftomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر کسی بخواهد به من صدمه بزند، پیش دستی می‌کنم و به او صدمه می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'کسی در زندگی‌ام نیست که واقعا به حرف دل من گوش دهد، مرا درک کند و نیازها و احساس‌های واقعی مرا بشناسد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم به هیچ گروه یا جایی تعلق خاطر ندارم. تنها و بی‌کس هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'آدم بی‌کفایتی هستم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'در روابط اجتماعی اکثراً به نفع دیگران رفتار می‌کنم تا به نفع خودم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه به شدت تحت فشار زمان و استرس هستم. سلامتی من به خطر افتاده است.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'طبق هیجان‌ها و تکانه‌هایم عمل می‌کنم، اگر چه بعدش دچار دردسر می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal7 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==6:
                javabsoal[username].append('2') #haftomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر کسی بخواهد به من صدمه بزند، پیش دستی می‌کنم و به او صدمه می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'کسی در زندگی‌ام نیست که واقعا به حرف دل من گوش دهد، مرا درک کند و نیازها و احساس‌های واقعی مرا بشناسد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم به هیچ گروه یا جایی تعلق خاطر ندارم. تنها و بی‌کس هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'آدم بی‌کفایتی هستم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'در روابط اجتماعی اکثراً به نفع دیگران رفتار می‌کنم تا به نفع خودم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه به شدت تحت فشار زمان و استرس هستم. سلامتی من به خطر افتاده است.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'طبق هیجان‌ها و تکانه‌هایم عمل می‌کنم، اگر چه بعدش دچار دردسر می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal7 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==6:
                javabsoal[username].append('3') #haftomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر کسی بخواهد به من صدمه بزند، پیش دستی می‌کنم و به او صدمه می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'کسی در زندگی‌ام نیست که واقعا به حرف دل من گوش دهد، مرا درک کند و نیازها و احساس‌های واقعی مرا بشناسد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم به هیچ گروه یا جایی تعلق خاطر ندارم. تنها و بی‌کس هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'آدم بی‌کفایتی هستم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'در روابط اجتماعی اکثراً به نفع دیگران رفتار می‌کنم تا به نفع خودم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه به شدت تحت فشار زمان و استرس هستم. سلامتی من به خطر افتاده است.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'طبق هیجان‌ها و تکانه‌هایم عمل می‌کنم، اگر چه بعدش دچار دردسر می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal7 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==6:
                javabsoal[username].append('4') #haftomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر کسی بخواهد به من صدمه بزند، پیش دستی می‌کنم و به او صدمه می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'کسی در زندگی‌ام نیست که واقعا به حرف دل من گوش دهد، مرا درک کند و نیازها و احساس‌های واقعی مرا بشناسد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم به هیچ گروه یا جایی تعلق خاطر ندارم. تنها و بی‌کس هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'آدم بی‌کفایتی هستم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'در روابط اجتماعی اکثراً به نفع دیگران رفتار می‌کنم تا به نفع خودم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه به شدت تحت فشار زمان و استرس هستم. سلامتی من به خطر افتاده است.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'طبق هیجان‌ها و تکانه‌هایم عمل می‌کنم، اگر چه بعدش دچار دردسر می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal7 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==6:
                javabsoal[username].append('5') #haftomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'اگر کسی بخواهد به من صدمه بزند، پیش دستی می‌کنم و به او صدمه می‌زنم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'کسی در زندگی‌ام نیست که واقعا به حرف دل من گوش دهد، مرا درک کند و نیازها و احساس‌های واقعی مرا بشناسد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم به هیچ گروه یا جایی تعلق خاطر ندارم. تنها و بی‌کس هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'آدم بی‌کفایتی هستم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'اگر به تنهایی سوار هواپیما، قطار یا هر وسیله نقلیه عمومی شوم، خیلی دچار اضطراب می‌شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'اغلب خودم را به باد انتقاد می‌گیرم و شخصیت خودم را خورد می‌کنم. خصوصا در حضور کسانی این کار را می‌کنم که مرا دوست دارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'در روابط اجتماعی اکثراً به نفع دیگران رفتار می‌کنم تا به نفع خودم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'به دلیل اینکه به شدت تحت فشار زمان و استرس هستم. سلامتی من به خطر افتاده است.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'طبق هیجان‌ها و تکانه‌هایم عمل می‌کنم، اگر چه بعدش دچار دردسر می‌شوم.')
                else:
                    pass
                write_json(javabsoal)
#..................................................................................................
        elif text=='1': #soal8 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==7:
                javabsoal[username].append('1') #hashtomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'می‌ترسم که به دیگران اجازه بدهم تا با من صمیمی شوند چون دیر یا زود به من اسیب می‌زنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'خیلی برای من دشوار است که به دیگران اجازه دهم از من حمایت و مرا راهنمایی کنند، حتی اگر این خواست درونی من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم که همیشه در حاشیه جمع یا گروه هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'عقل درست و حسابی ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'خیلی نسبت به احساس‌های جسمی‌ام آگاهی دارم و نگرانم که مبادا این احساس‌ها دلیل بیماری باشند.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'خیلی دل رحم هستم به نحوی که معمولاً کار و زحمت مراقبت از نزدیکانم روی دوش من است.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' اگر اشتباه کنم، لایق ترین بدترین انتقادها هستم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal8 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==7:
                javabsoal[username].append('2') #hashtomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'می‌ترسم که به دیگران اجازه بدهم تا با من صمیمی شوند چون دیر یا زود به من اسیب می‌زنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'خیلی برای من دشوار است که به دیگران اجازه دهم از من حمایت و مرا راهنمایی کنند، حتی اگر این خواست درونی من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم که همیشه در حاشیه جمع یا گروه هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'عقل درست و حسابی ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'خیلی نسبت به احساس‌های جسمی‌ام آگاهی دارم و نگرانم که مبادا این احساس‌ها دلیل بیماری باشند.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'خیلی دل رحم هستم به نحوی که معمولاً کار و زحمت مراقبت از نزدیکانم روی دوش من است.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' اگر اشتباه کنم، لایق ترین بدترین انتقادها هستم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal8 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==7:
                javabsoal[username].append('3') #hashtomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'می‌ترسم که به دیگران اجازه بدهم تا با من صمیمی شوند چون دیر یا زود به من اسیب می‌زنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'خیلی برای من دشوار است که به دیگران اجازه دهم از من حمایت و مرا راهنمایی کنند، حتی اگر این خواست درونی من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم که همیشه در حاشیه جمع یا گروه هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'عقل درست و حسابی ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'خیلی نسبت به احساس‌های جسمی‌ام آگاهی دارم و نگرانم که مبادا این احساس‌ها دلیل بیماری باشند.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'خیلی دل رحم هستم به نحوی که معمولاً کار و زحمت مراقبت از نزدیکانم روی دوش من است.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' اگر اشتباه کنم، لایق ترین بدترین انتقادها هستم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal8 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==7:
                javabsoal[username].append('4') #hashtomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'می‌ترسم که به دیگران اجازه بدهم تا با من صمیمی شوند چون دیر یا زود به من اسیب می‌زنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'خیلی برای من دشوار است که به دیگران اجازه دهم از من حمایت و مرا راهنمایی کنند، حتی اگر این خواست درونی من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم که همیشه در حاشیه جمع یا گروه هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'عقل درست و حسابی ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'خیلی نسبت به احساس‌های جسمی‌ام آگاهی دارم و نگرانم که مبادا این احساس‌ها دلیل بیماری باشند.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'خیلی دل رحم هستم به نحوی که معمولاً کار و زحمت مراقبت از نزدیکانم روی دوش من است.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' اگر اشتباه کنم، لایق ترین بدترین انتقادها هستم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal8 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==7:
                javabsoal[username].append('5') #hashtomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'می‌ترسم که به دیگران اجازه بدهم تا با من صمیمی شوند چون دیر یا زود به من اسیب می‌زنند.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'خیلی برای من دشوار است که به دیگران اجازه دهم از من حمایت و مرا راهنمایی کنند، حتی اگر این خواست درونی من باشد.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم که همیشه در حاشیه جمع یا گروه هستم')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'عقل درست و حسابی ندارم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'خیلی نسبت به احساس‌های جسمی‌ام آگاهی دارم و نگرانم که مبادا این احساس‌ها دلیل بیماری باشند.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'ویژگی‌های مثبت من در نظرم هیچ ارزشی ندارند.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'خیلی دل رحم هستم به نحوی که معمولاً کار و زحمت مراقبت از نزدیکانم روی دوش من است.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' اگر اشتباه کنم، لایق ترین بدترین انتقادها هستم.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم.')
                else:
                    pass
                write_json(javabsoal)
#.............................................................................................................
        elif text=='1': #soal9 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==8:
                javabsoal[username].append('1') #nohomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'وقتی به کارهای دیگران در قبال خودم فکر می‌کنم، عصبانی می‌شوم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' سخت به دیگران اجازه می‌دهم که دوستم داشته باشند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'خانواده من با دیگر خانواده‌ها خیلی فرق دارد')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'به قضاوت‌های خودم نمی‌توانم اعتماد کنم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که در جمع و حضور دیگران، کنترلم را از دست بدهم یا دیوانه شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'هرگاه خواسته‌های خودم را در اولویت قرار دهم، سخت دچار احساس گناه می‌شوم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' سخت رقابت‌گرا و اهل چشم و هم‌چشمی هستم. ')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'اصرار دارم که دیگران مطابق میل من رفتار کنند.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal9 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==8:
                javabsoal[username].append('2') #nohomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'وقتی به کارهای دیگران در قبال خودم فکر می‌کنم، عصبانی می‌شوم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' سخت به دیگران اجازه می‌دهم که دوستم داشته باشند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'خانواده من با دیگر خانواده‌ها خیلی فرق دارد')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'به قضاوت‌های خودم نمی‌توانم اعتماد کنم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که در جمع و حضور دیگران، کنترلم را از دست بدهم یا دیوانه شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'هرگاه خواسته‌های خودم را در اولویت قرار دهم، سخت دچار احساس گناه می‌شوم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' سخت رقابت‌گرا و اهل چشم و هم‌چشمی هستم. ')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'اصرار دارم که دیگران مطابق میل من رفتار کنند.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal9 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==8:
                javabsoal[username].append('3') #nohomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'وقتی به کارهای دیگران در قبال خودم فکر می‌کنم، عصبانی می‌شوم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' سخت به دیگران اجازه می‌دهم که دوستم داشته باشند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'خانواده من با دیگر خانواده‌ها خیلی فرق دارد')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'به قضاوت‌های خودم نمی‌توانم اعتماد کنم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که در جمع و حضور دیگران، کنترلم را از دست بدهم یا دیوانه شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'هرگاه خواسته‌های خودم را در اولویت قرار دهم، سخت دچار احساس گناه می‌شوم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' سخت رقابت‌گرا و اهل چشم و هم‌چشمی هستم. ')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'اصرار دارم که دیگران مطابق میل من رفتار کنند.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal9 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==8:
                javabsoal[username].append('4') #nohomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'وقتی به کارهای دیگران در قبال خودم فکر می‌کنم، عصبانی می‌شوم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' سخت به دیگران اجازه می‌دهم که دوستم داشته باشند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'خانواده من با دیگر خانواده‌ها خیلی فرق دارد')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'به قضاوت‌های خودم نمی‌توانم اعتماد کنم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که در جمع و حضور دیگران، کنترلم را از دست بدهم یا دیوانه شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'هرگاه خواسته‌های خودم را در اولویت قرار دهم، سخت دچار احساس گناه می‌شوم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' سخت رقابت‌گرا و اهل چشم و هم‌چشمی هستم. ')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'اصرار دارم که دیگران مطابق میل من رفتار کنند.')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal9 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==8:
                javabsoal[username].append('5') #nohomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'وقتی به کارهای دیگران در قبال خودم فکر می‌کنم، عصبانی می‌شوم.')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,' سخت به دیگران اجازه می‌دهم که دوستم داشته باشند')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'خانواده من با دیگر خانواده‌ها خیلی فرق دارد')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'به قضاوت‌های خودم نمی‌توانم اعتماد کنم.')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'نگرانم که در جمع و حضور دیگران، کنترلم را از دست بدهم یا دیوانه شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,'احساس شرمساری زیادی را تجربه می‌کنم.')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'هرگاه خواسته‌های خودم را در اولویت قرار دهم، سخت دچار احساس گناه می‌شوم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,' سخت رقابت‌گرا و اهل چشم و هم‌چشمی هستم. ')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'اصرار دارم که دیگران مطابق میل من رفتار کنند.')
                else:
                    pass
                write_json(javabsoal)
#.............................................................................................................
        elif text=='1': #soal10 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==9:
                javabsoal[username].append('1') #dahomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'افرادی که به انها اعتماد داشتم با من بدرفتاری (کلامی، جسمی و جنسی) کرده‌اند')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'بیشتر اوقات تنها بوده‌ام.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم از تمام جمع‌ها، کنار گذاشته شده‌ام')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'مسئولیت‌های زندگی روزمره برای من سخت و طاقت‌فرساست')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'سخت نگرانم که مبادا تمام سرمایه مالی‌ام را از دست بدهم یا ورشکست شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,' یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'آدم خوبی هستم چون بیشتر از آنچه به فکر رفاه حال خودم باشم به فکر حل مشکلات بقیه هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'ثروت و منزلت اجتماعی برای من بی‌نهایت مهم هستند.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم')
                else:
                    pass
                write_json(javabsoal)
        elif text=='2': #soal10 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==9:
                javabsoal[username].append('2') #dahomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'افرادی که به انها اعتماد داشتم با من بدرفتاری (کلامی، جسمی و جنسی) کرده‌اند')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'بیشتر اوقات تنها بوده‌ام.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم از تمام جمع‌ها، کنار گذاشته شده‌ام')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'مسئولیت‌های زندگی روزمره برای من سخت و طاقت‌فرساست')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'سخت نگرانم که مبادا تمام سرمایه مالی‌ام را از دست بدهم یا ورشکست شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,' یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'آدم خوبی هستم چون بیشتر از آنچه به فکر رفاه حال خودم باشم به فکر حل مشکلات بقیه هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'ثروت و منزلت اجتماعی برای من بی‌نهایت مهم هستند.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم')
                else:
                    pass
                write_json(javabsoal)
        elif text=='3': #soal10 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==9:
                javabsoal[username].append('3') #dahomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'افرادی که به انها اعتماد داشتم با من بدرفتاری (کلامی، جسمی و جنسی) کرده‌اند')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'بیشتر اوقات تنها بوده‌ام.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم از تمام جمع‌ها، کنار گذاشته شده‌ام')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'مسئولیت‌های زندگی روزمره برای من سخت و طاقت‌فرساست')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'سخت نگرانم که مبادا تمام سرمایه مالی‌ام را از دست بدهم یا ورشکست شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,' یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'آدم خوبی هستم چون بیشتر از آنچه به فکر رفاه حال خودم باشم به فکر حل مشکلات بقیه هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'ثروت و منزلت اجتماعی برای من بی‌نهایت مهم هستند.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم')
                else:
                    pass
                write_json(javabsoal)
        elif text=='4': #soal10 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==9:
                javabsoal[username].append('4') #dahomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'افرادی که به انها اعتماد داشتم با من بدرفتاری (کلامی، جسمی و جنسی) کرده‌اند')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'بیشتر اوقات تنها بوده‌ام.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم از تمام جمع‌ها، کنار گذاشته شده‌ام')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'مسئولیت‌های زندگی روزمره برای من سخت و طاقت‌فرساست')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'سخت نگرانم که مبادا تمام سرمایه مالی‌ام را از دست بدهم یا ورشکست شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,' یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'آدم خوبی هستم چون بیشتر از آنچه به فکر رفاه حال خودم باشم به فکر حل مشکلات بقیه هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'ثروت و منزلت اجتماعی برای من بی‌نهایت مهم هستند.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم')
                else:
                    pass
                write_json(javabsoal)
        elif text=='5': #soal10 tarhvare
            javabsoal= read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==9:
                javabsoal[username].append('5') #dahomin ozv list username
                if javabsoal[username][0]=='1':
                    sendMessage(chat_id,'یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود.')
                elif javabsoal[username][0]=='2':
                    sendMessage(chat_id,'افرادی که به انها اعتماد داشتم با من بدرفتاری (کلامی، جسمی و جنسی) کرده‌اند')
                elif javabsoal[username][0]=='3':
                    sendMessage(chat_id,'بیشتر اوقات تنها بوده‌ام.')
                elif javabsoal[username][0]=='4':
                    sendMessage(chat_id,'احساس می‌کنم از تمام جمع‌ها، کنار گذاشته شده‌ام')
                elif javabsoal[username][0]=='5':
                    sendMessage(chat_id,'مسئولیت‌های زندگی روزمره برای من سخت و طاقت‌فرساست')
                elif javabsoal[username][0]=='6':
                    sendMessage(chat_id,'سخت نگرانم که مبادا تمام سرمایه مالی‌ام را از دست بدهم یا ورشکست شوم.')
                elif javabsoal[username][0]=='7':
                    sendMessage(chat_id,' یکی از ترس‌های اصلی من این است که عیب‌هایم برملا شود')
                elif javabsoal[username][0]=='8':
                    sendMessage(chat_id,'آدم خوبی هستم چون بیشتر از آنچه به فکر رفاه حال خودم باشم به فکر حل مشکلات بقیه هستم.')
                elif javabsoal[username][0]=='9':  
                    sendMessage(chat_id,'ثروت و منزلت اجتماعی برای من بی‌نهایت مهم هستند.')
                elif javabsoal[username][0]=='10':
                    sendMessage(chat_id,'خیلی سخت است که دست از خوشی و رضایت آنی بردارم به این امید که در آینده به اهداف و دستاوردهای بزرگی برسم')
                else:
                    pass
                write_json(javabsoal)
#.............................................................................................................
        elif text=='1': 
            javabsoal= read_json()
            nemodar =read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==10:
                javabsoal[username].append('1') #yazdahomin ozv list username
                write_json(javabsoal)
                listemtiaz =[]
                for i in range(1,12):
                    emtiaz = int(javabsoal[username][i])
                    listemtiaz.append(emtiaz)
                jamemtiaz=sum(listemtiaz)
                nemodar[username]={}
                nemodar[username]['tale1']=[]
                nemodar[username]['tale2']=[]
                nemodar[username]['tale3']=[]
                nemodar[username]['tale4']=[]
                nemodar[username]['tale5']=[]
                nemodar[username]['tale6']=[]
                nemodar[username]['tale7']=[]
                nemodar[username]['tale8']=[]
                nemodar[username]['tale9']=[]
                nemodar[username]['tale10']=[]
                if 9<jamemtiaz<20:
                    sendMessage(chat_id,'خیلی پایین، احتمالا این تله زندگی در ذهن شما شکل نگرفته .')
                elif 19<jamemtiaz<30:
                    sendMessage(chat_id,'نسبتا پایین، این تله زندگی ممکن است گاهی اوقات یقه شما را بگیرد')
                elif 29<jamemtiaz<40:
                    sendMessage(chat_id,'متوسط، این تله زندگی باعث مشکلاتی برای شما شده است')
                elif 39<jamemtiaz<50:
                    sendMessage(chat_id,'بالا، بدون شک یکی از تله‌های زندگی شماست')
                else:
                    sendMessage(chat_id,'شدید، این تله زندگی دقیقا یکی از تله‌های اصلی شماست')
                if jamemtiaz>19:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی رهاشدگی,\n۱. رهاشدگی دوران کودکی‌تان را درک کنید.,\n۲. احساس‌های مربوط به رهاشدگی را بازنگری کنید و حساسیت‌های خود را به از دست ‌دادن افراد نزدیک، ترس از تنهایی و نیاز به آویزان شدن و وابستگی بیمارگونه بشناسید.,\n۳. روابط گذشته را بررسی کنید تا الگوهای منجر به عود و بازگشت تله زندگی را بشناسید و فهرستی از خطاهای فکری و رفتاری ناشی از رهاشدگی تهیه کنید.,\n۴. از رابطه با افراد بی‌ثبات، بی‌تعهد و تنوع‌طلب اجتناب کنید، ولو اینکه این افراد برای شما جذابیت و کشش زیادی داشته باشند.,\n۵. وقتی که نامزدی پیدا می‌کنید که متعهد و باثبات است به او اعتماد کنید. باور کنید که او برای همیشه در کنار شما می‌ماند و شما را ترک نمی‌کند.,\n۶. حسادت نکنید، به همسرتان آویزان نشوید و به جدایی‌های معمول زندگی، واکنش افراطی نشان ندهید. ')
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی بی‌اعتمادی و بدرفتاری,\n۱. در صورت امکان از درمانگری صاحبْ‌صلاحیت برای تغییر این تله زندگی کمک بگیرید. مخصوصا اگد سابقه‌ای از بدرفتاری جنسی یا جسمی داشته‌اید.,\n۲. دوستی قابل اعتماد پیدا کنید. تمرین‌های مربوط به تصویرسازی ذهنی را انجام دهید. سعی کنید خاطرات به بدرفتاری را به‌یاد بیاورید و حوادث را با جزئیات کامل بازگو کنید.,\n۳. در حین تصویرسازی ذهنی، خشم خود را بر سر فردی که از شما سوءاستفاده کرده‌ است، خالی کنید. با این کار در تصویر ذهنی بر احساس عجز و بیچارگی خود، غلبه کنید.,\n۴. خودتان را مقصر نپندارید. شما مستحق بدرفتاری و سوءاستفاده شدن نیستید. از فرد بدرفتار، عذرخواهی نکنید.,\n۵. در عین حال که به تغییر این تله زندگی می‌پردازید، به‌تدریج رابطه خو با افراد سوءاستفاده‌گر قطع، کنید.,\n۶. در صورت امکان برای فردی که از شما سوءاستفاده کرده است، پیامدها و اثرات رفتارش بر زندگی فعلی‌تان را بازگو کنید یا برای او در این زمینه، نامه بنویسید.,\n۷. بدرفتاری‌های موجود در رابطه‌های فعلی‌تان را تحمل نکنید.,\n۸. سعی کنید با فردی قابل اعتماد وارد رابطه‌ای صمیمی شوید. به کسی اعتماد کنید که از اعتماد شما سوءاستفاده نمی‌کند,\n۹. سعی کنید با افرادی رابطه برقرار کنید که قصد آسیب زدن به شما را ندارند و به حقوق شما احترام می‌گذارند.,\n۱۰. با نزدیکان خود بدرفتاری نکنید.')
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                        sendMessage(chat_id,' تغییر تله زندگی محرومیت هیجانی,\n۱.محرومیت کودکی‌تان را درک کنید. کودک درون و آسیب‌دیده درون را حس کنید.,\n۲. احساس‌های محرومیت در روابط فعلی‌تان را به دقت زیر نظر بگیرید. نیاز به محبت، همدلی و راهنمایی را به‌خوبی لمس کنید.,\n۳. روابط گذشته خود را به منظور روشن‌سازی الگوی حاکم بر روابط بررسی کنید. موانعی را که باعث عدم تغییر شما می‌شوند، فهرست کنید.,\n.  از رابطه با افراد سرد و بی مهری که شما را به شدت مجذوب خودشان می کنند، دوری کنید.۴,\n. وقتی که فرد مورد علاقه شما از لحاظ هیجانی آدم سالمی است از این فرصت استفاده کنید تا روابط خود را بهبود ببخشید. نیازهای خودتان را بازگو کنید. به طرف مقابل، آسیب پذیری های خود را بگویید,\n۶. از مقصر دانستن نامزدتان و پرتوقعی خود، دست بردارید.') #rahkarha
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی طرد اجتماعی ,\n۱.ریشه‌های تحولی تله زندگی طرد اجتماعی را را در دوران کودکی‌تان درک کنید. احساس حقارت و انزوای کودک درونتان را درک کنید.,\n۲.موقعیت‌هایی را بنویسید که در زندگی روزمره خود دچار احساس آشفتگی و اضطراب می‌شوید.,\n۳. موقعیت‌هایی را بنویسید که از آنها اجتناب می‌کنید.,\n۴. چنانچه در موقعیت‌هایی دچار احساس تنهایی و تفاوت می‌شوید یا جبران افراطی یا حمله متقابل، سعی در پنهان‌سازی این احساس‌ها دارید، سعی کنید این موقعیت ها را بنویسید.,\n۵. مراحل اول تا چهارم را بنویسید سپس ویژگی‌هایی را بنویسید که باعث می‌شوند از دیگران منزوی شوید، احساس حقارت کنید یا آسیب‌پذیری جلوه کنید.,\n۶. اگر واقعا مشکلات و کمبودهایی دارید که واقعی هستند، پس راهکارهایی را برای غلبه بر این مشکلات و کمبودها یا کاهش اثرات آنها پیدا کنید، به تدریج بر این مشکلات غلبه کنید.,\n۷. در اهمیت عیب‌ها و نقص‌هایی که نتوانسته‌اید تغییر بدهید تجدید نظر کنید. منظور این است که دیدگاه خودتان را درباره عیب‌ها و نقص‌های تغییر ناپذیر، عوض کنید.,\n۸. برای هرکدام از عیب‌ها و نقص‌های خود، کارت آموزشی تهیه کنید.,\n۹. از موقعیت‌های کاری و اجتماعی که اجتناب می‌کنید، سلسله‌مراتبی تهیه کنید. سعی کنید به تدریج به این موقعیت‌ها وارد شوید.,\n۱۰. وقتی در جمع به‌سر می‌برید سعی کنید آغازگر مکالمه با دیگران باشید,\n۱۱. سعی‌کنید در گروه‌ها شخصیت اصلی خودتان را بروز دهید و نقش بازی نکنید.,\n۱۲. دست از تلاش برای جبران افراطی حوزه.های نادلپذیر، ناخوشایند و نامحبوب بردارید.')
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی وابستگی,\n۱.ریشه‌های تحولی وابستگی در دوران کودکی‌تان را درک کنید. بی کفایتی و وابستگی کودک درون را تجربه کنید.,\n۲. موقعیت‌ها، وظایف، مسئولیت‌ها و تصمیم‌هایی را بنویسید که در زندگی روزمره برای شما چالش‌آفرین هستند و برای انجام این وظایف، ورود به موقعیت‌ها و پذیرش مسئولیت‌ها و اتخاذ تصمیم‌ها به کمک یا نظر دیگران، وابسته هستند.,\n۳. چالش‌ها تغییرات یا دل‌نگرانی‌هایی را بنویسید که دلیل ترس از آن‌ها اجتناب می‌کنید.,\n۴. به گونه‌ای نظام‌مند، خودتان را مجبور کنید که وظایف روزمره را بدون کمک دیگران انجام بدهید و تصمیم‌ها را بدون کمک‌طلبی اتخاذ کنید. چالش‌هایی را که از آنها اجتناب می‌کنید، برعهده بگیرید. در ابتدا از وظایف و تکالیف آسان و راحت شروع کنید.,\n۵. زمانی‌که در انجام و برعهده گرفتن مسئولیت‌ها موفق شدید به خودتان امتیاز بدهید. پاداش دهی به خود را دست کم نگیرید. اگر در انجام مسئولیت‌ها شکست خوردید، کارها را رها نکنید و مایوس نشوید. دست از طلب برندارید تا به هدف خود برسید.,\n۶. روابط گذشته خود را بررسی کنید و الگوهای وابستگی تکراری را مشخص سازید. علائم گرفتار شدن در تله زندگی را بنویسید تا به دام آنها نیفتید.,\n۷. از ارتباط با نامزد قوی، مستقل و سخت حمایتگر، خودداری کنید، ولو اینکه این فرد در شما کشش و جذابیت زیادی ایجاد کند.,\n۸. اگر نامزد شما بر اساس مساوات و احترام متقابل با شما رفتار می‌کند و به شما فرصت مسئولیت‌پذیری و نظردهی می‌دهد این فرصت ها را از دست ندهید.,\n۹. اگر همسر یا رئیس و کارمند تان به شما کمک کمک لازم را نمی‌کنند زبان به شکایت باز نکنید. اصرار نورزید که از جانب این افراد راهنمایی بگیرید یا توقع نداشته باشید خیال شما را جمع کنند.,\n۱۰. در حوزه شغلی به تدریج چالش‌ها یا مسئولیت‌های جدیدی بپذیرید، و به تدریج آنها را انجام دهید.,\n۱۱. اگر شما در زمره افراد مستقل‌نما هستید، از نیازتان برای کمک‌خواهی آگاه باشید. از دیگران کمک بگیرید. مسئولیت‌های فراتر از توان را نپذیرید. از اضطراب خود به عنوان علامت استفاده کنید تا بدانید که چقدر باید مسئولیت برعهده بگیرید')
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی آسیب پذیری,\n۱.ریشه‌های تحولی زندگیتان را درک کنید.,\n۲. فهرستی از ترس‌های خود تهیه کنید.,\n۳. موقعیت‌های استرس‌برانگیز را طبق سلسله مراتب، نظم بدهید.,\n۴. افراد صمیمی زندگی‌تان (مثل همسر، فرزند و اعضای خانواده) را ملاقات کنید و از آنها بخواهید که برای برخورد جدی و اساسی با ترس‌هایتان به شما کمک کنند.,\n۵. احتمال وقوع حوادث ترس‌برانگیز را بررسی کنید.,\n۶. برای هر کدام از ترس‌های خود، کارت آموزشی تهیه کنید.,\n۷. با کودک درون حرف بزنید. برای کودک درون، والدی توانمند و شجاع باشید.,\n۸. تمرین‌های آرامش را انجام دهید.,\n۹. با استفاده از تکنیک تصویرسازی ذهنی برعلیه ترس‌ها، موضع بگیرید.,\n۱۰. در زندگی واقعی بر ترس‌هایتان غلبه کنید,\n۱۱. برای هر کدام از این مراحل که با موفقیت پشت سر گذاشتید، به خودتان پاداش بدهید.')
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی نقص/ شرم,\n۱.احساس‌های بی‌ارزشی و شرمساری دوران کودکی را درک کنید. کودک آسیب دیده درون را حس کنید.,\n۲. فهرستی از شیوه‌های مقابله خود (تسلیم فرار و حمله) برای کنار آمدن با تله زندگی را بنویسید.,\n۳. تلاش کنید دست از رفتارهای مقابله‌ای فرار یا حمله بردارید,\n۴. احساس‌های شرم و بی‌ارزشی را زیر نظر بگیرید.,\n۵. معیارهایتان را برای انتخاب نامزد جذاب و نامزد غیرجذاب را بنویسید.,\n۶. نقاط ضعف و نقاط قوت خود را در دوران کودکی و دوران فعلی بنویسید.,\n۷. نقاط ضعف فعلی خود را به طور جدی ارزیابی کنید.,\n۸. برای تغییر نقاط ضعف تغییرپذیر، برنامه ریزی کنید.,\n۹. نامه‌ای به والد (یا والدین) سرزنشگرتان بنویسید.,\n۱۰. کارت آموزشی تهیه کنید.,\n۱۱. تلاش کنید در روابط صمیمی خود صادق‌تر باشید.,\n۱۲. عشق و محبت افراد نزدیک خود را بپذیرید.,\n۱۳. اجازه ندهید دیگران به رفتارهای توهین‌آمیز و نامحترمانه‌شان با شما ادامه دهند.,\n۱۴. اگر در روابط خود به طرف مقابل ایراد می‌گیرید و سرزنش می‌کنید، دست از این کار بردارید')
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی اطاعت,\n۱.ریشه‌های تحولی تله زندگی اطاعت را در دوران کودکی‌تان بشناسید و درک کنید کودک درون مطیع و فرمان بردار خود را بشناسید.,\n۲. موقعیت‌هایی را بشناسید که در محل کار یا در خانه تحت سلطه دیگران قرار می گیرید یا موقعیت‌هایی را بشناسید که نیازهای‌تان را فدای دیگران می‌کنید.,\n۳. در بسیاری از جنبه های زندگی برای خودتان علایق و ایده‌هایی دست و پا کنید (مثل سینما، غذا، تفریح، اوقات فراغت و استفاده از زمان و...) به تدریج با این کار خودتان و نیازهای‌تان را بشناسید.,\n۴. ببینید که چقدر به دیگران کمک می‌کنید و در مقابل، دیگران چقدر به شما کمک می‌کنند. چقدر برای دیگران وقت می‌گذارید و در برابر آنها چقدر برای شما وقت می‌گذارند.,\n۵. رفتا‌رهای منفعلانه_پرخاشگرانه را کنار بگذارید. خودتان را مجبور به رفتارهای جسارتمندانه کنید تا حق‌تان پایمال نشود. ابتدا خواسته‌های کوچک خود را برای دیگران مطرح کنید.,\n۶. از دیگران بخواهید که از شما حمایت و مراقبت کنند. از آنها کمک بگیرید و مشکلات خودتان را با آنها در میان بگذارید. سعی کنید ترازوی دادوستد شما در روابط بین‌فردی تا اندازه‌ای متعادل باشد.,\n۷. با افراد خودخواه و خودمحور که به نیازهای شما پشیزی ارزش قائل نمی‌شوند، قطع رابطه کنید. وقتی احساس کردید در روابط یک‌طرفه و ناسالم گرفتار شده‌اید، رابطه را تغییر بدهید یا از خیر رابطه بگذرید.,\n۸. تمرین کنید به جای موافقت با دیگران، با آنها جسارتمندانه برخورد کنید. به محض این که عصبانی شدید با شیوه ای مناسب خشم خودتان را ابراز کنید. اگر کسی موجب ناراحتی و آزردگی خاطر شما شد، یاد بگیرید که آرامش خودتان را حفظ کنید و سپس دلخوری‌تان را به او بگویید.,\n۹. برای گرایش خودتان به جلب رضایت دیگران، دلیل تراشی نکنید. مدام به خودتان نگویید بلاهایی که از این راه بر سر شما می‌آیند اهمیتی ندارند.,\n۱۰. به بررسی روابط گذشته خود بپردازید. دوستان یا افراد کنترلگر نیازمند را مشخص کنید. در روابط بعدی خود مواظب باشید با چنین افرادی رابطه برقرار نکنید. فهرستی از ویژگی های افراد خودخواه، مغرور، بی‌مسئولیت یا وابسته تهیه کنید که در شما اشتیاق زیادی برای برقراری رابطه ایجاد می‌کنند.,\n۱۱. به رابطه‌ای ارزش قائل شوید که طرف مقابل، نیازهای اصلی شما را ارضا می‌کند، از شما نظر می‌خواهد و به شما مجال می‌دهد که توانایی‌های خودتان را بشناسید.,\n۱۲. در محل‌کار، قاطع‌تر باشید. به کارهای خودتان ارزش قائل شوید. اگر فکر می‌کنید که درخواست پیشرفت و ارتقای شغلی حق شماست، از تقاضای درخواست به سادگی نگذرید. مسئولیت های افراطی را به دیگران واگذار کنید.,\n۱۳. (درباره افراد سرکش و نافرمان صادق است) سعی نکنید در برابر درخواست‌های دیگران به لاک دفاعی بروید. تلاش کنید درخواست های دیگران را درک کنید. خواسته های خودتان را بشناسید. برخی اوقات شما از سر لجبازی با خواسته افراد مافوق خود مخالفت می‌کنید. دست از لجبازی بردارید تا مشکل شما حل شود.,\n۱۴. نتیجه‌گیری‌های خودتان را از این مراحل روی کارت آموزشی بنویسید و آن را همراه خودتان داشته باشید')
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی معیارهای سخت‌گیرانه,\n۱.حوزه‌هایی از زندگی‌تان را مشخص کنید که زیر سیطره معیارهای سختگیرانه یا نامتعادل قرار گرفته‌اند.,\n۲. مزایای تلاش برای رسیدن به این معیارهای سخت‌گیرانه را بنویسید.,\n۳. معایب تلاش برای رسیدن به معیارهای سختگیرانه را بنویسید.,\n۴. تلاش کنید که به تصور خود پروبال بدهید و زندگی رها از این معیارها را تجسم کنید.,\n۵. ریشه های تحولی و دلایل شکل‌گیری تله زندگی‌تان را درک کنید.,\n۶. تصور کنید که اگر توقعات خود را کم کنید چه اتفاقی می‌افتد.,\n۷. میزان زمانی را که صرف حفظ این معیارها می کنید، مشخص سازید.,\n۸. با نظرخواهی از افراد معقول دیدی دقیق‌تر و منطقی‌تر نسبت به این معیارها پیدا کنید.,\n۹. با برنامه‌ریزی تدریجی یا تغییر رفتار، در راستای ارضا نیازهای اصلی‌تر گام بردارید.')
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                        sendMessage(chat_id,'غلبه بر مشکلات تله زندگی استحقاق,\n۱.فهرستی از مزایا و معایب نپذیرفتن محدودیت ها تهیه کنید. این کارها برای انگیزه‌مندسازی شما ضروری است.,\n۲. بهانه تراشی‌های خود را برای نپذیرفتن محدودیت ها کنار بگذارید.,\n۳. دقت کنید که چگونه نپذیرفتن محدودیت‌ها در زندگی روزمره برای شما مشکل درست می‌کند. فهرستی از این مشکلات تهیه کنید.,\n۴. برای این که یادتان باشد که با بی‌انضباطی و استحقاق خود در موقعیت‌ها بجنگید، کارت آموزشی درست کنید.,\n۵. همچنان که به دنبال تغییر هستید از دیگران درباره میزان تغییر خود، نظرخواهی کنید.,\n۶. تلاش کنید با اطرافیان خود، همدلی کنید.,\n۷. اگر تله زندگی شما از نوع حمله برعلیه سایر تله‌هاست سعی کنید طرح های زیربنایی را درک کنید و از تکنیک‌های مربوط به هر کدام از آنها استفاده نمایید.,\n۸. اگر در انضباط شخصی مشکل دارید، کارهای خود را بر اساس میزان ناکام سازی و بیزارسازی، درجه‌بندی کنید. کارهای خود را سلسله‌مراتبی در نظر بگیرید و برای انجام آنها اقدام کنید.,\n۹. اگر در کنترل هیجان‌های خود مشکل دارید از تکنیک "محروم‌سازی" استفاده کنید.,\n۱۰. اگر گرفتار استحقاق از نوع وابستگی شده‌اید، کارهایتان را براساس میزان سختی درجه‌بندی کنید. آنگاه به تدریج کارها را از آسان به سخت و بدون کمک دیگران انجام دهید. از کارهای آسان‌تر شروع کنید تا به خودتان ثابت کنید که آدم با کفایتی هستید.')
                    else:
                        pass
                    
                    sendMessage(chat_id,'آیا تمایل دارید نمودار غلبه بر تله زتدگی خود را ببینید؟\n در صورت تمایل، عبارت "نمودار" را ارسال کنید')
                    sendMessage(chat_id,'در صورت تمایل برای دریافت مشاوره تخصصی می‌توانید با شماره زیر تماس بگیرید:\n09123671593')
                else:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                    else:
                        pass
                    sendMessage(chat_id,'تبریک میگم، با توجه به پاسخ ارسال شده شما در دام این تله گرفتار نشدید')
                write_json(nemodar)
        elif text=='2': 
            javabsoal= read_json()
            nemodar =read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==10:
                javabsoal[username].append('2') #yazdahomin ozv list username
                write_json(javabsoal)
                listemtiaz =[]
                for i in range(1,12):
                    emtiaz = int(javabsoal[username][i])
                    listemtiaz.append(emtiaz)
                jamemtiaz=sum(listemtiaz)
                for key in nemodar.keys():
                    if username not in key:
                        nemodar[username]={}
                    else:
                        pass
                for key in nemodar[username].keys():
                    if 'tale1' not in key:
                        nemodar[username]['tale1']=[]
                    if 'tale2' not in key:
                        nemodar[username]['tale2']=[]
                    if 'tale3' not in key:
                        nemodar[username]['tale3']=[]
                    if 'tale4' not in key:
                        nemodar[username]['tale4']=[]
                    if 'tale5' not in key:
                        nemodar[username]['tale5']=[]
                    if 'tale6' not in key:
                        nemodar[username]['tale6']=[]
                    if 'tale7' not in key:
                        nemodar[username]['tale7']=[]
                    if 'tale8' not in key:
                        nemodar[username]['tale8']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale9']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale10']=[]
                    else:
                        pass
                if 9<jamemtiaz<20:
                    sendMessage(chat_id,'خیلی پایین، احتمالا این تله زندگی در ذهن شما شکل نگرفته .')
                elif 19<jamemtiaz<30:
                    sendMessage(chat_id,'نسبتا پایین، این تله زندگی ممکن است گاهی اوقات یقه شما را بگیرد')
                elif 29<jamemtiaz<40:
                    sendMessage(chat_id,'متوسط، این تله زندگی باعث مشکلاتی برای شما شده است')
                elif 39<jamemtiaz<50:
                    sendMessage(chat_id,'بالا، بدون شک یکی از تله‌های زندگی شماست')
                else:
                    sendMessage(chat_id,'شدید، این تله زندگی دقیقا یکی از تله‌های اصلی شماست')
                if jamemtiaz>19:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی رهاشدگی,\n۱. رهاشدگی دوران کودکی‌تان را درک کنید.,\n۲. احساس‌های مربوط به رهاشدگی را بازنگری کنید و حساسیت‌های خود را به از دست ‌دادن افراد نزدیک، ترس از تنهایی و نیاز به آویزان شدن و وابستگی بیمارگونه بشناسید.,\n۳. روابط گذشته را بررسی کنید تا الگوهای منجر به عود و بازگشت تله زندگی را بشناسید و فهرستی از خطاهای فکری و رفتاری ناشی از رهاشدگی تهیه کنید.,\n۴. از رابطه با افراد بی‌ثبات، بی‌تعهد و تنوع‌طلب اجتناب کنید، ولو اینکه این افراد برای شما جذابیت و کشش زیادی داشته باشند.,\n۵. وقتی که نامزدی پیدا می‌کنید که متعهد و باثبات است به او اعتماد کنید. باور کنید که او برای همیشه در کنار شما می‌ماند و شما را ترک نمی‌کند.,\n۶. حسادت نکنید، به همسرتان آویزان نشوید و به جدایی‌های معمول زندگی، واکنش افراطی نشان ندهید. ')
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی بی‌اعتمادی و بدرفتاری,\n۱. در صورت امکان از درمانگری صاحبْ‌صلاحیت برای تغییر این تله زندگی کمک بگیرید. مخصوصا اگد سابقه‌ای از بدرفتاری جنسی یا جسمی داشته‌اید.,\n۲. دوستی قابل اعتماد پیدا کنید. تمرین‌های مربوط به تصویرسازی ذهنی را انجام دهید. سعی کنید خاطرات به بدرفتاری را به‌یاد بیاورید و حوادث را با جزئیات کامل بازگو کنید.,\n۳. در حین تصویرسازی ذهنی، خشم خود را بر سر فردی که از شما سوءاستفاده کرده‌ است، خالی کنید. با این کار در تصویر ذهنی بر احساس عجز و بیچارگی خود، غلبه کنید.,\n۴. خودتان را مقصر نپندارید. شما مستحق بدرفتاری و سوءاستفاده شدن نیستید. از فرد بدرفتار، عذرخواهی نکنید.,\n۵. در عین حال که به تغییر این تله زندگی می‌پردازید، به‌تدریج رابطه خو با افراد سوءاستفاده‌گر قطع، کنید.,\n۶. در صورت امکان برای فردی که از شما سوءاستفاده کرده است، پیامدها و اثرات رفتارش بر زندگی فعلی‌تان را بازگو کنید یا برای او در این زمینه، نامه بنویسید.,\n۷. بدرفتاری‌های موجود در رابطه‌های فعلی‌تان را تحمل نکنید.,\n۸. سعی کنید با فردی قابل اعتماد وارد رابطه‌ای صمیمی شوید. به کسی اعتماد کنید که از اعتماد شما سوءاستفاده نمی‌کند,\n۹. سعی کنید با افرادی رابطه برقرار کنید که قصد آسیب زدن به شما را ندارند و به حقوق شما احترام می‌گذارند.,\n۱۰. با نزدیکان خود بدرفتاری نکنید.')
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                        sendMessage(chat_id,' تغییر تله زندگی محرومیت هیجانی,\n۱.محرومیت کودکی‌تان را درک کنید. کودک درون و آسیب‌دیده درون را حس کنید.,\n۲. احساس‌های محرومیت در روابط فعلی‌تان را به دقت زیر نظر بگیرید. نیاز به محبت، همدلی و راهنمایی را به‌خوبی لمس کنید.,\n۳. روابط گذشته خود را به منظور روشن‌سازی الگوی حاکم بر روابط بررسی کنید. موانعی را که باعث عدم تغییر شما می‌شوند، فهرست کنید.,\n.  از رابطه با افراد سرد و بی مهری که شما را به شدت مجذوب خودشان می کنند، دوری کنید.۴,\n. وقتی که فرد مورد علاقه شما از لحاظ هیجانی آدم سالمی است از این فرصت استفاده کنید تا روابط خود را بهبود ببخشید. نیازهای خودتان را بازگو کنید. به طرف مقابل، آسیب پذیری های خود را بگویید,\n۶. از مقصر دانستن نامزدتان و پرتوقعی خود، دست بردارید.') #rahkarha
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی طرد اجتماعی ,\n۱.ریشه‌های تحولی تله زندگی طرد اجتماعی را را در دوران کودکی‌تان درک کنید. احساس حقارت و انزوای کودک درونتان را درک کنید.,\n۲.موقعیت‌هایی را بنویسید که در زندگی روزمره خود دچار احساس آشفتگی و اضطراب می‌شوید.,\n۳. موقعیت‌هایی را بنویسید که از آنها اجتناب می‌کنید.,\n۴. چنانچه در موقعیت‌هایی دچار احساس تنهایی و تفاوت می‌شوید یا جبران افراطی یا حمله متقابل، سعی در پنهان‌سازی این احساس‌ها دارید، سعی کنید این موقعیت ها را بنویسید.,\n۵. مراحل اول تا چهارم را بنویسید سپس ویژگی‌هایی را بنویسید که باعث می‌شوند از دیگران منزوی شوید، احساس حقارت کنید یا آسیب‌پذیری جلوه کنید.,\n۶. اگر واقعا مشکلات و کمبودهایی دارید که واقعی هستند، پس راهکارهایی را برای غلبه بر این مشکلات و کمبودها یا کاهش اثرات آنها پیدا کنید، به تدریج بر این مشکلات غلبه کنید.,\n۷. در اهمیت عیب‌ها و نقص‌هایی که نتوانسته‌اید تغییر بدهید تجدید نظر کنید. منظور این است که دیدگاه خودتان را درباره عیب‌ها و نقص‌های تغییر ناپذیر، عوض کنید.,\n۸. برای هرکدام از عیب‌ها و نقص‌های خود، کارت آموزشی تهیه کنید.,\n۹. از موقعیت‌های کاری و اجتماعی که اجتناب می‌کنید، سلسله‌مراتبی تهیه کنید. سعی کنید به تدریج به این موقعیت‌ها وارد شوید.,\n۱۰. وقتی در جمع به‌سر می‌برید سعی کنید آغازگر مکالمه با دیگران باشید,\n۱۱. سعی‌کنید در گروه‌ها شخصیت اصلی خودتان را بروز دهید و نقش بازی نکنید.,\n۱۲. دست از تلاش برای جبران افراطی حوزه.های نادلپذیر، ناخوشایند و نامحبوب بردارید.')
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی وابستگی,\n۱.ریشه‌های تحولی وابستگی در دوران کودکی‌تان را درک کنید. بی کفایتی و وابستگی کودک درون را تجربه کنید.,\n۲. موقعیت‌ها، وظایف، مسئولیت‌ها و تصمیم‌هایی را بنویسید که در زندگی روزمره برای شما چالش‌آفرین هستند و برای انجام این وظایف، ورود به موقعیت‌ها و پذیرش مسئولیت‌ها و اتخاذ تصمیم‌ها به کمک یا نظر دیگران، وابسته هستند.,\n۳. چالش‌ها تغییرات یا دل‌نگرانی‌هایی را بنویسید که دلیل ترس از آن‌ها اجتناب می‌کنید.,\n۴. به گونه‌ای نظام‌مند، خودتان را مجبور کنید که وظایف روزمره را بدون کمک دیگران انجام بدهید و تصمیم‌ها را بدون کمک‌طلبی اتخاذ کنید. چالش‌هایی را که از آنها اجتناب می‌کنید، برعهده بگیرید. در ابتدا از وظایف و تکالیف آسان و راحت شروع کنید.,\n۵. زمانی‌که در انجام و برعهده گرفتن مسئولیت‌ها موفق شدید به خودتان امتیاز بدهید. پاداش دهی به خود را دست کم نگیرید. اگر در انجام مسئولیت‌ها شکست خوردید، کارها را رها نکنید و مایوس نشوید. دست از طلب برندارید تا به هدف خود برسید.,\n۶. روابط گذشته خود را بررسی کنید و الگوهای وابستگی تکراری را مشخص سازید. علائم گرفتار شدن در تله زندگی را بنویسید تا به دام آنها نیفتید.,\n۷. از ارتباط با نامزد قوی، مستقل و سخت حمایتگر، خودداری کنید، ولو اینکه این فرد در شما کشش و جذابیت زیادی ایجاد کند.,\n۸. اگر نامزد شما بر اساس مساوات و احترام متقابل با شما رفتار می‌کند و به شما فرصت مسئولیت‌پذیری و نظردهی می‌دهد این فرصت ها را از دست ندهید.,\n۹. اگر همسر یا رئیس و کارمند تان به شما کمک کمک لازم را نمی‌کنند زبان به شکایت باز نکنید. اصرار نورزید که از جانب این افراد راهنمایی بگیرید یا توقع نداشته باشید خیال شما را جمع کنند.,\n۱۰. در حوزه شغلی به تدریج چالش‌ها یا مسئولیت‌های جدیدی بپذیرید، و به تدریج آنها را انجام دهید.,\n۱۱. اگر شما در زمره افراد مستقل‌نما هستید، از نیازتان برای کمک‌خواهی آگاه باشید. از دیگران کمک بگیرید. مسئولیت‌های فراتر از توان را نپذیرید. از اضطراب خود به عنوان علامت استفاده کنید تا بدانید که چقدر باید مسئولیت برعهده بگیرید')
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی آسیب پذیری,\n۱.ریشه‌های تحولی زندگیتان را درک کنید.,\n۲. فهرستی از ترس‌های خود تهیه کنید.,\n۳. موقعیت‌های استرس‌برانگیز را طبق سلسله مراتب، نظم بدهید.,\n۴. افراد صمیمی زندگی‌تان (مثل همسر، فرزند و اعضای خانواده) را ملاقات کنید و از آنها بخواهید که برای برخورد جدی و اساسی با ترس‌هایتان به شما کمک کنند.,\n۵. احتمال وقوع حوادث ترس‌برانگیز را بررسی کنید.,\n۶. برای هر کدام از ترس‌های خود، کارت آموزشی تهیه کنید.,\n۷. با کودک درون حرف بزنید. برای کودک درون، والدی توانمند و شجاع باشید.,\n۸. تمرین‌های آرامش را انجام دهید.,\n۹. با استفاده از تکنیک تصویرسازی ذهنی برعلیه ترس‌ها، موضع بگیرید.,\n۱۰. در زندگی واقعی بر ترس‌هایتان غلبه کنید,\n۱۱. برای هر کدام از این مراحل که با موفقیت پشت سر گذاشتید، به خودتان پاداش بدهید.')
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی نقص/ شرم,\n۱.احساس‌های بی‌ارزشی و شرمساری دوران کودکی را درک کنید. کودک آسیب دیده درون را حس کنید.,\n۲. فهرستی از شیوه‌های مقابله خود (تسلیم فرار و حمله) برای کنار آمدن با تله زندگی را بنویسید.,\n۳. تلاش کنید دست از رفتارهای مقابله‌ای فرار یا حمله بردارید,\n۴. احساس‌های شرم و بی‌ارزشی را زیر نظر بگیرید.,\n۵. معیارهایتان را برای انتخاب نامزد جذاب و نامزد غیرجذاب را بنویسید.,\n۶. نقاط ضعف و نقاط قوت خود را در دوران کودکی و دوران فعلی بنویسید.,\n۷. نقاط ضعف فعلی خود را به طور جدی ارزیابی کنید.,\n۸. برای تغییر نقاط ضعف تغییرپذیر، برنامه ریزی کنید.,\n۹. نامه‌ای به والد (یا والدین) سرزنشگرتان بنویسید.,\n۱۰. کارت آموزشی تهیه کنید.,\n۱۱. تلاش کنید در روابط صمیمی خود صادق‌تر باشید.,\n۱۲. عشق و محبت افراد نزدیک خود را بپذیرید.,\n۱۳. اجازه ندهید دیگران به رفتارهای توهین‌آمیز و نامحترمانه‌شان با شما ادامه دهند.,\n۱۴. اگر در روابط خود به طرف مقابل ایراد می‌گیرید و سرزنش می‌کنید، دست از این کار بردارید')
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی اطاعت,\n۱.ریشه‌های تحولی تله زندگی اطاعت را در دوران کودکی‌تان بشناسید و درک کنید کودک درون مطیع و فرمان بردار خود را بشناسید.,\n۲. موقعیت‌هایی را بشناسید که در محل کار یا در خانه تحت سلطه دیگران قرار می گیرید یا موقعیت‌هایی را بشناسید که نیازهای‌تان را فدای دیگران می‌کنید.,\n۳. در بسیاری از جنبه های زندگی برای خودتان علایق و ایده‌هایی دست و پا کنید (مثل سینما، غذا، تفریح، اوقات فراغت و استفاده از زمان و...) به تدریج با این کار خودتان و نیازهای‌تان را بشناسید.,\n۴. ببینید که چقدر به دیگران کمک می‌کنید و در مقابل، دیگران چقدر به شما کمک می‌کنند. چقدر برای دیگران وقت می‌گذارید و در برابر آنها چقدر برای شما وقت می‌گذارند.,\n۵. رفتا‌رهای منفعلانه_پرخاشگرانه را کنار بگذارید. خودتان را مجبور به رفتارهای جسارتمندانه کنید تا حق‌تان پایمال نشود. ابتدا خواسته‌های کوچک خود را برای دیگران مطرح کنید.,\n۶. از دیگران بخواهید که از شما حمایت و مراقبت کنند. از آنها کمک بگیرید و مشکلات خودتان را با آنها در میان بگذارید. سعی کنید ترازوی دادوستد شما در روابط بین‌فردی تا اندازه‌ای متعادل باشد.,\n۷. با افراد خودخواه و خودمحور که به نیازهای شما پشیزی ارزش قائل نمی‌شوند، قطع رابطه کنید. وقتی احساس کردید در روابط یک‌طرفه و ناسالم گرفتار شده‌اید، رابطه را تغییر بدهید یا از خیر رابطه بگذرید.,\n۸. تمرین کنید به جای موافقت با دیگران، با آنها جسارتمندانه برخورد کنید. به محض این که عصبانی شدید با شیوه ای مناسب خشم خودتان را ابراز کنید. اگر کسی موجب ناراحتی و آزردگی خاطر شما شد، یاد بگیرید که آرامش خودتان را حفظ کنید و سپس دلخوری‌تان را به او بگویید.,\n۹. برای گرایش خودتان به جلب رضایت دیگران، دلیل تراشی نکنید. مدام به خودتان نگویید بلاهایی که از این راه بر سر شما می‌آیند اهمیتی ندارند.,\n۱۰. به بررسی روابط گذشته خود بپردازید. دوستان یا افراد کنترلگر نیازمند را مشخص کنید. در روابط بعدی خود مواظب باشید با چنین افرادی رابطه برقرار نکنید. فهرستی از ویژگی های افراد خودخواه، مغرور، بی‌مسئولیت یا وابسته تهیه کنید که در شما اشتیاق زیادی برای برقراری رابطه ایجاد می‌کنند.,\n۱۱. به رابطه‌ای ارزش قائل شوید که طرف مقابل، نیازهای اصلی شما را ارضا می‌کند، از شما نظر می‌خواهد و به شما مجال می‌دهد که توانایی‌های خودتان را بشناسید.,\n۱۲. در محل‌کار، قاطع‌تر باشید. به کارهای خودتان ارزش قائل شوید. اگر فکر می‌کنید که درخواست پیشرفت و ارتقای شغلی حق شماست، از تقاضای درخواست به سادگی نگذرید. مسئولیت های افراطی را به دیگران واگذار کنید.,\n۱۳. (درباره افراد سرکش و نافرمان صادق است) سعی نکنید در برابر درخواست‌های دیگران به لاک دفاعی بروید. تلاش کنید درخواست های دیگران را درک کنید. خواسته های خودتان را بشناسید. برخی اوقات شما از سر لجبازی با خواسته افراد مافوق خود مخالفت می‌کنید. دست از لجبازی بردارید تا مشکل شما حل شود.,\n۱۴. نتیجه‌گیری‌های خودتان را از این مراحل روی کارت آموزشی بنویسید و آن را همراه خودتان داشته باشید')
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی معیارهای سخت‌گیرانه,\n۱.حوزه‌هایی از زندگی‌تان را مشخص کنید که زیر سیطره معیارهای سختگیرانه یا نامتعادل قرار گرفته‌اند.,\n۲. مزایای تلاش برای رسیدن به این معیارهای سخت‌گیرانه را بنویسید.,\n۳. معایب تلاش برای رسیدن به معیارهای سختگیرانه را بنویسید.,\n۴. تلاش کنید که به تصور خود پروبال بدهید و زندگی رها از این معیارها را تجسم کنید.,\n۵. ریشه های تحولی و دلایل شکل‌گیری تله زندگی‌تان را درک کنید.,\n۶. تصور کنید که اگر توقعات خود را کم کنید چه اتفاقی می‌افتد.,\n۷. میزان زمانی را که صرف حفظ این معیارها می کنید، مشخص سازید.,\n۸. با نظرخواهی از افراد معقول دیدی دقیق‌تر و منطقی‌تر نسبت به این معیارها پیدا کنید.,\n۹. با برنامه‌ریزی تدریجی یا تغییر رفتار، در راستای ارضا نیازهای اصلی‌تر گام بردارید.')
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                        sendMessage(chat_id,'غلبه بر مشکلات تله زندگی استحقاق,\n۱.فهرستی از مزایا و معایب نپذیرفتن محدودیت ها تهیه کنید. این کارها برای انگیزه‌مندسازی شما ضروری است.,\n۲. بهانه تراشی‌های خود را برای نپذیرفتن محدودیت ها کنار بگذارید.,\n۳. دقت کنید که چگونه نپذیرفتن محدودیت‌ها در زندگی روزمره برای شما مشکل درست می‌کند. فهرستی از این مشکلات تهیه کنید.,\n۴. برای این که یادتان باشد که با بی‌انضباطی و استحقاق خود در موقعیت‌ها بجنگید، کارت آموزشی درست کنید.,\n۵. همچنان که به دنبال تغییر هستید از دیگران درباره میزان تغییر خود، نظرخواهی کنید.,\n۶. تلاش کنید با اطرافیان خود، همدلی کنید.,\n۷. اگر تله زندگی شما از نوع حمله برعلیه سایر تله‌هاست سعی کنید طرح های زیربنایی را درک کنید و از تکنیک‌های مربوط به هر کدام از آنها استفاده نمایید.,\n۸. اگر در انضباط شخصی مشکل دارید، کارهای خود را بر اساس میزان ناکام سازی و بیزارسازی، درجه‌بندی کنید. کارهای خود را سلسله‌مراتبی در نظر بگیرید و برای انجام آنها اقدام کنید.,\n۹. اگر در کنترل هیجان‌های خود مشکل دارید از تکنیک "محروم‌سازی" استفاده کنید.,\n۱۰. اگر گرفتار استحقاق از نوع وابستگی شده‌اید، کارهایتان را براساس میزان سختی درجه‌بندی کنید. آنگاه به تدریج کارها را از آسان به سخت و بدون کمک دیگران انجام دهید. از کارهای آسان‌تر شروع کنید تا به خودتان ثابت کنید که آدم با کفایتی هستید.')
                    else:
                        pass
                    sendMessage(chat_id,'آیا تمایل دارید نمودار غلبه بر تله زتدگی خود را ببینید؟\n در صورت تمایل، عبارت "نمودار" را ارسال کنید')
                    sendMessage(chat_id,'در صورت تمایل برای دریافت مشاوره تخصصی می‌توانید با شماره زیر تماس بگیرید:\n09123671593')

                else:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                    else:
                        pass
                    sendMessage(chat_id,'تبریک میگم، با توجه به پاسخ ارسال شده شما در دام این تله گرفتار نشدید')
                write_json(nemodar)
        elif text=='3': 
            javabsoal= read_json()
            nemodar =read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==10:
                javabsoal[username].append('3') #yazdahomin ozv list username
                write_json(javabsoal)
                listemtiaz =[]
                for i in range(1,12):
                    emtiaz = int(javabsoal[username][i])
                    listemtiaz.append(emtiaz)
                jamemtiaz=sum(listemtiaz)
                for key in nemodar.keys():
                    if username not in key:
                        nemodar[username]={}
                    else:
                        pass
                for key in nemodar[username].keys():
                    if 'tale1' not in key:
                        nemodar[username]['tale1']=[]
                    if 'tale2' not in key:
                        nemodar[username]['tale2']=[]
                    if 'tale3' not in key:
                        nemodar[username]['tale3']=[]
                    if 'tale4' not in key:
                        nemodar[username]['tale4']=[]
                    if 'tale5' not in key:
                        nemodar[username]['tale5']=[]
                    if 'tale6' not in key:
                        nemodar[username]['tale6']=[]
                    if 'tale7' not in key:
                        nemodar[username]['tale7']=[]
                    if 'tale8' not in key:
                        nemodar[username]['tale8']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale9']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale10']=[]
                    else:
                        pass
                if 9<jamemtiaz<20:
                    sendMessage(chat_id,'خیلی پایین، احتمالا این تله زندگی در ذهن شما شکل نگرفته .')
                elif 19<jamemtiaz<30:
                    sendMessage(chat_id,'نسبتا پایین، این تله زندگی ممکن است گاهی اوقات یقه شما را بگیرد')
                elif 29<jamemtiaz<40:
                    sendMessage(chat_id,'متوسط، این تله زندگی باعث مشکلاتی برای شما شده است')
                elif 39<jamemtiaz<50:
                    sendMessage(chat_id,'بالا، بدون شک یکی از تله‌های زندگی شماست')
                else:
                    sendMessage(chat_id,'شدید، این تله زندگی دقیقا یکی از تله‌های اصلی شماست')
                if jamemtiaz>19:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی رهاشدگی,\n۱. رهاشدگی دوران کودکی‌تان را درک کنید.,\n۲. احساس‌های مربوط به رهاشدگی را بازنگری کنید و حساسیت‌های خود را به از دست ‌دادن افراد نزدیک، ترس از تنهایی و نیاز به آویزان شدن و وابستگی بیمارگونه بشناسید.,\n۳. روابط گذشته را بررسی کنید تا الگوهای منجر به عود و بازگشت تله زندگی را بشناسید و فهرستی از خطاهای فکری و رفتاری ناشی از رهاشدگی تهیه کنید.,\n۴. از رابطه با افراد بی‌ثبات، بی‌تعهد و تنوع‌طلب اجتناب کنید، ولو اینکه این افراد برای شما جذابیت و کشش زیادی داشته باشند.,\n۵. وقتی که نامزدی پیدا می‌کنید که متعهد و باثبات است به او اعتماد کنید. باور کنید که او برای همیشه در کنار شما می‌ماند و شما را ترک نمی‌کند.,\n۶. حسادت نکنید، به همسرتان آویزان نشوید و به جدایی‌های معمول زندگی، واکنش افراطی نشان ندهید. ')
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی بی‌اعتمادی و بدرفتاری,\n۱. در صورت امکان از درمانگری صاحبْ‌صلاحیت برای تغییر این تله زندگی کمک بگیرید. مخصوصا اگد سابقه‌ای از بدرفتاری جنسی یا جسمی داشته‌اید.,\n۲. دوستی قابل اعتماد پیدا کنید. تمرین‌های مربوط به تصویرسازی ذهنی را انجام دهید. سعی کنید خاطرات به بدرفتاری را به‌یاد بیاورید و حوادث را با جزئیات کامل بازگو کنید.,\n۳. در حین تصویرسازی ذهنی، خشم خود را بر سر فردی که از شما سوءاستفاده کرده‌ است، خالی کنید. با این کار در تصویر ذهنی بر احساس عجز و بیچارگی خود، غلبه کنید.,\n۴. خودتان را مقصر نپندارید. شما مستحق بدرفتاری و سوءاستفاده شدن نیستید. از فرد بدرفتار، عذرخواهی نکنید.,\n۵. در عین حال که به تغییر این تله زندگی می‌پردازید، به‌تدریج رابطه خو با افراد سوءاستفاده‌گر قطع، کنید.,\n۶. در صورت امکان برای فردی که از شما سوءاستفاده کرده است، پیامدها و اثرات رفتارش بر زندگی فعلی‌تان را بازگو کنید یا برای او در این زمینه، نامه بنویسید.,\n۷. بدرفتاری‌های موجود در رابطه‌های فعلی‌تان را تحمل نکنید.,\n۸. سعی کنید با فردی قابل اعتماد وارد رابطه‌ای صمیمی شوید. به کسی اعتماد کنید که از اعتماد شما سوءاستفاده نمی‌کند,\n۹. سعی کنید با افرادی رابطه برقرار کنید که قصد آسیب زدن به شما را ندارند و به حقوق شما احترام می‌گذارند.,\n۱۰. با نزدیکان خود بدرفتاری نکنید.')
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                        sendMessage(chat_id,' تغییر تله زندگی محرومیت هیجانی,\n۱.محرومیت کودکی‌تان را درک کنید. کودک درون و آسیب‌دیده درون را حس کنید.,\n۲. احساس‌های محرومیت در روابط فعلی‌تان را به دقت زیر نظر بگیرید. نیاز به محبت، همدلی و راهنمایی را به‌خوبی لمس کنید.,\n۳. روابط گذشته خود را به منظور روشن‌سازی الگوی حاکم بر روابط بررسی کنید. موانعی را که باعث عدم تغییر شما می‌شوند، فهرست کنید.,\n.  از رابطه با افراد سرد و بی مهری که شما را به شدت مجذوب خودشان می کنند، دوری کنید.۴,\n. وقتی که فرد مورد علاقه شما از لحاظ هیجانی آدم سالمی است از این فرصت استفاده کنید تا روابط خود را بهبود ببخشید. نیازهای خودتان را بازگو کنید. به طرف مقابل، آسیب پذیری های خود را بگویید,\n۶. از مقصر دانستن نامزدتان و پرتوقعی خود، دست بردارید.') #rahkarha
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی طرد اجتماعی ,\n۱.ریشه‌های تحولی تله زندگی طرد اجتماعی را را در دوران کودکی‌تان درک کنید. احساس حقارت و انزوای کودک درونتان را درک کنید.,\n۲.موقعیت‌هایی را بنویسید که در زندگی روزمره خود دچار احساس آشفتگی و اضطراب می‌شوید.,\n۳. موقعیت‌هایی را بنویسید که از آنها اجتناب می‌کنید.,\n۴. چنانچه در موقعیت‌هایی دچار احساس تنهایی و تفاوت می‌شوید یا جبران افراطی یا حمله متقابل، سعی در پنهان‌سازی این احساس‌ها دارید، سعی کنید این موقعیت ها را بنویسید.,\n۵. مراحل اول تا چهارم را بنویسید سپس ویژگی‌هایی را بنویسید که باعث می‌شوند از دیگران منزوی شوید، احساس حقارت کنید یا آسیب‌پذیری جلوه کنید.,\n۶. اگر واقعا مشکلات و کمبودهایی دارید که واقعی هستند، پس راهکارهایی را برای غلبه بر این مشکلات و کمبودها یا کاهش اثرات آنها پیدا کنید، به تدریج بر این مشکلات غلبه کنید.,\n۷. در اهمیت عیب‌ها و نقص‌هایی که نتوانسته‌اید تغییر بدهید تجدید نظر کنید. منظور این است که دیدگاه خودتان را درباره عیب‌ها و نقص‌های تغییر ناپذیر، عوض کنید.,\n۸. برای هرکدام از عیب‌ها و نقص‌های خود، کارت آموزشی تهیه کنید.,\n۹. از موقعیت‌های کاری و اجتماعی که اجتناب می‌کنید، سلسله‌مراتبی تهیه کنید. سعی کنید به تدریج به این موقعیت‌ها وارد شوید.,\n۱۰. وقتی در جمع به‌سر می‌برید سعی کنید آغازگر مکالمه با دیگران باشید,\n۱۱. سعی‌کنید در گروه‌ها شخصیت اصلی خودتان را بروز دهید و نقش بازی نکنید.,\n۱۲. دست از تلاش برای جبران افراطی حوزه.های نادلپذیر، ناخوشایند و نامحبوب بردارید.')
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی وابستگی,\n۱.ریشه‌های تحولی وابستگی در دوران کودکی‌تان را درک کنید. بی کفایتی و وابستگی کودک درون را تجربه کنید.,\n۲. موقعیت‌ها، وظایف، مسئولیت‌ها و تصمیم‌هایی را بنویسید که در زندگی روزمره برای شما چالش‌آفرین هستند و برای انجام این وظایف، ورود به موقعیت‌ها و پذیرش مسئولیت‌ها و اتخاذ تصمیم‌ها به کمک یا نظر دیگران، وابسته هستند.,\n۳. چالش‌ها تغییرات یا دل‌نگرانی‌هایی را بنویسید که دلیل ترس از آن‌ها اجتناب می‌کنید.,\n۴. به گونه‌ای نظام‌مند، خودتان را مجبور کنید که وظایف روزمره را بدون کمک دیگران انجام بدهید و تصمیم‌ها را بدون کمک‌طلبی اتخاذ کنید. چالش‌هایی را که از آنها اجتناب می‌کنید، برعهده بگیرید. در ابتدا از وظایف و تکالیف آسان و راحت شروع کنید.,\n۵. زمانی‌که در انجام و برعهده گرفتن مسئولیت‌ها موفق شدید به خودتان امتیاز بدهید. پاداش دهی به خود را دست کم نگیرید. اگر در انجام مسئولیت‌ها شکست خوردید، کارها را رها نکنید و مایوس نشوید. دست از طلب برندارید تا به هدف خود برسید.,\n۶. روابط گذشته خود را بررسی کنید و الگوهای وابستگی تکراری را مشخص سازید. علائم گرفتار شدن در تله زندگی را بنویسید تا به دام آنها نیفتید.,\n۷. از ارتباط با نامزد قوی، مستقل و سخت حمایتگر، خودداری کنید، ولو اینکه این فرد در شما کشش و جذابیت زیادی ایجاد کند.,\n۸. اگر نامزد شما بر اساس مساوات و احترام متقابل با شما رفتار می‌کند و به شما فرصت مسئولیت‌پذیری و نظردهی می‌دهد این فرصت ها را از دست ندهید.,\n۹. اگر همسر یا رئیس و کارمند تان به شما کمک کمک لازم را نمی‌کنند زبان به شکایت باز نکنید. اصرار نورزید که از جانب این افراد راهنمایی بگیرید یا توقع نداشته باشید خیال شما را جمع کنند.,\n۱۰. در حوزه شغلی به تدریج چالش‌ها یا مسئولیت‌های جدیدی بپذیرید، و به تدریج آنها را انجام دهید.,\n۱۱. اگر شما در زمره افراد مستقل‌نما هستید، از نیازتان برای کمک‌خواهی آگاه باشید. از دیگران کمک بگیرید. مسئولیت‌های فراتر از توان را نپذیرید. از اضطراب خود به عنوان علامت استفاده کنید تا بدانید که چقدر باید مسئولیت برعهده بگیرید')
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی آسیب پذیری,\n۱.ریشه‌های تحولی زندگیتان را درک کنید.,\n۲. فهرستی از ترس‌های خود تهیه کنید.,\n۳. موقعیت‌های استرس‌برانگیز را طبق سلسله مراتب، نظم بدهید.,\n۴. افراد صمیمی زندگی‌تان (مثل همسر، فرزند و اعضای خانواده) را ملاقات کنید و از آنها بخواهید که برای برخورد جدی و اساسی با ترس‌هایتان به شما کمک کنند.,\n۵. احتمال وقوع حوادث ترس‌برانگیز را بررسی کنید.,\n۶. برای هر کدام از ترس‌های خود، کارت آموزشی تهیه کنید.,\n۷. با کودک درون حرف بزنید. برای کودک درون، والدی توانمند و شجاع باشید.,\n۸. تمرین‌های آرامش را انجام دهید.,\n۹. با استفاده از تکنیک تصویرسازی ذهنی برعلیه ترس‌ها، موضع بگیرید.,\n۱۰. در زندگی واقعی بر ترس‌هایتان غلبه کنید,\n۱۱. برای هر کدام از این مراحل که با موفقیت پشت سر گذاشتید، به خودتان پاداش بدهید.')
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی نقص/ شرم,\n۱.احساس‌های بی‌ارزشی و شرمساری دوران کودکی را درک کنید. کودک آسیب دیده درون را حس کنید.,\n۲. فهرستی از شیوه‌های مقابله خود (تسلیم فرار و حمله) برای کنار آمدن با تله زندگی را بنویسید.,\n۳. تلاش کنید دست از رفتارهای مقابله‌ای فرار یا حمله بردارید,\n۴. احساس‌های شرم و بی‌ارزشی را زیر نظر بگیرید.,\n۵. معیارهایتان را برای انتخاب نامزد جذاب و نامزد غیرجذاب را بنویسید.,\n۶. نقاط ضعف و نقاط قوت خود را در دوران کودکی و دوران فعلی بنویسید.,\n۷. نقاط ضعف فعلی خود را به طور جدی ارزیابی کنید.,\n۸. برای تغییر نقاط ضعف تغییرپذیر، برنامه ریزی کنید.,\n۹. نامه‌ای به والد (یا والدین) سرزنشگرتان بنویسید.,\n۱۰. کارت آموزشی تهیه کنید.,\n۱۱. تلاش کنید در روابط صمیمی خود صادق‌تر باشید.,\n۱۲. عشق و محبت افراد نزدیک خود را بپذیرید.,\n۱۳. اجازه ندهید دیگران به رفتارهای توهین‌آمیز و نامحترمانه‌شان با شما ادامه دهند.,\n۱۴. اگر در روابط خود به طرف مقابل ایراد می‌گیرید و سرزنش می‌کنید، دست از این کار بردارید')
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی اطاعت,\n۱.ریشه‌های تحولی تله زندگی اطاعت را در دوران کودکی‌تان بشناسید و درک کنید کودک درون مطیع و فرمان بردار خود را بشناسید.,\n۲. موقعیت‌هایی را بشناسید که در محل کار یا در خانه تحت سلطه دیگران قرار می گیرید یا موقعیت‌هایی را بشناسید که نیازهای‌تان را فدای دیگران می‌کنید.,\n۳. در بسیاری از جنبه های زندگی برای خودتان علایق و ایده‌هایی دست و پا کنید (مثل سینما، غذا، تفریح، اوقات فراغت و استفاده از زمان و...) به تدریج با این کار خودتان و نیازهای‌تان را بشناسید.,\n۴. ببینید که چقدر به دیگران کمک می‌کنید و در مقابل، دیگران چقدر به شما کمک می‌کنند. چقدر برای دیگران وقت می‌گذارید و در برابر آنها چقدر برای شما وقت می‌گذارند.,\n۵. رفتا‌رهای منفعلانه_پرخاشگرانه را کنار بگذارید. خودتان را مجبور به رفتارهای جسارتمندانه کنید تا حق‌تان پایمال نشود. ابتدا خواسته‌های کوچک خود را برای دیگران مطرح کنید.,\n۶. از دیگران بخواهید که از شما حمایت و مراقبت کنند. از آنها کمک بگیرید و مشکلات خودتان را با آنها در میان بگذارید. سعی کنید ترازوی دادوستد شما در روابط بین‌فردی تا اندازه‌ای متعادل باشد.,\n۷. با افراد خودخواه و خودمحور که به نیازهای شما پشیزی ارزش قائل نمی‌شوند، قطع رابطه کنید. وقتی احساس کردید در روابط یک‌طرفه و ناسالم گرفتار شده‌اید، رابطه را تغییر بدهید یا از خیر رابطه بگذرید.,\n۸. تمرین کنید به جای موافقت با دیگران، با آنها جسارتمندانه برخورد کنید. به محض این که عصبانی شدید با شیوه ای مناسب خشم خودتان را ابراز کنید. اگر کسی موجب ناراحتی و آزردگی خاطر شما شد، یاد بگیرید که آرامش خودتان را حفظ کنید و سپس دلخوری‌تان را به او بگویید.,\n۹. برای گرایش خودتان به جلب رضایت دیگران، دلیل تراشی نکنید. مدام به خودتان نگویید بلاهایی که از این راه بر سر شما می‌آیند اهمیتی ندارند.,\n۱۰. به بررسی روابط گذشته خود بپردازید. دوستان یا افراد کنترلگر نیازمند را مشخص کنید. در روابط بعدی خود مواظب باشید با چنین افرادی رابطه برقرار نکنید. فهرستی از ویژگی های افراد خودخواه، مغرور، بی‌مسئولیت یا وابسته تهیه کنید که در شما اشتیاق زیادی برای برقراری رابطه ایجاد می‌کنند.,\n۱۱. به رابطه‌ای ارزش قائل شوید که طرف مقابل، نیازهای اصلی شما را ارضا می‌کند، از شما نظر می‌خواهد و به شما مجال می‌دهد که توانایی‌های خودتان را بشناسید.,\n۱۲. در محل‌کار، قاطع‌تر باشید. به کارهای خودتان ارزش قائل شوید. اگر فکر می‌کنید که درخواست پیشرفت و ارتقای شغلی حق شماست، از تقاضای درخواست به سادگی نگذرید. مسئولیت های افراطی را به دیگران واگذار کنید.,\n۱۳. (درباره افراد سرکش و نافرمان صادق است) سعی نکنید در برابر درخواست‌های دیگران به لاک دفاعی بروید. تلاش کنید درخواست های دیگران را درک کنید. خواسته های خودتان را بشناسید. برخی اوقات شما از سر لجبازی با خواسته افراد مافوق خود مخالفت می‌کنید. دست از لجبازی بردارید تا مشکل شما حل شود.,\n۱۴. نتیجه‌گیری‌های خودتان را از این مراحل روی کارت آموزشی بنویسید و آن را همراه خودتان داشته باشید')
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی معیارهای سخت‌گیرانه,\n۱.حوزه‌هایی از زندگی‌تان را مشخص کنید که زیر سیطره معیارهای سختگیرانه یا نامتعادل قرار گرفته‌اند.,\n۲. مزایای تلاش برای رسیدن به این معیارهای سخت‌گیرانه را بنویسید.,\n۳. معایب تلاش برای رسیدن به معیارهای سختگیرانه را بنویسید.,\n۴. تلاش کنید که به تصور خود پروبال بدهید و زندگی رها از این معیارها را تجسم کنید.,\n۵. ریشه های تحولی و دلایل شکل‌گیری تله زندگی‌تان را درک کنید.,\n۶. تصور کنید که اگر توقعات خود را کم کنید چه اتفاقی می‌افتد.,\n۷. میزان زمانی را که صرف حفظ این معیارها می کنید، مشخص سازید.,\n۸. با نظرخواهی از افراد معقول دیدی دقیق‌تر و منطقی‌تر نسبت به این معیارها پیدا کنید.,\n۹. با برنامه‌ریزی تدریجی یا تغییر رفتار، در راستای ارضا نیازهای اصلی‌تر گام بردارید.')
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                        sendMessage(chat_id,'غلبه بر مشکلات تله زندگی استحقاق,\n۱.فهرستی از مزایا و معایب نپذیرفتن محدودیت ها تهیه کنید. این کارها برای انگیزه‌مندسازی شما ضروری است.,\n۲. بهانه تراشی‌های خود را برای نپذیرفتن محدودیت ها کنار بگذارید.,\n۳. دقت کنید که چگونه نپذیرفتن محدودیت‌ها در زندگی روزمره برای شما مشکل درست می‌کند. فهرستی از این مشکلات تهیه کنید.,\n۴. برای این که یادتان باشد که با بی‌انضباطی و استحقاق خود در موقعیت‌ها بجنگید، کارت آموزشی درست کنید.,\n۵. همچنان که به دنبال تغییر هستید از دیگران درباره میزان تغییر خود، نظرخواهی کنید.,\n۶. تلاش کنید با اطرافیان خود، همدلی کنید.,\n۷. اگر تله زندگی شما از نوع حمله برعلیه سایر تله‌هاست سعی کنید طرح های زیربنایی را درک کنید و از تکنیک‌های مربوط به هر کدام از آنها استفاده نمایید.,\n۸. اگر در انضباط شخصی مشکل دارید، کارهای خود را بر اساس میزان ناکام سازی و بیزارسازی، درجه‌بندی کنید. کارهای خود را سلسله‌مراتبی در نظر بگیرید و برای انجام آنها اقدام کنید.,\n۹. اگر در کنترل هیجان‌های خود مشکل دارید از تکنیک "محروم‌سازی" استفاده کنید.,\n۱۰. اگر گرفتار استحقاق از نوع وابستگی شده‌اید، کارهایتان را براساس میزان سختی درجه‌بندی کنید. آنگاه به تدریج کارها را از آسان به سخت و بدون کمک دیگران انجام دهید. از کارهای آسان‌تر شروع کنید تا به خودتان ثابت کنید که آدم با کفایتی هستید.')
                    else:
                        pass
                    sendMessage(chat_id,'آیا تمایل دارید نمودار غلبه بر تله زتدگی خود را ببینید؟\n در صورت تمایل، عبارت "نمودار" را ارسال کنید')
                    sendMessage(chat_id,'در صورت تمایل برای دریافت مشاوره تخصصی می‌توانید با شماره زیر تماس بگیرید:\n09123671593')

                else:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                    else:
                        pass
                    sendMessage(chat_id,'تبریک میگم، با توجه به پاسخ ارسال شده شما در دام این تله گرفتار نشدید')
                write_json(nemodar)
        elif text=='4': 
            javabsoal= read_json()
            nemodar =read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==10:
                javabsoal[username].append('4') #yazdahomin ozv list username
                write_json(javabsoal)
                listemtiaz =[]
                for i in range(1,12):
                    emtiaz = int(javabsoal[username][i])
                    listemtiaz.append(emtiaz)
                jamemtiaz=sum(listemtiaz)
                for key in nemodar.keys():
                    if username not in key:
                        nemodar[username]={}
                    else:
                        pass
                for key in nemodar[username].keys():
                    if 'tale1' not in key:
                        nemodar[username]['tale1']=[]
                    if 'tale2' not in key:
                        nemodar[username]['tale2']=[]
                    if 'tale3' not in key:
                        nemodar[username]['tale3']=[]
                    if 'tale4' not in key:
                        nemodar[username]['tale4']=[]
                    if 'tale5' not in key:
                        nemodar[username]['tale5']=[]
                    if 'tale6' not in key:
                        nemodar[username]['tale6']=[]
                    if 'tale7' not in key:
                        nemodar[username]['tale7']=[]
                    if 'tale8' not in key:
                        nemodar[username]['tale8']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale9']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale10']=[]
                    else:
                        pass
                if 9<jamemtiaz<20:
                    sendMessage(chat_id,'خیلی پایین، احتمالا این تله زندگی در ذهن شما شکل نگرفته .')
                elif 19<jamemtiaz<30:
                    sendMessage(chat_id,'نسبتا پایین، این تله زندگی ممکن است گاهی اوقات یقه شما را بگیرد')
                elif 29<jamemtiaz<40:
                    sendMessage(chat_id,'متوسط، این تله زندگی باعث مشکلاتی برای شما شده است')
                elif 39<jamemtiaz<50:
                    sendMessage(chat_id,'بالا، بدون شک یکی از تله‌های زندگی شماست')
                else:
                    sendMessage(chat_id,'شدید، این تله زندگی دقیقا یکی از تله‌های اصلی شماست')
                if jamemtiaz>19:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی رهاشدگی,\n۱. رهاشدگی دوران کودکی‌تان را درک کنید.,\n۲. احساس‌های مربوط به رهاشدگی را بازنگری کنید و حساسیت‌های خود را به از دست ‌دادن افراد نزدیک، ترس از تنهایی و نیاز به آویزان شدن و وابستگی بیمارگونه بشناسید.,\n۳. روابط گذشته را بررسی کنید تا الگوهای منجر به عود و بازگشت تله زندگی را بشناسید و فهرستی از خطاهای فکری و رفتاری ناشی از رهاشدگی تهیه کنید.,\n۴. از رابطه با افراد بی‌ثبات، بی‌تعهد و تنوع‌طلب اجتناب کنید، ولو اینکه این افراد برای شما جذابیت و کشش زیادی داشته باشند.,\n۵. وقتی که نامزدی پیدا می‌کنید که متعهد و باثبات است به او اعتماد کنید. باور کنید که او برای همیشه در کنار شما می‌ماند و شما را ترک نمی‌کند.,\n۶. حسادت نکنید، به همسرتان آویزان نشوید و به جدایی‌های معمول زندگی، واکنش افراطی نشان ندهید. ')
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی بی‌اعتمادی و بدرفتاری,\n۱. در صورت امکان از درمانگری صاحبْ‌صلاحیت برای تغییر این تله زندگی کمک بگیرید. مخصوصا اگد سابقه‌ای از بدرفتاری جنسی یا جسمی داشته‌اید.,\n۲. دوستی قابل اعتماد پیدا کنید. تمرین‌های مربوط به تصویرسازی ذهنی را انجام دهید. سعی کنید خاطرات به بدرفتاری را به‌یاد بیاورید و حوادث را با جزئیات کامل بازگو کنید.,\n۳. در حین تصویرسازی ذهنی، خشم خود را بر سر فردی که از شما سوءاستفاده کرده‌ است، خالی کنید. با این کار در تصویر ذهنی بر احساس عجز و بیچارگی خود، غلبه کنید.,\n۴. خودتان را مقصر نپندارید. شما مستحق بدرفتاری و سوءاستفاده شدن نیستید. از فرد بدرفتار، عذرخواهی نکنید.,\n۵. در عین حال که به تغییر این تله زندگی می‌پردازید، به‌تدریج رابطه خو با افراد سوءاستفاده‌گر قطع، کنید.,\n۶. در صورت امکان برای فردی که از شما سوءاستفاده کرده است، پیامدها و اثرات رفتارش بر زندگی فعلی‌تان را بازگو کنید یا برای او در این زمینه، نامه بنویسید.,\n۷. بدرفتاری‌های موجود در رابطه‌های فعلی‌تان را تحمل نکنید.,\n۸. سعی کنید با فردی قابل اعتماد وارد رابطه‌ای صمیمی شوید. به کسی اعتماد کنید که از اعتماد شما سوءاستفاده نمی‌کند,\n۹. سعی کنید با افرادی رابطه برقرار کنید که قصد آسیب زدن به شما را ندارند و به حقوق شما احترام می‌گذارند.,\n۱۰. با نزدیکان خود بدرفتاری نکنید.')
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                        sendMessage(chat_id,' تغییر تله زندگی محرومیت هیجانی,\n۱.محرومیت کودکی‌تان را درک کنید. کودک درون و آسیب‌دیده درون را حس کنید.,\n۲. احساس‌های محرومیت در روابط فعلی‌تان را به دقت زیر نظر بگیرید. نیاز به محبت، همدلی و راهنمایی را به‌خوبی لمس کنید.,\n۳. روابط گذشته خود را به منظور روشن‌سازی الگوی حاکم بر روابط بررسی کنید. موانعی را که باعث عدم تغییر شما می‌شوند، فهرست کنید.,\n.  از رابطه با افراد سرد و بی مهری که شما را به شدت مجذوب خودشان می کنند، دوری کنید.۴,\n. وقتی که فرد مورد علاقه شما از لحاظ هیجانی آدم سالمی است از این فرصت استفاده کنید تا روابط خود را بهبود ببخشید. نیازهای خودتان را بازگو کنید. به طرف مقابل، آسیب پذیری های خود را بگویید,\n۶. از مقصر دانستن نامزدتان و پرتوقعی خود، دست بردارید.') #rahkarha
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی طرد اجتماعی ,\n۱.ریشه‌های تحولی تله زندگی طرد اجتماعی را را در دوران کودکی‌تان درک کنید. احساس حقارت و انزوای کودک درونتان را درک کنید.,\n۲.موقعیت‌هایی را بنویسید که در زندگی روزمره خود دچار احساس آشفتگی و اضطراب می‌شوید.,\n۳. موقعیت‌هایی را بنویسید که از آنها اجتناب می‌کنید.,\n۴. چنانچه در موقعیت‌هایی دچار احساس تنهایی و تفاوت می‌شوید یا جبران افراطی یا حمله متقابل، سعی در پنهان‌سازی این احساس‌ها دارید، سعی کنید این موقعیت ها را بنویسید.,\n۵. مراحل اول تا چهارم را بنویسید سپس ویژگی‌هایی را بنویسید که باعث می‌شوند از دیگران منزوی شوید، احساس حقارت کنید یا آسیب‌پذیری جلوه کنید.,\n۶. اگر واقعا مشکلات و کمبودهایی دارید که واقعی هستند، پس راهکارهایی را برای غلبه بر این مشکلات و کمبودها یا کاهش اثرات آنها پیدا کنید، به تدریج بر این مشکلات غلبه کنید.,\n۷. در اهمیت عیب‌ها و نقص‌هایی که نتوانسته‌اید تغییر بدهید تجدید نظر کنید. منظور این است که دیدگاه خودتان را درباره عیب‌ها و نقص‌های تغییر ناپذیر، عوض کنید.,\n۸. برای هرکدام از عیب‌ها و نقص‌های خود، کارت آموزشی تهیه کنید.,\n۹. از موقعیت‌های کاری و اجتماعی که اجتناب می‌کنید، سلسله‌مراتبی تهیه کنید. سعی کنید به تدریج به این موقعیت‌ها وارد شوید.,\n۱۰. وقتی در جمع به‌سر می‌برید سعی کنید آغازگر مکالمه با دیگران باشید,\n۱۱. سعی‌کنید در گروه‌ها شخصیت اصلی خودتان را بروز دهید و نقش بازی نکنید.,\n۱۲. دست از تلاش برای جبران افراطی حوزه.های نادلپذیر، ناخوشایند و نامحبوب بردارید.')
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی وابستگی,\n۱.ریشه‌های تحولی وابستگی در دوران کودکی‌تان را درک کنید. بی کفایتی و وابستگی کودک درون را تجربه کنید.,\n۲. موقعیت‌ها، وظایف، مسئولیت‌ها و تصمیم‌هایی را بنویسید که در زندگی روزمره برای شما چالش‌آفرین هستند و برای انجام این وظایف، ورود به موقعیت‌ها و پذیرش مسئولیت‌ها و اتخاذ تصمیم‌ها به کمک یا نظر دیگران، وابسته هستند.,\n۳. چالش‌ها تغییرات یا دل‌نگرانی‌هایی را بنویسید که دلیل ترس از آن‌ها اجتناب می‌کنید.,\n۴. به گونه‌ای نظام‌مند، خودتان را مجبور کنید که وظایف روزمره را بدون کمک دیگران انجام بدهید و تصمیم‌ها را بدون کمک‌طلبی اتخاذ کنید. چالش‌هایی را که از آنها اجتناب می‌کنید، برعهده بگیرید. در ابتدا از وظایف و تکالیف آسان و راحت شروع کنید.,\n۵. زمانی‌که در انجام و برعهده گرفتن مسئولیت‌ها موفق شدید به خودتان امتیاز بدهید. پاداش دهی به خود را دست کم نگیرید. اگر در انجام مسئولیت‌ها شکست خوردید، کارها را رها نکنید و مایوس نشوید. دست از طلب برندارید تا به هدف خود برسید.,\n۶. روابط گذشته خود را بررسی کنید و الگوهای وابستگی تکراری را مشخص سازید. علائم گرفتار شدن در تله زندگی را بنویسید تا به دام آنها نیفتید.,\n۷. از ارتباط با نامزد قوی، مستقل و سخت حمایتگر، خودداری کنید، ولو اینکه این فرد در شما کشش و جذابیت زیادی ایجاد کند.,\n۸. اگر نامزد شما بر اساس مساوات و احترام متقابل با شما رفتار می‌کند و به شما فرصت مسئولیت‌پذیری و نظردهی می‌دهد این فرصت ها را از دست ندهید.,\n۹. اگر همسر یا رئیس و کارمند تان به شما کمک کمک لازم را نمی‌کنند زبان به شکایت باز نکنید. اصرار نورزید که از جانب این افراد راهنمایی بگیرید یا توقع نداشته باشید خیال شما را جمع کنند.,\n۱۰. در حوزه شغلی به تدریج چالش‌ها یا مسئولیت‌های جدیدی بپذیرید، و به تدریج آنها را انجام دهید.,\n۱۱. اگر شما در زمره افراد مستقل‌نما هستید، از نیازتان برای کمک‌خواهی آگاه باشید. از دیگران کمک بگیرید. مسئولیت‌های فراتر از توان را نپذیرید. از اضطراب خود به عنوان علامت استفاده کنید تا بدانید که چقدر باید مسئولیت برعهده بگیرید')
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی آسیب پذیری,\n۱.ریشه‌های تحولی زندگیتان را درک کنید.,\n۲. فهرستی از ترس‌های خود تهیه کنید.,\n۳. موقعیت‌های استرس‌برانگیز را طبق سلسله مراتب، نظم بدهید.,\n۴. افراد صمیمی زندگی‌تان (مثل همسر، فرزند و اعضای خانواده) را ملاقات کنید و از آنها بخواهید که برای برخورد جدی و اساسی با ترس‌هایتان به شما کمک کنند.,\n۵. احتمال وقوع حوادث ترس‌برانگیز را بررسی کنید.,\n۶. برای هر کدام از ترس‌های خود، کارت آموزشی تهیه کنید.,\n۷. با کودک درون حرف بزنید. برای کودک درون، والدی توانمند و شجاع باشید.,\n۸. تمرین‌های آرامش را انجام دهید.,\n۹. با استفاده از تکنیک تصویرسازی ذهنی برعلیه ترس‌ها، موضع بگیرید.,\n۱۰. در زندگی واقعی بر ترس‌هایتان غلبه کنید,\n۱۱. برای هر کدام از این مراحل که با موفقیت پشت سر گذاشتید، به خودتان پاداش بدهید.')
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی نقص/ شرم,\n۱.احساس‌های بی‌ارزشی و شرمساری دوران کودکی را درک کنید. کودک آسیب دیده درون را حس کنید.,\n۲. فهرستی از شیوه‌های مقابله خود (تسلیم فرار و حمله) برای کنار آمدن با تله زندگی را بنویسید.,\n۳. تلاش کنید دست از رفتارهای مقابله‌ای فرار یا حمله بردارید,\n۴. احساس‌های شرم و بی‌ارزشی را زیر نظر بگیرید.,\n۵. معیارهایتان را برای انتخاب نامزد جذاب و نامزد غیرجذاب را بنویسید.,\n۶. نقاط ضعف و نقاط قوت خود را در دوران کودکی و دوران فعلی بنویسید.,\n۷. نقاط ضعف فعلی خود را به طور جدی ارزیابی کنید.,\n۸. برای تغییر نقاط ضعف تغییرپذیر، برنامه ریزی کنید.,\n۹. نامه‌ای به والد (یا والدین) سرزنشگرتان بنویسید.,\n۱۰. کارت آموزشی تهیه کنید.,\n۱۱. تلاش کنید در روابط صمیمی خود صادق‌تر باشید.,\n۱۲. عشق و محبت افراد نزدیک خود را بپذیرید.,\n۱۳. اجازه ندهید دیگران به رفتارهای توهین‌آمیز و نامحترمانه‌شان با شما ادامه دهند.,\n۱۴. اگر در روابط خود به طرف مقابل ایراد می‌گیرید و سرزنش می‌کنید، دست از این کار بردارید')
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی اطاعت,\n۱.ریشه‌های تحولی تله زندگی اطاعت را در دوران کودکی‌تان بشناسید و درک کنید کودک درون مطیع و فرمان بردار خود را بشناسید.,\n۲. موقعیت‌هایی را بشناسید که در محل کار یا در خانه تحت سلطه دیگران قرار می گیرید یا موقعیت‌هایی را بشناسید که نیازهای‌تان را فدای دیگران می‌کنید.,\n۳. در بسیاری از جنبه های زندگی برای خودتان علایق و ایده‌هایی دست و پا کنید (مثل سینما، غذا، تفریح، اوقات فراغت و استفاده از زمان و...) به تدریج با این کار خودتان و نیازهای‌تان را بشناسید.,\n۴. ببینید که چقدر به دیگران کمک می‌کنید و در مقابل، دیگران چقدر به شما کمک می‌کنند. چقدر برای دیگران وقت می‌گذارید و در برابر آنها چقدر برای شما وقت می‌گذارند.,\n۵. رفتا‌رهای منفعلانه_پرخاشگرانه را کنار بگذارید. خودتان را مجبور به رفتارهای جسارتمندانه کنید تا حق‌تان پایمال نشود. ابتدا خواسته‌های کوچک خود را برای دیگران مطرح کنید.,\n۶. از دیگران بخواهید که از شما حمایت و مراقبت کنند. از آنها کمک بگیرید و مشکلات خودتان را با آنها در میان بگذارید. سعی کنید ترازوی دادوستد شما در روابط بین‌فردی تا اندازه‌ای متعادل باشد.,\n۷. با افراد خودخواه و خودمحور که به نیازهای شما پشیزی ارزش قائل نمی‌شوند، قطع رابطه کنید. وقتی احساس کردید در روابط یک‌طرفه و ناسالم گرفتار شده‌اید، رابطه را تغییر بدهید یا از خیر رابطه بگذرید.,\n۸. تمرین کنید به جای موافقت با دیگران، با آنها جسارتمندانه برخورد کنید. به محض این که عصبانی شدید با شیوه ای مناسب خشم خودتان را ابراز کنید. اگر کسی موجب ناراحتی و آزردگی خاطر شما شد، یاد بگیرید که آرامش خودتان را حفظ کنید و سپس دلخوری‌تان را به او بگویید.,\n۹. برای گرایش خودتان به جلب رضایت دیگران، دلیل تراشی نکنید. مدام به خودتان نگویید بلاهایی که از این راه بر سر شما می‌آیند اهمیتی ندارند.,\n۱۰. به بررسی روابط گذشته خود بپردازید. دوستان یا افراد کنترلگر نیازمند را مشخص کنید. در روابط بعدی خود مواظب باشید با چنین افرادی رابطه برقرار نکنید. فهرستی از ویژگی های افراد خودخواه، مغرور، بی‌مسئولیت یا وابسته تهیه کنید که در شما اشتیاق زیادی برای برقراری رابطه ایجاد می‌کنند.,\n۱۱. به رابطه‌ای ارزش قائل شوید که طرف مقابل، نیازهای اصلی شما را ارضا می‌کند، از شما نظر می‌خواهد و به شما مجال می‌دهد که توانایی‌های خودتان را بشناسید.,\n۱۲. در محل‌کار، قاطع‌تر باشید. به کارهای خودتان ارزش قائل شوید. اگر فکر می‌کنید که درخواست پیشرفت و ارتقای شغلی حق شماست، از تقاضای درخواست به سادگی نگذرید. مسئولیت های افراطی را به دیگران واگذار کنید.,\n۱۳. (درباره افراد سرکش و نافرمان صادق است) سعی نکنید در برابر درخواست‌های دیگران به لاک دفاعی بروید. تلاش کنید درخواست های دیگران را درک کنید. خواسته های خودتان را بشناسید. برخی اوقات شما از سر لجبازی با خواسته افراد مافوق خود مخالفت می‌کنید. دست از لجبازی بردارید تا مشکل شما حل شود.,\n۱۴. نتیجه‌گیری‌های خودتان را از این مراحل روی کارت آموزشی بنویسید و آن را همراه خودتان داشته باشید')
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی معیارهای سخت‌گیرانه,\n۱.حوزه‌هایی از زندگی‌تان را مشخص کنید که زیر سیطره معیارهای سختگیرانه یا نامتعادل قرار گرفته‌اند.,\n۲. مزایای تلاش برای رسیدن به این معیارهای سخت‌گیرانه را بنویسید.,\n۳. معایب تلاش برای رسیدن به معیارهای سختگیرانه را بنویسید.,\n۴. تلاش کنید که به تصور خود پروبال بدهید و زندگی رها از این معیارها را تجسم کنید.,\n۵. ریشه های تحولی و دلایل شکل‌گیری تله زندگی‌تان را درک کنید.,\n۶. تصور کنید که اگر توقعات خود را کم کنید چه اتفاقی می‌افتد.,\n۷. میزان زمانی را که صرف حفظ این معیارها می کنید، مشخص سازید.,\n۸. با نظرخواهی از افراد معقول دیدی دقیق‌تر و منطقی‌تر نسبت به این معیارها پیدا کنید.,\n۹. با برنامه‌ریزی تدریجی یا تغییر رفتار، در راستای ارضا نیازهای اصلی‌تر گام بردارید.')
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                        sendMessage(chat_id,'غلبه بر مشکلات تله زندگی استحقاق,\n۱.فهرستی از مزایا و معایب نپذیرفتن محدودیت ها تهیه کنید. این کارها برای انگیزه‌مندسازی شما ضروری است.,\n۲. بهانه تراشی‌های خود را برای نپذیرفتن محدودیت ها کنار بگذارید.,\n۳. دقت کنید که چگونه نپذیرفتن محدودیت‌ها در زندگی روزمره برای شما مشکل درست می‌کند. فهرستی از این مشکلات تهیه کنید.,\n۴. برای این که یادتان باشد که با بی‌انضباطی و استحقاق خود در موقعیت‌ها بجنگید، کارت آموزشی درست کنید.,\n۵. همچنان که به دنبال تغییر هستید از دیگران درباره میزان تغییر خود، نظرخواهی کنید.,\n۶. تلاش کنید با اطرافیان خود، همدلی کنید.,\n۷. اگر تله زندگی شما از نوع حمله برعلیه سایر تله‌هاست سعی کنید طرح های زیربنایی را درک کنید و از تکنیک‌های مربوط به هر کدام از آنها استفاده نمایید.,\n۸. اگر در انضباط شخصی مشکل دارید، کارهای خود را بر اساس میزان ناکام سازی و بیزارسازی، درجه‌بندی کنید. کارهای خود را سلسله‌مراتبی در نظر بگیرید و برای انجام آنها اقدام کنید.,\n۹. اگر در کنترل هیجان‌های خود مشکل دارید از تکنیک "محروم‌سازی" استفاده کنید.,\n۱۰. اگر گرفتار استحقاق از نوع وابستگی شده‌اید، کارهایتان را براساس میزان سختی درجه‌بندی کنید. آنگاه به تدریج کارها را از آسان به سخت و بدون کمک دیگران انجام دهید. از کارهای آسان‌تر شروع کنید تا به خودتان ثابت کنید که آدم با کفایتی هستید.')
                    else:
                        pass
                    sendMessage(chat_id,'آیا تمایل دارید نمودار غلبه بر تله زتدگی خود را ببینید؟\n در صورت تمایل، عبارت "نمودار" را ارسال کنید')
                    sendMessage(chat_id,'در صورت تمایل برای دریافت مشاوره تخصصی می‌توانید با شماره زیر تماس بگیرید:\n09123671593')

                else:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                    else:
                        pass
                    sendMessage(chat_id,'تبریک میگم، با توجه به پاسخ ارسال شده شما در دام این تله گرفتار نشدید')
                write_json(nemodar)
        elif text=='5': 
            javabsoal= read_json()
            nemodar =read_json()
            username = msg['message']['from']['username']
            if len(javabsoal[username])==10:
                javabsoal[username].append('5') #yazdahomin ozv list username
                write_json(javabsoal)
                listemtiaz =[]
                for i in range(1,12):
                    emtiaz = int(javabsoal[username][i])
                    listemtiaz.append(emtiaz)
                jamemtiaz=sum(listemtiaz)
                for key in nemodar.keys():
                    if username not in key:
                        nemodar[username]={}
                    else:
                        pass
                for key in nemodar[username].keys():
                    if 'tale1' not in key:
                        nemodar[username]['tale1']=[]
                    if 'tale2' not in key:
                        nemodar[username]['tale2']=[]
                    if 'tale3' not in key:
                        nemodar[username]['tale3']=[]
                    if 'tale4' not in key:
                        nemodar[username]['tale4']=[]
                    if 'tale5' not in key:
                        nemodar[username]['tale5']=[]
                    if 'tale6' not in key:
                        nemodar[username]['tale6']=[]
                    if 'tale7' not in key:
                        nemodar[username]['tale7']=[]
                    if 'tale8' not in key:
                        nemodar[username]['tale8']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale9']=[]
                    if 'tale9' not in key:
                        nemodar[username]['tale10']=[]
                    else:
                        pass
                if 9<jamemtiaz<20:
                    sendMessage(chat_id,'خیلی پایین، احتمالا این تله زندگی در ذهن شما شکل نگرفته .')
                elif 19<jamemtiaz<30:
                    sendMessage(chat_id,'نسبتا پایین، این تله زندگی ممکن است گاهی اوقات یقه شما را بگیرد')
                elif 29<jamemtiaz<40:
                    sendMessage(chat_id,'متوسط، این تله زندگی باعث مشکلاتی برای شما شده است')
                elif 39<jamemtiaz<50:
                    sendMessage(chat_id,'بالا، بدون شک یکی از تله‌های زندگی شماست')
                else:
                    sendMessage(chat_id,'شدید، این تله زندگی دقیقا یکی از تله‌های اصلی شماست')
                if jamemtiaz>19:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی رهاشدگی,\n۱. رهاشدگی دوران کودکی‌تان را درک کنید.,\n۲. احساس‌های مربوط به رهاشدگی را بازنگری کنید و حساسیت‌های خود را به از دست ‌دادن افراد نزدیک، ترس از تنهایی و نیاز به آویزان شدن و وابستگی بیمارگونه بشناسید.,\n۳. روابط گذشته را بررسی کنید تا الگوهای منجر به عود و بازگشت تله زندگی را بشناسید و فهرستی از خطاهای فکری و رفتاری ناشی از رهاشدگی تهیه کنید.,\n۴. از رابطه با افراد بی‌ثبات، بی‌تعهد و تنوع‌طلب اجتناب کنید، ولو اینکه این افراد برای شما جذابیت و کشش زیادی داشته باشند.,\n۵. وقتی که نامزدی پیدا می‌کنید که متعهد و باثبات است به او اعتماد کنید. باور کنید که او برای همیشه در کنار شما می‌ماند و شما را ترک نمی‌کند.,\n۶. حسادت نکنید، به همسرتان آویزان نشوید و به جدایی‌های معمول زندگی، واکنش افراطی نشان ندهید. ')
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی بی‌اعتمادی و بدرفتاری,\n۱. در صورت امکان از درمانگری صاحبْ‌صلاحیت برای تغییر این تله زندگی کمک بگیرید. مخصوصا اگد سابقه‌ای از بدرفتاری جنسی یا جسمی داشته‌اید.,\n۲. دوستی قابل اعتماد پیدا کنید. تمرین‌های مربوط به تصویرسازی ذهنی را انجام دهید. سعی کنید خاطرات به بدرفتاری را به‌یاد بیاورید و حوادث را با جزئیات کامل بازگو کنید.,\n۳. در حین تصویرسازی ذهنی، خشم خود را بر سر فردی که از شما سوءاستفاده کرده‌ است، خالی کنید. با این کار در تصویر ذهنی بر احساس عجز و بیچارگی خود، غلبه کنید.,\n۴. خودتان را مقصر نپندارید. شما مستحق بدرفتاری و سوءاستفاده شدن نیستید. از فرد بدرفتار، عذرخواهی نکنید.,\n۵. در عین حال که به تغییر این تله زندگی می‌پردازید، به‌تدریج رابطه خو با افراد سوءاستفاده‌گر قطع، کنید.,\n۶. در صورت امکان برای فردی که از شما سوءاستفاده کرده است، پیامدها و اثرات رفتارش بر زندگی فعلی‌تان را بازگو کنید یا برای او در این زمینه، نامه بنویسید.,\n۷. بدرفتاری‌های موجود در رابطه‌های فعلی‌تان را تحمل نکنید.,\n۸. سعی کنید با فردی قابل اعتماد وارد رابطه‌ای صمیمی شوید. به کسی اعتماد کنید که از اعتماد شما سوءاستفاده نمی‌کند,\n۹. سعی کنید با افرادی رابطه برقرار کنید که قصد آسیب زدن به شما را ندارند و به حقوق شما احترام می‌گذارند.,\n۱۰. با نزدیکان خود بدرفتاری نکنید.')
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                        sendMessage(chat_id,' تغییر تله زندگی محرومیت هیجانی,\n۱.محرومیت کودکی‌تان را درک کنید. کودک درون و آسیب‌دیده درون را حس کنید.,\n۲. احساس‌های محرومیت در روابط فعلی‌تان را به دقت زیر نظر بگیرید. نیاز به محبت، همدلی و راهنمایی را به‌خوبی لمس کنید.,\n۳. روابط گذشته خود را به منظور روشن‌سازی الگوی حاکم بر روابط بررسی کنید. موانعی را که باعث عدم تغییر شما می‌شوند، فهرست کنید.,\n.  از رابطه با افراد سرد و بی مهری که شما را به شدت مجذوب خودشان می کنند، دوری کنید.۴,\n. وقتی که فرد مورد علاقه شما از لحاظ هیجانی آدم سالمی است از این فرصت استفاده کنید تا روابط خود را بهبود ببخشید. نیازهای خودتان را بازگو کنید. به طرف مقابل، آسیب پذیری های خود را بگویید,\n۶. از مقصر دانستن نامزدتان و پرتوقعی خود، دست بردارید.') #rahkarha
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی طرد اجتماعی ,\n۱.ریشه‌های تحولی تله زندگی طرد اجتماعی را را در دوران کودکی‌تان درک کنید. احساس حقارت و انزوای کودک درونتان را درک کنید.,\n۲.موقعیت‌هایی را بنویسید که در زندگی روزمره خود دچار احساس آشفتگی و اضطراب می‌شوید.,\n۳. موقعیت‌هایی را بنویسید که از آنها اجتناب می‌کنید.,\n۴. چنانچه در موقعیت‌هایی دچار احساس تنهایی و تفاوت می‌شوید یا جبران افراطی یا حمله متقابل، سعی در پنهان‌سازی این احساس‌ها دارید، سعی کنید این موقعیت ها را بنویسید.,\n۵. مراحل اول تا چهارم را بنویسید سپس ویژگی‌هایی را بنویسید که باعث می‌شوند از دیگران منزوی شوید، احساس حقارت کنید یا آسیب‌پذیری جلوه کنید.,\n۶. اگر واقعا مشکلات و کمبودهایی دارید که واقعی هستند، پس راهکارهایی را برای غلبه بر این مشکلات و کمبودها یا کاهش اثرات آنها پیدا کنید، به تدریج بر این مشکلات غلبه کنید.,\n۷. در اهمیت عیب‌ها و نقص‌هایی که نتوانسته‌اید تغییر بدهید تجدید نظر کنید. منظور این است که دیدگاه خودتان را درباره عیب‌ها و نقص‌های تغییر ناپذیر، عوض کنید.,\n۸. برای هرکدام از عیب‌ها و نقص‌های خود، کارت آموزشی تهیه کنید.,\n۹. از موقعیت‌های کاری و اجتماعی که اجتناب می‌کنید، سلسله‌مراتبی تهیه کنید. سعی کنید به تدریج به این موقعیت‌ها وارد شوید.,\n۱۰. وقتی در جمع به‌سر می‌برید سعی کنید آغازگر مکالمه با دیگران باشید,\n۱۱. سعی‌کنید در گروه‌ها شخصیت اصلی خودتان را بروز دهید و نقش بازی نکنید.,\n۱۲. دست از تلاش برای جبران افراطی حوزه.های نادلپذیر، ناخوشایند و نامحبوب بردارید.')
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی وابستگی,\n۱.ریشه‌های تحولی وابستگی در دوران کودکی‌تان را درک کنید. بی کفایتی و وابستگی کودک درون را تجربه کنید.,\n۲. موقعیت‌ها، وظایف، مسئولیت‌ها و تصمیم‌هایی را بنویسید که در زندگی روزمره برای شما چالش‌آفرین هستند و برای انجام این وظایف، ورود به موقعیت‌ها و پذیرش مسئولیت‌ها و اتخاذ تصمیم‌ها به کمک یا نظر دیگران، وابسته هستند.,\n۳. چالش‌ها تغییرات یا دل‌نگرانی‌هایی را بنویسید که دلیل ترس از آن‌ها اجتناب می‌کنید.,\n۴. به گونه‌ای نظام‌مند، خودتان را مجبور کنید که وظایف روزمره را بدون کمک دیگران انجام بدهید و تصمیم‌ها را بدون کمک‌طلبی اتخاذ کنید. چالش‌هایی را که از آنها اجتناب می‌کنید، برعهده بگیرید. در ابتدا از وظایف و تکالیف آسان و راحت شروع کنید.,\n۵. زمانی‌که در انجام و برعهده گرفتن مسئولیت‌ها موفق شدید به خودتان امتیاز بدهید. پاداش دهی به خود را دست کم نگیرید. اگر در انجام مسئولیت‌ها شکست خوردید، کارها را رها نکنید و مایوس نشوید. دست از طلب برندارید تا به هدف خود برسید.,\n۶. روابط گذشته خود را بررسی کنید و الگوهای وابستگی تکراری را مشخص سازید. علائم گرفتار شدن در تله زندگی را بنویسید تا به دام آنها نیفتید.,\n۷. از ارتباط با نامزد قوی، مستقل و سخت حمایتگر، خودداری کنید، ولو اینکه این فرد در شما کشش و جذابیت زیادی ایجاد کند.,\n۸. اگر نامزد شما بر اساس مساوات و احترام متقابل با شما رفتار می‌کند و به شما فرصت مسئولیت‌پذیری و نظردهی می‌دهد این فرصت ها را از دست ندهید.,\n۹. اگر همسر یا رئیس و کارمند تان به شما کمک کمک لازم را نمی‌کنند زبان به شکایت باز نکنید. اصرار نورزید که از جانب این افراد راهنمایی بگیرید یا توقع نداشته باشید خیال شما را جمع کنند.,\n۱۰. در حوزه شغلی به تدریج چالش‌ها یا مسئولیت‌های جدیدی بپذیرید، و به تدریج آنها را انجام دهید.,\n۱۱. اگر شما در زمره افراد مستقل‌نما هستید، از نیازتان برای کمک‌خواهی آگاه باشید. از دیگران کمک بگیرید. مسئولیت‌های فراتر از توان را نپذیرید. از اضطراب خود به عنوان علامت استفاده کنید تا بدانید که چقدر باید مسئولیت برعهده بگیرید')
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی آسیب پذیری,\n۱.ریشه‌های تحولی زندگیتان را درک کنید.,\n۲. فهرستی از ترس‌های خود تهیه کنید.,\n۳. موقعیت‌های استرس‌برانگیز را طبق سلسله مراتب، نظم بدهید.,\n۴. افراد صمیمی زندگی‌تان (مثل همسر، فرزند و اعضای خانواده) را ملاقات کنید و از آنها بخواهید که برای برخورد جدی و اساسی با ترس‌هایتان به شما کمک کنند.,\n۵. احتمال وقوع حوادث ترس‌برانگیز را بررسی کنید.,\n۶. برای هر کدام از ترس‌های خود، کارت آموزشی تهیه کنید.,\n۷. با کودک درون حرف بزنید. برای کودک درون، والدی توانمند و شجاع باشید.,\n۸. تمرین‌های آرامش را انجام دهید.,\n۹. با استفاده از تکنیک تصویرسازی ذهنی برعلیه ترس‌ها، موضع بگیرید.,\n۱۰. در زندگی واقعی بر ترس‌هایتان غلبه کنید,\n۱۱. برای هر کدام از این مراحل که با موفقیت پشت سر گذاشتید، به خودتان پاداش بدهید.')
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی نقص/ شرم,\n۱.احساس‌های بی‌ارزشی و شرمساری دوران کودکی را درک کنید. کودک آسیب دیده درون را حس کنید.,\n۲. فهرستی از شیوه‌های مقابله خود (تسلیم فرار و حمله) برای کنار آمدن با تله زندگی را بنویسید.,\n۳. تلاش کنید دست از رفتارهای مقابله‌ای فرار یا حمله بردارید,\n۴. احساس‌های شرم و بی‌ارزشی را زیر نظر بگیرید.,\n۵. معیارهایتان را برای انتخاب نامزد جذاب و نامزد غیرجذاب را بنویسید.,\n۶. نقاط ضعف و نقاط قوت خود را در دوران کودکی و دوران فعلی بنویسید.,\n۷. نقاط ضعف فعلی خود را به طور جدی ارزیابی کنید.,\n۸. برای تغییر نقاط ضعف تغییرپذیر، برنامه ریزی کنید.,\n۹. نامه‌ای به والد (یا والدین) سرزنشگرتان بنویسید.,\n۱۰. کارت آموزشی تهیه کنید.,\n۱۱. تلاش کنید در روابط صمیمی خود صادق‌تر باشید.,\n۱۲. عشق و محبت افراد نزدیک خود را بپذیرید.,\n۱۳. اجازه ندهید دیگران به رفتارهای توهین‌آمیز و نامحترمانه‌شان با شما ادامه دهند.,\n۱۴. اگر در روابط خود به طرف مقابل ایراد می‌گیرید و سرزنش می‌کنید، دست از این کار بردارید')
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی اطاعت,\n۱.ریشه‌های تحولی تله زندگی اطاعت را در دوران کودکی‌تان بشناسید و درک کنید کودک درون مطیع و فرمان بردار خود را بشناسید.,\n۲. موقعیت‌هایی را بشناسید که در محل کار یا در خانه تحت سلطه دیگران قرار می گیرید یا موقعیت‌هایی را بشناسید که نیازهای‌تان را فدای دیگران می‌کنید.,\n۳. در بسیاری از جنبه های زندگی برای خودتان علایق و ایده‌هایی دست و پا کنید (مثل سینما، غذا، تفریح، اوقات فراغت و استفاده از زمان و...) به تدریج با این کار خودتان و نیازهای‌تان را بشناسید.,\n۴. ببینید که چقدر به دیگران کمک می‌کنید و در مقابل، دیگران چقدر به شما کمک می‌کنند. چقدر برای دیگران وقت می‌گذارید و در برابر آنها چقدر برای شما وقت می‌گذارند.,\n۵. رفتا‌رهای منفعلانه_پرخاشگرانه را کنار بگذارید. خودتان را مجبور به رفتارهای جسارتمندانه کنید تا حق‌تان پایمال نشود. ابتدا خواسته‌های کوچک خود را برای دیگران مطرح کنید.,\n۶. از دیگران بخواهید که از شما حمایت و مراقبت کنند. از آنها کمک بگیرید و مشکلات خودتان را با آنها در میان بگذارید. سعی کنید ترازوی دادوستد شما در روابط بین‌فردی تا اندازه‌ای متعادل باشد.,\n۷. با افراد خودخواه و خودمحور که به نیازهای شما پشیزی ارزش قائل نمی‌شوند، قطع رابطه کنید. وقتی احساس کردید در روابط یک‌طرفه و ناسالم گرفتار شده‌اید، رابطه را تغییر بدهید یا از خیر رابطه بگذرید.,\n۸. تمرین کنید به جای موافقت با دیگران، با آنها جسارتمندانه برخورد کنید. به محض این که عصبانی شدید با شیوه ای مناسب خشم خودتان را ابراز کنید. اگر کسی موجب ناراحتی و آزردگی خاطر شما شد، یاد بگیرید که آرامش خودتان را حفظ کنید و سپس دلخوری‌تان را به او بگویید.,\n۹. برای گرایش خودتان به جلب رضایت دیگران، دلیل تراشی نکنید. مدام به خودتان نگویید بلاهایی که از این راه بر سر شما می‌آیند اهمیتی ندارند.,\n۱۰. به بررسی روابط گذشته خود بپردازید. دوستان یا افراد کنترلگر نیازمند را مشخص کنید. در روابط بعدی خود مواظب باشید با چنین افرادی رابطه برقرار نکنید. فهرستی از ویژگی های افراد خودخواه، مغرور، بی‌مسئولیت یا وابسته تهیه کنید که در شما اشتیاق زیادی برای برقراری رابطه ایجاد می‌کنند.,\n۱۱. به رابطه‌ای ارزش قائل شوید که طرف مقابل، نیازهای اصلی شما را ارضا می‌کند، از شما نظر می‌خواهد و به شما مجال می‌دهد که توانایی‌های خودتان را بشناسید.,\n۱۲. در محل‌کار، قاطع‌تر باشید. به کارهای خودتان ارزش قائل شوید. اگر فکر می‌کنید که درخواست پیشرفت و ارتقای شغلی حق شماست، از تقاضای درخواست به سادگی نگذرید. مسئولیت های افراطی را به دیگران واگذار کنید.,\n۱۳. (درباره افراد سرکش و نافرمان صادق است) سعی نکنید در برابر درخواست‌های دیگران به لاک دفاعی بروید. تلاش کنید درخواست های دیگران را درک کنید. خواسته های خودتان را بشناسید. برخی اوقات شما از سر لجبازی با خواسته افراد مافوق خود مخالفت می‌کنید. دست از لجبازی بردارید تا مشکل شما حل شود.,\n۱۴. نتیجه‌گیری‌های خودتان را از این مراحل روی کارت آموزشی بنویسید و آن را همراه خودتان داشته باشید')
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                        sendMessage(chat_id,'تغییر تله زندگی معیارهای سخت‌گیرانه,\n۱.حوزه‌هایی از زندگی‌تان را مشخص کنید که زیر سیطره معیارهای سختگیرانه یا نامتعادل قرار گرفته‌اند.,\n۲. مزایای تلاش برای رسیدن به این معیارهای سخت‌گیرانه را بنویسید.,\n۳. معایب تلاش برای رسیدن به معیارهای سختگیرانه را بنویسید.,\n۴. تلاش کنید که به تصور خود پروبال بدهید و زندگی رها از این معیارها را تجسم کنید.,\n۵. ریشه های تحولی و دلایل شکل‌گیری تله زندگی‌تان را درک کنید.,\n۶. تصور کنید که اگر توقعات خود را کم کنید چه اتفاقی می‌افتد.,\n۷. میزان زمانی را که صرف حفظ این معیارها می کنید، مشخص سازید.,\n۸. با نظرخواهی از افراد معقول دیدی دقیق‌تر و منطقی‌تر نسبت به این معیارها پیدا کنید.,\n۹. با برنامه‌ریزی تدریجی یا تغییر رفتار، در راستای ارضا نیازهای اصلی‌تر گام بردارید.')
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                        sendMessage(chat_id,'غلبه بر مشکلات تله زندگی استحقاق,\n۱.فهرستی از مزایا و معایب نپذیرفتن محدودیت ها تهیه کنید. این کارها برای انگیزه‌مندسازی شما ضروری است.,\n۲. بهانه تراشی‌های خود را برای نپذیرفتن محدودیت ها کنار بگذارید.,\n۳. دقت کنید که چگونه نپذیرفتن محدودیت‌ها در زندگی روزمره برای شما مشکل درست می‌کند. فهرستی از این مشکلات تهیه کنید.,\n۴. برای این که یادتان باشد که با بی‌انضباطی و استحقاق خود در موقعیت‌ها بجنگید، کارت آموزشی درست کنید.,\n۵. همچنان که به دنبال تغییر هستید از دیگران درباره میزان تغییر خود، نظرخواهی کنید.,\n۶. تلاش کنید با اطرافیان خود، همدلی کنید.,\n۷. اگر تله زندگی شما از نوع حمله برعلیه سایر تله‌هاست سعی کنید طرح های زیربنایی را درک کنید و از تکنیک‌های مربوط به هر کدام از آنها استفاده نمایید.,\n۸. اگر در انضباط شخصی مشکل دارید، کارهای خود را بر اساس میزان ناکام سازی و بیزارسازی، درجه‌بندی کنید. کارهای خود را سلسله‌مراتبی در نظر بگیرید و برای انجام آنها اقدام کنید.,\n۹. اگر در کنترل هیجان‌های خود مشکل دارید از تکنیک "محروم‌سازی" استفاده کنید.,\n۱۰. اگر گرفتار استحقاق از نوع وابستگی شده‌اید، کارهایتان را براساس میزان سختی درجه‌بندی کنید. آنگاه به تدریج کارها را از آسان به سخت و بدون کمک دیگران انجام دهید. از کارهای آسان‌تر شروع کنید تا به خودتان ثابت کنید که آدم با کفایتی هستید.')
                    else:
                        pass
                    sendMessage(chat_id,'آیا تمایل دارید نمودار غلبه بر تله زتدگی خود را ببینید؟\n در صورت تمایل، عبارت "نمودار" را ارسال کنید')
                    sendMessage(chat_id,'در صورت تمایل برای دریافت مشاوره تخصصی می‌توانید با شماره زیر تماس بگیرید:\n09123671593')

                else:
                    if javabsoal[username][0]=='1':
                        nemodar[username]['tale1'].append(jamemtiaz)
                    elif javabsoal[username][0]=='2':
                        nemodar[username]['tale2'].append(jamemtiaz)
                    elif javabsoal[username][0]=='3':
                        nemodar[username]['tale3'].append(jamemtiaz)
                    elif javabsoal[username][0]=='4':
                        nemodar[username]['tale4'].append(jamemtiaz)
                    elif javabsoal[username][0]=='5':
                        nemodar[username]['tale5'].append(jamemtiaz)
                    elif javabsoal[username][0]=='6':
                        nemodar[username]['tale6'].append(jamemtiaz)
                    elif javabsoal[username][0]=='7':
                        nemodar[username]['tale7'].append(jamemtiaz)
                    elif javabsoal[username][0]=='8':
                        nemodar[username]['tale8'].append(jamemtiaz)
                    elif javabsoal[username][0]=='9':  
                        nemodar[username]['tale9'].append(jamemtiaz)
                    elif javabsoal[username][0]=='10':
                        nemodar[username]['tale10'].append(jamemtiaz)
                    else:
                        pass
                    sendMessage(chat_id,'تبریک میگم، با توجه به پاسخ ارسال شده شما در دام این تله گرفتار نشدید')
                write_json(nemodar)
#..............................................................................................................
        elif text=='نمودار':
            javabsoal=read_json()
            nemodar = read_json()
            username = msg['message']['from']['username']
            shomaretale = javabsoal[username][0]
            y = []
            x = []
            for i in range(1,11):
                if i==shomaretale:
                    talei= 'tale'+str(i)
                    for j in nemodar[username][talei]:
                        y.append(j)
                for k in range(1,len(y)+1):
                    x.append(k)
            if len(x)>0 and len(y)>0:
                plt.plot(x, y, marker='*', linestyle='--')
                plt.xlabel('تعداد دفعات شرکت')
                plt.ylabel('امتیاز')
                plt.title('غلبه بر تله‌های زندگی')
                plt.savefig('nemoudar.jpg')
                requests.post(
                url + "sendPhoto",
                {
                    "chat_id": chat_id,
                    "nemoudar.jpg": f"{chat_id}.jpg",
                })
        else:
            javabsoal=read_json()
            javabsoal.clear()
            write_json(javabsoal)
            sendMessage(chat_id,'تست به اتمام رسیده است، خدانگهدار')

        return Response('ok',status=200)
        
            
        
    else:
        return ' '
def write_json(data,filename=''):   #یک دیکشنری رو به صورت فایل روی سرور ذخیره کردم
    with open(filename,'w') as target:
        json.dump(data,target,indent=4,ensure_ascii=False)
def read_json(filename=''):
    with open(filename,'r') as target:
        data=json.load(target)
    return data
write_json({}, 'file.txt')
app.run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))





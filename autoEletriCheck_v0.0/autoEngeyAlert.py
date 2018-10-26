from acessData import getData
from sendMail import mail
import time 

if __name__ =='__main__':
    while True:
        data = getData()
        if data<10.0:
            mail()
        time.sleep(100)

from acessData import getData
from sendMail import sendMail
import urlIO
import time 

if __name__ =='__main__':
    urls_addrs = urlIO.Output()
    while True:
        for url in urls_addrs:
            data = getData(url)
            if data<10.0:
                ret=sendMail(urls_addrs[url])
                if ret:
                    print("邮件发送成功")
                else:
                    print("邮件发送失败")
        time.sleep(100)

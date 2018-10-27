'''
Output 返回一个dict包括电费的url和要发送的mail地址

'''

def Input():
    url = input('Please input new url to add:')
    add = input('Please input new e-mail address to match it:')
    with open('urls&addrs.txt','a') as f:
        f.write(url+' ')
        f.write(add+'\n')
    
def Output():
    urls_addrs={}
    with open('urls&addrs.txt','r') as f:
        while True:
            s=f.readline()
            if s:
                t=s.split(' ')
                urls_addrs[t[0]] = t[1].strip('\n')
            else:
                break
    return urls_addrs




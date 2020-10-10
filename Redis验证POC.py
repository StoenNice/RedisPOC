import redis
import os
while True:
    address = input("Redis Address Input\nIP:")
    try:
        r = redis.Redis(host=address, socket_timeout=5)
        info = r.info()
        for ls in info:
            print(ls, ": ", info[ls])
        input("Enter ReStart")
        os.system("cls")
    except BaseException as err:
        print("ERR", address, err)
        input("Enter ReStart")
        os.system("cls")

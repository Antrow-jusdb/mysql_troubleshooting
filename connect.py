
import pymysql
import yaml
from core_code import *
def connection_all():
    try:
        all_single=["Selected one server enter `1`","All server enter`2`"]
        for i in all_single:
            print(i)
        var = input("Kindly select any number: ")
        if var == "2":
            all_server =[1,2,3]
            for typ in all_server:
                try:
                    with open('cred.yml','r')as file:
                        db = yaml.safe_load(file)
                        hostname= (db[typ]['hostname'])
                        print("Hostname: ",hostname)
                        user= (db[typ]['username'])
                        password= (db[typ]['password'])
                        conn = pymysql.connect(host = hostname,user = user,password = password)
                        cur =conn.cursor()
                        show(cur)
                        uptime(cur)
                        master(cur)
                        slave(cur)
                        top(cur)
                        conn.close()
                except:
                    print("pleace check connection")

                
        elif var == "1":
            with open('cred.yml','r')as file:
                single=["1. user-cawm-replica","2. my local mechine","3. pyxis-replica"]
                for i in single:
                    print(i)
                var = int(input("Kindly select any number(server): "))
                db = yaml.safe_load(file)
                hostname= (db[var]['hostname'])
                print(hostname)
                user= (db[var]['username'])
                password= (db[var]['password'])
                conn = pymysql.connect(host = hostname,user = user,password = password,)
                cur =conn.cursor()
                show(cur)
                uptime(cur)
                master(cur)
                slave(cur)
                top(cur)
                conn.close()
    except Exception as E:
        print(E)

    finally:
        print("clean-up")
    
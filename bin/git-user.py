#!/usr/bin/python3

import os,sys
import yaml

config = """
github:
    user : reharish
    email : rengarajharish@gmail.com
work repo:
     user : Harish
     email : harishbabu.r@zilogic.com
"""


def user_config(conf_file):
    with open(conf_file) as conf:
    users = yaml.load(conf.read(), yaml.SafeLoader)
    return users

def set_config(conf, user):
    os.system("git config user.name {}".format(conf.get(user)["user"]))
    os.system("git config user.email {}".format(conf.get(user)["email"]))
    return True


if __name__ == "__main__":
    try :
        users = user_config("git-users.yml")
        c = 1
        if len(users) >= c:
            for user,value in users.items():
                print("[{}] {}".format(c,user))
                c += 1
            get_user = int(input("Choose : "))-1
            list_user = list(users)
            status = set_config(users, list_user[get_user])
            if status:
                print("Done")
        else:
            print("No user conf found !")
    except Exception as e:
        print("ERR : {}".format(e))
        sys.exit(1)

sys.exit(0)

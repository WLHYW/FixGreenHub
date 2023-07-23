import getpass
import os
import shutil


def error():
    print(ERROR + " ------------------------------------------------")
    print(ERROR + " + 按任意键退出FixGreenHub")
    print(ERROR + " ------------------------------------------------")


def end():
    print(INFO + " ------------------------------------------------")
    print(INFO + " + 已重置GreenHub时间为60分钟，请重新打开GreenHub")
    print(INFO + " + 按任意键退出FixGreenHub")
    print(INFO + " ------------------------------------------------")


def fix(path):
    try:
        shutil.rmtree(path)
        end()
    except OSError as e:
        print(ERROR + "重置GreenHub失败！")
        print(ERROR + " ------------------------------------------------")
        print(ERROR + " + 请检查GreenHub是否关闭")
        print(ERROR + " + 请检查FixGreenHub是否拥有权限")
        print(ERROR + " + 若非以上问题，请联系：2049621985@qq.com")
        print(ERROR + " ------------------------------------------------")
        error()


def check_path():
    path = getpath()
    status = os.path.exists(path)
    if status:
        print(INFO + "获取GreenHub路径成功")
        print(INFO + " ------------------------------------------------")
        print(INFO + " + 路径: "+path)
        print(INFO + " ------------------------------------------------")
        fix(path)
    else:
        print(ERROR + "获取GreenHub路径错误！")
        print(ERROR + " ------------------------------------------------")
        print(ERROR + " + 请检查GreenHub是否安装在默认路径")
        print(ERROR + " + 暂不支持自定义路径")
        print(ERROR + " + 若非以上问题，请联系：2049621985@qq.com")
        print(ERROR + " ------------------------------------------------")
        error()


def getpath():
    user = getpass.getuser()
    path = f'C:\\Users\\{user}\\AppData\\Roaming\\GreenHub'
    return path


if __name__ == '__main__':
    Introduce = "___________          _________                       ______  __      ______\n___  ____/__(_)___  ___  ____/__________________________  / / /___  ____  /_ \n__  /_   _/  /__  |/_/  / __ __  ___/  _ \  _ \_  __ \_  /_/ /_  / / /_  __ \ \n_  __/   _/ / __>  < / /_/ / _  /   /  __/  __/  / / /  __  / / /_/ /_  /_/ / \n/_/      /_/  /_/|_| \____/  /_/    \___/\___//_/ /_//_/ /_/  \__,_/ /_.___/ \n + ©2023 WLHYW. All rights reserved. \n + Version beta 1.0.0 \n"
    INFO = "[\033[92mINFO\033[0m]"
    ERROR = "[\033[91mERROR\033[0m]"
    print(Introduce)
    check_path()
    input()

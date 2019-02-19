# file : main.py
# 学生管理系统主模块

from menu import show_menu
from student_info import *

def main():
    infos=[] #用于保存学生信息的列表
    while True:
        # 打印菜单
        show_menu()
        s=input('请选择：')
        if s=='1':
            infos+=input_student()
        elif s=='2':
            print_student(infos)
        elif s=='3':
            remove_student(infos)
        elif s=='4':
            modify_score(infos)
        elif s=='5':
            print_score_desc(infos)
        elif s=='6':
            print_score_asc(infos)
        elif s=='7':
            print_age_desc(infos)
        elif s=='8':
            print_age_asc(infos)
        elif s=='9':
            infos=read_from_file()
        elif s=='10':
            save_to_file(infos)
        elif s=='q':
            break
main()

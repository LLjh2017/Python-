# file:student_info
def input_student():
    L=[] #创建一个列表用来保存学生信息的字典
    #循环输入学生姓名，年龄，成绩，姓名为空时结束输入
    while True:
        n=input('请输入学生姓名:')
        if not n: #姓名为空时结束输入
            break
        # 让用户输入年龄，如果错误就重新输入
        # 如果没有错，则跳出循环，做后面的事
        while True:
            try:
                a=int(input('请输入年龄：'))
            except:
                print("您的输入有误，请重新输入")
                continue
            else:
                break
        try:
            s=int(input('请输入成绩：'))
        except:
            print("您的输入有误，请重新输入")
            continue
        # 得到的数据形成字典
        d={}
        d['name']=n
        d['age']=a
        d['score']=s
        #加到列表内
        L.append(d)
    return L

def print_student(L):
    print("+---------------+-----------+----------+")
    print("|     name      |    age    |  score   |")
    print("+---------------+-----------+----------+")
    for d in L:
        line = '|' + d['name'].center(15)
        line += '|' + str(d['age']).center(11)
        line += '|' + str(d['score']).center(10)
        line += '|'
        print(line)
    print("+---------------+-----------+----------+")
     
def remove_student(L):
    n=input('请输入要删除学生的姓名：')
    for i in range(len(L)):
        if L[i]['name']==n:
            del L[i]
            break
            print('您输入的姓名有误')
    
def modify_score(L):
    n = input("请输入学生的姓名:")
    s =int(input("请输入学生的成绩:"))
    for i in range(len(L)):
        if L[i]['name']==n:
            L[i]['score']=s
            break
            print('您输入的姓名有误')

def print_score_desc(L):
    def get_score(d):
        return d['score']
    lst=sorted(L,key=get_score,reverse=True)
    print_student(lst)


def print_score_asc(L):
    def get_score(d):
        return d['score']
    lst=sorted(L,key=get_score)
    lst=sorted(L,key=lambda d:d['score'])

    print_student(lst)
def print_age_desc(L):
    def get_age(d):
        return d['age']
    lst=sorted(L,key=get_age,reverse=True)
    print_student(lst)
def print_age_asc(L):
    def get_age(d):
        return d['age']
    lst=sorted(L,key=get_age)
    print_student(lst)
def read_from_file():
    L=[]
    try:
        f=open('si.txt','r')
        for line in f:
            line=line.strip() # 去掉\n
            items=line.split(',')
            n,a,s=items
            a=int(a)
            s=int(s)
            L.append(dict(name=n,age=a,score=s))
        f.close()
    except OSError:
        print('打开文件失败')
    return L
def save_to_file(L):
    try:
        f=open('si.txt','w')
        for d in L:
            f.write(d['name'])
            f.write(',')
            f.write(str(d['age']))
            f.write(',')
            f.write(str(d['score']))
            f.write('\n')
        f.close()
        print('保存成功')
    except OSError:
        print('保存文件失败')























"""
用户视图层接口
"""
from core import admin
from core import student

fun_dict = {
    "1": admin.admin_view,
    "2": student.student_view,
}

def run():
    while True:
        print(
            '''
          =====选课系统======  
            1.管理员功能
            2.学生功能
            '''
        )
        choice = input("请输入功能:")
        # 判断一下输入
        if choice not in fun_dict:
            print("输入有误,请重新输入")
            continue
            
        fun_dict[choice]()
        
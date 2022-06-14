stature=input('请输入你的身高(单位米):')
stature=float(stature)
weight=input('请输入你的体重(单位公斤):')
weight=float(weight)
age=input('请输入你的年龄:')
age=int(age)
if age<10:
    print('10岁以下儿童不参与健康评估')
elif age <60:
    BMI=weight/(stature**2)
    if BMI >24:
        print('用户体重超重')
    elif BMI<18:
        print('用户体重超轻')
    else:
        print('体重正常')
else: 
    print('60岁以上老人不参与健康评估')
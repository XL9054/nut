temperature = input('请输入今天的气温（单位 摄氏度）:')
temperature =int(temperature)
airpressure =input('请输入今天气压（单位 帕）:')
airpressure =int(airpressure)
if temperature >30 or temperature <-8 :
    print('不舒适')
elif airpressure >300 or airpressure <20 :
    print('不舒适')
elif 25< temperature<=30 and 200<airpressure<=300:
    print('比较舒适')
elif 10< temperature <=25 and 100<airpressure<=200:
    print('特别舒适')
elif -8< temperature <=10 and 20<airpressure<=100:
    print('比较舒适')
else:
    print('本程序不能判断')
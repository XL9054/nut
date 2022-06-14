sex=input('请输入您的性别：')
sex=sex.replace(' ','')
height=input('请输入您的身高（厘米）')
height=height.replace(' ','')
height=height.replace('厘米','')
height=int(height)
weight=input('请输入您的体重（公斤）')
weight=weight.replace(' ','')
weight=weight.replace('公斤','')
weight=int(weight)
if sex =='男':
    standard=(height-100)*0.9
else:
    standard=(height-100)*0.9-2.5
if standard-5<weight<standard+5:
    print('体重标准')
elif standard< weight:
    print('体重太重')
else:
    print('体重太轻')
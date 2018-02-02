
import json
import requests
"""根据起点和终点，返回路线规划的距离和行驶时间"""


#设置出行方式
trip_mode = 'driving'

#判断出行方式，获取相应接口地址
if trip_mode == 'driving':
	url = 'http://api.map.baidu.com/routematrix/v2/driving?'
elif trip_mode == 'riding':
	url = 'http://api.map.baidu.com/routematrix/v2/riding?'
elif trip_mode == 'walking':
	url = 'http://api.map.baidu.com/routematrix/v2/walking?'

#生成两个空列表存储出发、到达坐标
origins = []
destinations = []

#逐行读取文件，方法strip()去除换行符，添加到list
for origin in open("E:/baidumap/origins.txt"):
	origins.append(origin.strip())	
for destination in  open("E:/baidumap/destinations.txt"):
	destinations.append(destination.strip())
print(origins)
#计算坐标list长度，for循环提取出发、到达坐标
for i in range(len(origins)):
	
	#引入try except处理KeyError
	try:
		required_parameter = {
			'origins':origins[i], 
			'destinations':destinations[i], 
			'output':'json',
			'tactics':'11',
			'ak':'G4rOuo6mHVvNtSU7PpRLTsWdz51oT4ho',
			}
		#request模块，方法get()获取参数
		r = requests.get(url,required_parameter)
		#json解析
		r_js = r.json()
		#提取距离、时间、速度
		dis = r_js['result'][0]['distance']['value']/1000
		time = r_js['result'][0]['duration']['value']/60
		speed = round(dis/time*60)
	except KeyError:
		print("距离太远，检查坐标或出行方式！")
	else:
		print('总行程距离为：'+str(dis)+'千米，总时间为：'
			+str(time)+'分钟',"速度为： " + str(speed) + "千米/小时")
		
		#结果写入文件
		with open("result.txt","a") as result:
			result.write('{},{},{}\n'.format(dis,time,speed))

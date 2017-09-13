import requests
'''
	I only tried for a particular range
	It maybe altered to experiment if user exists in it
	For different colleges, range may differ too
'''
R_LOW = 80 #Lower limit for search
R_HIGH = 1200 #Upper limit for search
URL = ['https://scemod.vit.ac.in/pluginfile.php/','/user/icon/boost/f3'] #Change it according to college
for i in range(R_LOW, R_HIGH):       
	print('Trying for id', i) #Visuals
	'''
		Url works for VIT Vellore, Chennai
		Other colleges can be given a shot too 
	'''
	url = URL[0]+str(i)+URL[1] 
	filename = str(i)+'.jpg' 
	try:
		resp = requests.get(url, verify=False) 
		data = resp.content
		'''
			not.jpg is a reference file which is returned if the user doesn't have a photo
			if user doesn't exists, a html document is returned 
			while downloading, we keep a check that it's not not.jpg or html file
		'''
		with open('not.jpg', 'rb') as fnot:
			if b'html' not in data and data != fnot.read():
				with open(filename, 'wb') as f:	
					f.write(data)
	except Exception as e:
		print(e)

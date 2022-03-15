def sopi(lim):
	if lim == 1:
		return 1
	else:
		return lim + sopi(lim-1)

def reccounting(lim):
	if lim > 0:
		print(lim)
		reccounting(lim-1)
	else:
		return 0;	

print(reccounting(10))
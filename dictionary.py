def freq_k(string,k):
	s=string.split()
	d={}
	for w in s:
		if w in d:
			d[w]=d[w]+1
		else:
			d[w]=1
	for i in d:
		if d[i]==k:
			print(i)
#string='my name is Jatin Malhotra and my favourite anime is DBZ'
#freq_k(string,1)

def max_freq(string):
	s=string.split()
	d={}
	for w in s:
		if w in d:
			d[w]=d[w]+1
		else:
			d[w]=1
	maxV=max(d.values())
	#print(maxV)
	for i in d:
		if d[i]==maxV:
			print(i)
			break

def duplicate(string):
	d={}
	ans=''
	s=string
	for x in s:
		if x not in ans:
			ans=ans+x
		#print(ans)
#			d[x]=None
	return (ans)

def longestSeries(lst):
	Minn=min(lst)
	Maxx=max(lst)
	d={}
	for w in lst:
		if w and (w+1) in d:
			d[w]=d[w]+1
		else:
			d[w]=1
	maxV=max(d.values())
	print(maxV)

lst=[1,2,3,4,11,12,13]
print(longestSeries(lst))

















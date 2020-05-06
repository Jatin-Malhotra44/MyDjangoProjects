def is_bala(string):
	s=[]
	for x in string:
		if x in '({[':
			s.append(x)
		elif x ==')':
			if(not s or  s[-1]!='('):
				return False
			s.pop()
		elif x =='}':
			if(not s or s[-1]!='{'):
				return False
			s.pop()
		elif x ==']':
			if(not s or s[-1]!='['):
				return False
			s.pop()
	if(not s):
		return True
string=input()
ans=is_bala(string)
print(ans)
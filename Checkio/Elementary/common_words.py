first="hello,World,ball"
second="hello,earth,ball"
s1=set(first.split(','))
s2=set(second.split(','))
s3=sorted(list(s1 & s2))
str=','.join(str(e) for e in s3)
print str
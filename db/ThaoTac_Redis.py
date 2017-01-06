import redis

print(redis.__file__)
print(dir(redis))

re = redis.StrictRedis(host='localhost', port=6379, db=0)
re.set('foo', "thanhnm")

print('************')
print(re.get('foo'))
print(type(re.get('foo')))
print(re.get('foo123'))

#pipeline : tăng	performance	bởi	gộp	nhiều	lệnh	vào	một 	request 	thay
#vì	mỗi	lệnh	là	một 	request 	như	thông	thường
print('PIPELINE')
pipe = re.pipeline()
pipe.set('a', 'chu a')
pipe.set('b', 'chu b')
pipe.get('a')
res = pipe.execute()
print(res)
print(type(res))
print(re.get('a'))
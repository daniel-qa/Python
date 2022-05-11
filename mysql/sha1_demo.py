import hashlib
data = 't1'
sha1 = hashlib.sha1(data.encode('utf-8')).hexdigest()
print(sha1)

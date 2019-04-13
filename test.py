import csv
a=0
b=5000
path="test.csv"
with open(path, 'wb') as f:
	while a<b:
		a=a+1
		i="hello"
		print(i)
		csvwriter=csv.writer(f)
		csvwriter.writerows(i)
		f.flush()
f.close()
import sqlite3
#create a machine that will be able to ask his origines

#concepts
#first phase is learning.
''' Learning is to be seen as an association of knowlegde object associate by pathways.
 It is not important to have a fast path way it is way more usefull to have a consistant one '''
#thinkering one

#abstract declaration
#create a new data type with three composent: id,value1, value2. they will be all numerical and store in a data base that can point to nearly whatever

class kindle:
	kindleId = 0
	def __init__(self, object1, object2):
		self.object1 = object1
		self.object2 = object2
		kindle.kindleId += 1
	def checker(self):
		print "number of kindle happen so far: %d" %kindle.kindleId
		print "object1 ::", self.object1, ",object2 ::", self.object2

time1 = kindle(222,924)
time1.checker()
#we want to save our data so we don't have to worry  about it no more.
conn=sqlite3.connect('database.db')
c= conn.cursor()

c.execute('''CREATE TABLE memory
			(id, obect1,object2,)''')
c.execute(" INSERT INSERT INTO memory(time1.kindleId,time1.object1,time1.object2)")


conn.commit()

conn.close()

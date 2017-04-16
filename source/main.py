#-*- coding: utf-8 -*-
import sqlite3 as lite
import sys

#create a machine that will be able to question it's origines, follow https://medium.com/@tonytam874/maths-and-the-rest-of-us-7f65c9e04fa2 to learn more about the driven theory

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
	#checker
	def checker(self):
		print "number of kindle happen so far: %d" %kindle.kindleId
		print "object1 ::", self.object1, ",object2 ::", self.object2
	

time1 = kindle(222,924)
time1.checker()


#we want to save our data so we don't have to worry  about it no more.
con = lite.connect('../bin/test.db')

with con:

	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Abstracts(Id INT, Object1 INT, Object2 INT)")
	cur.execute("INSERT INTO Abstracts VALUES(?,?,?)",(time1.kindleId,time1.object1,time1.object2))

	
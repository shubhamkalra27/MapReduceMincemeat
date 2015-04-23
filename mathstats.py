#!/usr/bin/env python
import mincemeat, sys, fileinput


# Don't forget to start a client!
# ./mincemeat.py -l -p changeme
# s
# data = fileinput.input()
dataraw = fileinput.input()
#sys.exit(0)

temp = ''
counter = 0
datasource = {}
for line in dataraw:
  temp = temp +  line.rstrip() + ' '  
  # print cousnter
  if counter % 30 == 0:    
    datasource[counter] = temp
    temp = ''
  counter += 1
if temp!= '':
    datasource[counter] = temp
# print counter

def mapfn(k, v):
    for k in v.split():
      yield "count", int(k)
      yield "square", int(k)*int(k)

def reducefn(k, vs):
    a = []
    a.append(("count",len(vs)))
    a.append(("sum",sum(vs)))
    # a.append(("mean",float(sum(vs))/len(vs) ))
    return a

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

# print results
count = results ['count'][0][1]
addition = results['count'][1][1]
mean = addition /float(count)
variance = results['square'][1][1]/float(count) -(results['count'][1][1]/float(count))**2

SD = (variance)**(0.5)

print "count = " + str(count)
print "sum = " + str(addition)
print "variance = " + str(SD) 



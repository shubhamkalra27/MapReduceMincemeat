#!/usr/bin/env python
import mincemeat
import sys, fileinput

# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

#file = open('mobydick.txt','r')
#dataraw = list(file)
#file.close()
dataraw = fileinput.input()

temp = ''
counter = 0
datasource = {}
for line in dataraw:
  temp = temp +  line.rstrip() + ' '
  if counter % 30 == 0:
    datasource[counter] = temp
    temp = ''
  counter += 1
datasource[counter] = temp
 

def mapfn(k, v):
    for w in list(v.lower()):
      yield w, 1
      yield "total", 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

total = results["total"]
print total
results.pop("total", None)
resultlist = []

for k in results.keys():
  print ((100*results[k])/3398)
  resultlist.append((k,round(100*results[k]/float(total),2),results[k]))
  
resultlist = sorted(resultlist, key=lambda a: a[2])

#print resultlist

for disp in resultlist:
    print str(disp[0]) + "  " +  str(disp[1]) + " %   " +  str(disp[2])




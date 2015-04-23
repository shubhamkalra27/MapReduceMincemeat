# import

import mincemeat, sys, md5, md5, hashlib

#input is saved in the variable
hashToCheck = sys.argv[1]
print "Attacking " + str(hashToCheck) + " ..."


#custom function to generate data 
def customEnumerate(length, possibles):
  ret = []
  if length == 1:
    return list(possibles)
  else:
    subs = customEnumerate(length -1, possibles)
    #ret = ret + subs
    for ch in possibles:
      for sub in subs:
        ret.append(str(ch) + str(sub))
  return ret

allowed = "abcdefghijklmnopqrstuvwxyz0123456789"

allPossibleKeys = ''

for x in range(1, 5):
    allPossibleKeys += str(customEnumerate(x,allowed))

#data is stored in allPossibleKeys


# print allPossibleKeys
temp = []
temp.append(hashToCheck)
data =[]
counter = 1
for word in allPossibleKeys:
  temp.append(word.rstrip())
  if counter % 4444 == 0:
    data.append(temp)
    temp = []
    temp.append(hashToCheck)	
  counter += 1
if temp != []:
   data.append(temp)

datasource = dict(enumerate(data))

def mapfn(k, v):
    import md5, hashlib
    for value in v:
    	#see the server logs for the current hash check. 
    	print (hashlib.md5(value).hexdigest()[:5])
        if (v[0]) == (hashlib.md5(str(value)).hexdigest()[:5]):
          # print value
          print "yayee"
          yield value, 1

def reducefn(k, vs):
    return list(set(vs))
    #remove redudant values 

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print results

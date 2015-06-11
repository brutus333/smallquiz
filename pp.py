from math import sqrt
from math import ceil
def calc(xstart,ystart,len,total,lista):
   if len==0:
      return
   x=xstart
   y=ystart
   def put(a,b):
     lista.append(int(a+total*b))
     #print "%d,%d" % (a,b)
   for x in range(xstart,len):
     put(x,ystart)
   for y in range(ystart+1,len):
     put(x,y)
   for x in reversed(range(xstart,x)):
     put(x,y)
   for y in reversed(range(ystart+1,len-1)):
     put(x,y)
   calc(x+1,y,len-1,total,lista)
indexlist=[]
string="Averylongstringfortestingtheboxstringproblemwithouthassleandworries"
stringlen=int(ceil(sqrt(len(string))))
if len(string)!=stringlen^2:
  paddedstring=string+" "*(stringlen**2-len(string))
print "%s#" % paddedstring
calc(0,0,stringlen,stringlen,indexlist)
reversedindex=[ indexlist.index(x) for x in range(len(indexlist)) ]
changedstring=[ paddedstring[x] for x in reversedindex ]
newstring=[ changedstring[x-stringlen:x] for x in range(stringlen,stringlen*stringlen+1,stringlen) ]
print newstring
print "\n".join([ " ".join(x) for x in newstring ])


from functools import reduce

list_1 =['let', 'us', 'go']

sentence = reduce(lambda x,y: x+' '+y,list_1)


# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:07:58 2016

@author: Rush
"""


#class generate_subsets(set):
#    def subsets(self):
#        s1 = []
#        s2 = list(self)
#
#        def recfunc(i=0):            
#            if i == len(s2):
#                yield frozenset(s1)
#            else:                
#                yield from recfunc(i + 1)
#                s1.append(s2[ i ])
#                yield from recfunc(i + 1)
#                s1.pop()
#
#        yield from recfunc()
#
#if __name__=='__main__':
#    generate_subsets({})
#    

from itertools import combinations
s={1,2,3,5}
subs = [set(j) for i in range(len(s)) for j in combinations(s, i+1)]
print subs
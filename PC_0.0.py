# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 20:06:02 2016

@author: Rush
"""

import json
import ijson
d=''
with open('E:\\UITest\\UITest\\fliondeso.json', "r") as json_data:
#    d = json.load(json_data)
    objects = ijson.items(json_data, 'Fliondeso.Transportation.Bus')
    columns = list(objects)
    
#    if 'Transportation' in columns[0]:
#        objects1 = ijson.items(json_data, 'Fliondeso.Transportation')
#        columns = list(objects1)
        
    
print columns[0]
#print len(columns[0])
#print ['Transportation'][0]
#print d['Fliondeso']['Transportation']['Bus'][0]
#print len(d['Fliondeso'])
#print d[0]
#https://www.dataquest.io/blog/python-json-tutorial/


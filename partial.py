import requests
import json


AUTH = ('annoop', 'kuva8')
CATALOG = 'ibeam-catalog'
REPO = 'timecard'
BASE_URL = 'http://agraph.semanticarts.com/catalogs/%s/repositories/%s' % (CATALOG, REPO)

def query(query):
    payload = {'query': query}
    headers = {"Accept": "application/json"}
    r = requests.get(BASE_URL, auth=AUTH, headers=headers, params=payload)
    #print r.text
    return json.loads(r.text)


new_Query ="""Select ?empName  ?week (CONCAT(STR(?empName), "-",STR(?week) )AS ?label )  ?selWeek 
       ?t ?task ?project ?projectN ?woPercent ?hours ?amount ?earnedRev ?s ?sponsor ?tc ?location 
       ?diary
       ?startDateTime ?endDateTime ?postDateTime 
       
       
        WHERE {?tc rdf:type sa:TimeCharge . ?tc sa:consumptionOf ?p . ?p gist:hasA ?br .  
            ?p gist:name ?empName . 
            ?br gist:decimalValue ?rate .
            ?tc gist:hasMagnitude ?m . ?m gist:decimalValue ?hours .
            ?tc gist:directPartOf ?ww . ?ww rdf:type sa:WorkWeek . 
            ?ww gist:sequence ?week . 
            ?tc sa:consumedToward ?t . ?t rdfs:label ?task .
            ?tc gist:occurredAt ?l . ?l rdfs:label ?location .
            ?t gist:directPartOf ?project . ?project rdfs:label ?projectN .
            ?project sa:hasSponsor ?s . ?s gist:name ?sponsor . 
            ?project gist:categorizedBy ?cat . ?cat rdf:type sa:ChargeabilityType . 
            ?project gist:hasMagnitude ?wo . ?wo rdf:type sa:WriteOff .
             ?wo gist:decimalValue ?woPercent .
            ?tc gist:actualEnd ?e . ?e gist:universalDateTime ?endDateTime . 
            ?tc gist:actualStart ?startTime . ?startTime gist:universalDateTime ?startDateTime . 
            ?tc gist:recordedOn ?r . ?r gist:universalDateTime ?postDateTime . 
            BIND((1-?woPercent) AS ?realizedPercent) . 
            OPTIONAL {?tc gist:describedIn ?c . ?c gist:containedText ?diary .}
            BIND (?rate * ?hours AS ?amount)
            BIND ((?amount * ?realizedPercent) AS ?earnedRev )
            BIND(?week AS ?selWeek)
            FILTER (?cat NOT IN (sa:_Unpaid))
      }
 """
result = query(new_Query)
for k,v in result.iteritems():
    print k


new_list = []

for i in range(2000):
    new_list.append(result["values"][i])
# print new_list[0]
# print new_list[0]
ind = new_list[0].index('"create agenda and brainstorm things we might to in training business."^^<http://www.w3.org/2001/XMLSchema#string>')
# print ind

array = []
for i in range(len(new_list)):
    array.append(new_list[i][16]) 
# print array
print len(array)

newArray = []
for i in range(len(array)):
    newArray.append(array[i][1:-44])
print newArray[0]

mango = []
for i in range(len(newArray)):
    mango += newArray[i].split(" ")
print mango

final_at = []
final_hash = []
final_dollar = []
for word in mango:
    if len(word) > 0:
        if word[0] == "@":
            final_at.append(word)
        if word[0] == "$":
            final_dollar.append(word)
        if word[0] == "#":
            final_hash.append(word)


print "final_at", list(set(final_at))
print "final_hash", list(set(final_hash))
print "final_dollar", list(set(final_dollar))


# k = []
# for j in range(len(newArray)):
#     print newArray[j]
#     k = newArray[j](" ")
#     for u in k:
#         m = u.startswith("@")
#         l = u.startswith("#")
#         n = u.startswith("$")
#         for v in range(len(final_dollar)):
#             if(final_dollar[v] != n):
#                 final_dollar.append(n)
#             if v in range(len(final_hash)):
#                 final_hash.append(l)
#             if v in range(len(final_at)):
#                 final_at.append(m)



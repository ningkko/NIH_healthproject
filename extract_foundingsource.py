import re
import collections


with open('data.txt', 'r') as file:

    funding_sources = []
    # read through evey line to find ones containing sources
    for line in file:
        if "SourceAwardList" in line:
            for result in re.findall(r'.:(.*?)/', line):
                funding_sources.append(result.strip())    	

print("Reading done.\nWriting...")

# create a dictionary
dictionary = {} 
for item in funding_sources: 
    if (item in dictionary): 
        dictionary[item] += 1
    else: 
        dictionary[item] = 1

dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse = True)
dictionary = collections.OrderedDict(dictionary)

# write to text
file = open("funding_sources.txt","w") 
dic_copy = dictionary
file.write(str(dictionary))
print("Writing done.\n\n----------------------------\n")

# print out dictionary
for key, value in dic_copy.items(): 
	print("% s : % d"%(key, value))




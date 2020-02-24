import re
import collections


print("Reading Mesh terms...")

with open('data.txt', 'r') as file:

	# Get rid of # 
	# Reason: All useful * is followed by /
    data = file.read().replace("*", "")
    # Extract mesh_term using <li> and </li>
    words_raw = re.findall(r'<li>.(.*?)</li>', data)
    mesh = []
    for word in words_raw:
    	# Split by /
    	word_list = re.split('/|,',word)
    	for w in word_list:
    		# Gest rid of white spaces
	    	mesh.append(w.strip().lower())

print("Reading done.\nWriting...\n\n----------------------------\n")

dictionary = {} 
for item in mesh: 
    if (item in dictionary): 
        dictionary[item] += 1
    else: 
        dictionary[item] = 1

dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse = True)
dictionary = collections.OrderedDict(dictionary)

file = open("mesh_terms.txt","w") 
dic_copy = dictionary
file.write(str(dictionary))
print("Writing done.")
for key, value in dic_copy.items(): 
	print("% s : % d"%(key, value))





import re
import collections

with open('data.txt', 'r') as file:
    data = file.read().replace("\n","")
    records = re.findall(r'ProjectID(.*?)aSource', data)

keywords = [["age","aging"],
            ["female","pregnanc"],
            ["veteran"],
            ["adolescen","young","child"],
            ["ethn","minority","indian","africa","mexic","hispani"]]
dictionary = {"0":0,
             "1":0,
             "2":0,
             "3":0,
             "4":0,
             "others":0}

def funding_from_record(record):
    '''
    Gets funding as int from the mess
    '''
    funding_raw = re.search(r'award amount:(.*?)projectstatus', record.lower())
    # if there is funding
    if funding_raw!= None:
        funding_str = funding_raw.group()
        # funding in the format of $xxx,xxx
        funding = int(re.search(r'\d+', funding_str.replace(",","")).group())
        return funding
    # if no, return 0
    return 0


total_funding = 0

for record in records:
    record = record.lower()
    meshterms = re.search(r'mesh terms:(.*?)dat', record).group()
    funding = funding_from_record(record)
    total_funding += funding
    others = 1

    for i in range(len(keywords)):
        # is the funding for others?
        for k in keywords[i]:
            if k in meshterms:
                others = 0
                dictionary[str(i)] += funding
                # for a keyword group, count the research for only once.
    if others == 1:
        dictionary["others"] += funding

# sort
dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse = True)
dictionary = collections.OrderedDict(dictionary)



# write to file
file = open("funding.txt","a") 
dic_copy = dictionary
file.write(str(keywords))
file.write(str(dictionary))
print("Writing done.")
print(keywords)
print("Total funding: ",total_funding)
for key, value in dic_copy.items(): 
    print("% s : % d"%(key, value))
msg="Lao People's Democratic Republic (hereafter Lao PDR) was the first country in Asia to submitits NDC, doing so in Septr 2015. Building on national development and environmental protection policies, the country aimed to make full use of existing institutional capacity and financial resources, and embed NDC targets in existing policies and planning."
print(msg)
word_list = msg.split()    # converts a string to list

counter = dict()      # empty dictionary

for word in word_list:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1


# print(counter)
for key,value in counter.items():
    print(key, value)
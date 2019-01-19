
import sys

keywords = sys.argv[1:]

count = {}
with open("Raw text", "r") as f:
 
    article = f.read().lower().split()
    
    for keyword in keywords:
        for word in article:
            if keyword in word:
                if keyword in count:
                    count[keyword]+=1
                else:
                    count[keyword]=1
print("Keyword, Frequency")
for key in count:
    print("{}, {}".format(key,count[key]))


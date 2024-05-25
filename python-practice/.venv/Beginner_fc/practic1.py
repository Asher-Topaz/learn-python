import string

#assign user input file name to fname
fname = input('Enter file name')

#use try and except to check user input meets requirements
try: 
    fhand = open(fname)
except:
    print("Could not open file")
    exit()

#create empty dictionary
counts = dict()

#read lines inside file
for line in fhand:
    #remove spaces from the line
    line = line.rstrip()

    line = line.translate(line.maketrans('','',string.punctuation))
    #turn all lines in file into lowercase letters
    line = line.lower()
    #turn each line into list of words
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)



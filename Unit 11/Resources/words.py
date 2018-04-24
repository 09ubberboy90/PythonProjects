from collections import defaultdict 

def wordFreq(inputstr):
    word = defaultdict(int)
    lower_lines = inputstr.lower()
    #splited = lower_lines.split(" ")
    buffer = []
    for tu in lower_lines:
        for el in tu:
            if 122>ord(el)>96 or ord(el) == 32:
                buffer.append(el) 
            discarded = "".join(buffer)
    splited = discarded.split(" ")
    for u in splited:
        word[u]+=1
    return word
print(wordFreq("this is a test for a random amount of words. d151 2r88 t5he the the the the"))

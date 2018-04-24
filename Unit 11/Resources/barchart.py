from Resources import words,join,Canvas,Graphs


# TASK 5
# call wordFreq from words.py
frequencies = words.wordFreq("This is the first test of the function the the the.")
freqlist = [[k,v] for k,v in frequencies.items()]

# call split from join.py
labels, data = join.split(freqlist)
print(data)

Graphs.barchart(30,20,500,200,labels,data)

# click on canvas to exit
Canvas.complete()

    
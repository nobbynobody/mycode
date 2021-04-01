#!/usr/bin/python3

correct = 0

qdata = [["What is Python's first name?", "Monty"] , ["The life of", "Brian"]]

for x in qdata:    
    question = (x[0])    
    answer = (x[1])
    useranswer = input(str(question) + ": ")
    if (useranswer.lower()).capitalize() == answer:
        correct +=1

print(f"You answered {correct} questions correctly!")



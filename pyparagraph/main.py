# import os
from csv import reader, writer
import re

# text_file = os.path.join(r'python-challenge\pyparagraph\alice_in_wonderland.txt')

with open ('python-challenge/pyparagraph/alice_in_wonderland.txt', "r",encoding = 'utf-8') as txt_f:
    alice = txt_f.read()
    
# print(alice)


def title():
    p = "Paragraph Analysis"
    s= "\n---------------"
    return p+s

def approx_word_count(string):
    analysis = re.compile(r"\b[\w']+\b",re.I) #complete words
    match = analysis.findall(string)
    return "Approximate Word Count: "+str(len(match))

def approx_sent_count(string):
    analysis = re.compile(r"[\s\w,'-]+",re.I) #complete sentences
    match = analysis.findall(string)
    return "Approximate Sentence Count: "+str(len(match))

def average_sent_len(string):
    num_sum = 0
    analysis = re.compile(r"[\s\w,'-]+",re.I) #avg sentence len
    match = analysis.findall(string)
    for i in range(len(match)):
        num_sum += len(match[i])
    return "Average Sentence Length:"+str(num_sum/len(match))

def average_letter_count(string):
    analysis = re.compile(r"\w",re.I) #complete sentences
    match = analysis.findall(string)
    return "Average Letter Count:"+str(len(match)/132.8)



print(title())
print(approx_word_count(alice))
print(approx_sent_count(alice))
print(average_letter_count(alice))
print(average_sent_len(alice))

# print(alice)

with open("python-challenge/pyparagraph/Py_Paragraph_output.txt","w") as file:
    py_paragraph_write = writer(file)
    py_paragraph_write.writerow([title()])
    py_paragraph_write.writerow([approx_word_count(alice)])
    py_paragraph_write.writerow([approx_sent_count(alice)])
    py_paragraph_write.writerow([average_letter_count(alice)])
    py_paragraph_write.writerow([average_sent_len(alice)])

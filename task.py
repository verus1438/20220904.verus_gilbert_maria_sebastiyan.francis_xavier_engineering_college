# Python code to illustrate with()
# from ctypes.wintypes import WORD
import csv,time,tracemalloc
from csv import writer
from doctest import OutputChecker
from gettext import translation
from sre_constants import SUCCESS
from traceback import print_tb
# from fnmatch import translate
start = time.time()
tracemalloc.start()
temp_line = ""
french_words = {}
findwords = []
frequency = []
frequency_Output = []

def wordTranslate():
    inputfile = []
    with open('french_dictionary.csv') as f:
        french_words = dict(filter(None, csv.reader(f)))
    with open("find_words.txt") as file:
        data = file.read()
        findwords = data.split("\n")
        length = len(findwords)
        frequency = [0] * length
    op = open("output.txt",'w+')
    op.truncate(0)
    with open("t8.shakespeare.txt",'r') as file:
        inputfile = file.readlines()
    
    for line in inputfile:
        temp_line = line
        for word in findwords:
            if word in temp_line:
                index = findwords.index(word)
                frequency[index] += 1
                for key,value in french_words.items():
                    if key == word:
                        outputline = temp_line
                        temp_line = outputline.replace(word,value)
        op.writelines(temp_line) 
    i = 0
    for key,value in french_words.items():
            frequency_Output.append([key,value,frequency[i]])
            i += 1
    with open("outputFile.csv",'a',newline='') as output:
        output.truncate(0)
        writerObj = writer(output)
        for row in frequency_Output:
            writerObj.writerow(row)
        output.close() 
    print("Success")   
    #         # temp_line = line
    # for word in findwords:
    #     freq_count = 0
    #     for line in inputfile:
    #         if word in line:
    #             freq_count +=1
    #     frequency[word] = freq_count

                    
    # print(frequency)      
    op.close()
    end = time.time()
    print("Time  ",end - start)   
    print(tracemalloc.get_traced_memory())    
    tracemalloc.stop()      
if __name__ == '__main__':
    wordTranslate()
    


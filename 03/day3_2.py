
import re
index_liste = []

def day3(filename):
    max_voltage = 0
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            getVoltage(line)
            max_voltage += int(line)
    return max_voltage
 
def getVoltage(line): 
    digits_count = len(str(line))
    i = 1
    if digits_count != 12:
        i_str = str(i)
        anzahl_ = line.count(i_str)
        if digits_count - anzahl_ > 12:
            line = re.sub('[1]', '', line)
            digits_count = len(str(line))
            print(digits_count, line)
        else: 
            gap = 12 - (digits_count - anzahl_)
            for index, char in enumerate(line):
                ziffer = int(char)
                print('Ziffer:',ziffer)
                print('Index:', index)
                if ziffer == i:
                    index_liste.append(index)
            line_list = list(line)   
            
            #for index_zwei, char_zwei in enumerate(line_list):
            #    if index_zwei < gap:
            #        do_something_to(item)
            print(line_list)
            print(index_liste)
    
    
    return line




def anzahlZiffern(line):
    linecount = len(str(line))
    anzahl_ = line.count('1')
    if linecount - eins < 12:
        gap = 12-(linecount - eins)
        cutLineFull(1)
    cutLinePartially(1,eins)
    zwei = line.count('2')
    drei = line.count('3')
    vier = line.count('4')
    fuenf = line.count('5')
 
# Aufruf:
result = day3("inputTag3.txt")
print("Gesamt-Maximalspannung:", result)
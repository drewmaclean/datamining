import sys
import csv
from statistics import *

def main(readfile, writefile, iterations):
    fWriter = open(writefile, 'w', newline='')
    csvwriter = csv.writer(fWriter, delimiter=',')

    fReader = open(readfile, 'r', newline='')
    csvreader = csv.reader(fReader, delimiter=',')

    header = csvreader.__next__()
    csvwriter.writerow(header)

    for row in csvreader:
        rowlist = []
        for i, col in enumerate(row):
            col_lst = []
            col = col.split(' ')
            if i == 5:
                try:
                    col_result = mode(col)
                except:
                    col_result = 0
            else:
                for item in col:
                    if -900 <= float(item) <= 900:
                        col_lst.append(float(item))  # change to float
                if not col_lst:
                    col_lst = [0]
                col_result = mean(col_lst)
                #print("s " + str(col))
            rowlist.append(col_result)
        csvwriter.writerow(rowlist)

        if csvreader.line_num % 100 == 0:  # print progress
            progress = csvreader.line_num / int(iterations) * 100
            sys.stdout.write("File progress: %d%%   \r" % progress)
            sys.stdout.flush()
        if csvreader.line_num >= int(iterations):  # break if number of lines are reached
            print("File Completed")
            break

    fReader.close()
    fWriter.close()


#main('train_2013.csv', 'train_small.csv', 100000)
main(sys.argv[1], sys.argv[2], sys.argv[3])

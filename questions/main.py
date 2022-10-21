import csv

filename = 'questions.csv'

# 辞書型で保持
ans_lists = dict()
with open(filename, encoding='utf-8-sig', newline='') as f:
    csvreader = csv.reader(f)
    row_num = 1
    for row in csvreader:
        ans_lists[row_num] = row
        row_num += 1



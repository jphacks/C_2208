import csv
import random

filename = 'questions.csv'

# 辞書型で保持
ans_lists = dict()
with open(filename, encoding='utf-8-sig', newline='') as f:
    csvreader = csv.reader(f)
    row_num = 1
    for row in csvreader:
        ans_lists[row_num] = row
        row_num += 1

# 乱数生成（引数：最大問題数，欲しい問題数）
def random_generator(max_question_num, want_question_num):
    previous = []
    while len(previous) < want_question_num:
        random_num = random.randint(1, max_question_num)
        if not random_num in previous:
            previous.append(random_num)
    return previous

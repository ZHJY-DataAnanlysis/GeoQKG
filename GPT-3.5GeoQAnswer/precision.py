import csv
import re

correct_answer={}
with open('str_exp_new2.csv',newline='',encoding='gbk') as csvfile:
    csv_read=csv.reader(csvfile)
    for r in csv_read:
        correct_answer[r[0]]=r[4]


sum=0
count=0
with open('gpt-3.5-turbo-16k-0613result1.txt', 'r',encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        sum += 1
        # print(line)
        answer=line.strip().split(':')  # 使用 strip() 方法去除行末的换行符
        # print(answer)
        if answer[0] not in correct_answer.keys():
            continue
        else:
            ans=answer[1].split( )
            degree=[re.sub(r'\D', '', item) for item in ans]
            numbers = [item for item in degree if re.match(r'^\d+(\.\d+)?$', item)]
            print(numbers)
            for number in numbers:
                if number==correct_answer[answer[0]]:
                    count+=1
print(sum)
print(count)
print('正确率：',count/sum)
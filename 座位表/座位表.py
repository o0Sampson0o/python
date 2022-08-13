import random as rnd #import random and name it as rnd
import sys #system
import csv

student_m = ["陈毅恒", "颜荣发", "林俊杰", "周勇祥", "黃尚堯", "林昕肯", "黄勇恺", "吕世文", "郑轩", "张宇恒", "辜津傑", "王子翊", "黄永承", "黄胤健", "陈绍翊", "陈云起", "廖侨华", "吴维杰", "郑正褀", "洪语涵", "陈子健", "张俊豪", "陈炜轩", "何一汎", "徐梓严", "颜展正", "吴永赐"]

student_f = ["陈玮欣","林芝勤","刘昱婷","郑安彤","郭丝霓","苏婕琳","黄嘉婧","林妤昕","李芷仪","余慧敏","廖欣蜜","邹欣彤","林思恩","李翎瑄","李佳璇","颜馨茹","王佳凌"]
    
seat = [["", "", "", ""]]

for i in range(4, 48): #i = 4, 5 ,6 ,7 ,8, ..., 48  == for loop
    mod_8 = i % 8
    if mod_8 == 0:
        seat.append([]) # append == add a element at back
    if (mod_8)%2 == 0 or len(student_f) == 0: #len == length of
        rand = rnd.randint(0, len(student_m)-1)
        seat[int(i/8)].append(student_m[rand])
        student_m.remove(student_m[rand])
    else:
        rand = rnd.randint(0, len(student_f)-1)    
        seat[int(i/8)].append(student_f[rand])
        student_f.remove(student_f[rand])


with open('座位表.csv', 'w', newline='', encoding='utf-8-sig') as file: #open a csv(comma separated value) file, name of variable of file == file， name of file == 座位表.csv
    writer = csv.writer(file)
    writer.writerows(seat)
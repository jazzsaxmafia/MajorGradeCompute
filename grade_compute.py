#-*- coding: utf-8 -*

""" when you want to calculate the grade of only your major courses, use this"""
fin= open("Untitled.csv")
fout = open("output.txt", "w");
score_dic = {
                "A+":4.5,
                "A" :4.0,
                "B+":3.5,
                "B" :3.0,
                "C+":2.5,
                "C" :2.0
            };

score_sum = 0;
num_major = 0;
isu = 0;
while 1:
    one_line = fin.readline();
    if not one_line: break;

    split_line = one_line.split("\t");


    if split_line[4].find("전공") != -1 and split_line[9] != 'F' :
        print one_line
        score_sum += score_dic[split_line[9]];
        num_major += 1;
        isu += int(split_line[7]);

print score_sum
print num_major
print isu



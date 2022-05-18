import re

def read_file(filename):
    global file_data #boi vi goi lai ham read_file trong chinh function read_file 
    path_to_file = 'Data_Files/' + filename + '.txt'
    try:
        file_data = open(path_to_file)
        print('Successfully opened '+filename+'.txt')
    except:
        print("Sorry, I can't find this file name")
        filename = input('Please enter file name again or "Quit" to exit program: ')
        if filename == 'Quit' :
            exit()
        else :
            read_file(filename)
    return file_data,filename
    
def write_file(score,filename):
    for i in range(len(score)):
        score[i] = [str(j) for j in score[i]]
        score[i] = ','.join(score[i])
    score_in_str = '\n'.join(score)
    filename_output = 'Output/'+filename + '_grades.txt'
    file_write = open(filename_output,'w')
    file_write.write(score_in_str)
    file_write.close()
    return
        


# Chuyen dap an thanh list de tinh diem
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')

#nap file va chuyen thanh list cua list 
filename = input('Enter file name : ')

data,filename = read_file(filename)
data = data.readlines()
data = [i.strip() for i in data]
data = [line.split(',') for line in data]



print('**** ANALYZING ****')
error_count = 0 # de dem dong loi
score = [] # luu MaHS va diem tuong ung
pattern = 'N\d{8}' # dung de kiem tra ma HS
points = [] # luu cac gia tri diem
skip = [0]*25 # list so hoc sinh bo qua theo tung cau hoi
wrong = [0]*25 # list so hoc sinh tra loi sai theo tung cau
for line in data:
   
    if len(line) != 26:
        print('Invalid line of data: does not contain exactly 26 values: ')
        error_count += 1
        print(line,'\n')
    elif not(re.match(pattern,line[0])):
        print('Invalid line of data: N# is invalid')
        error_count += 1
        print(line,'\n') 
    else:
        point = 0    
        for i in range(1,len(line)):
            if line[i] == '':
                skip[i-1] +=1
            elif line[i] == answer_key[i-1]:
                point += 4
            else:
                point -= 1
                wrong[i-1] += 1
        score.append([line[0],point])
        points.append(point)

if error_count == 0:
    print('No errors founds \n')
valid_lines = len(data) - error_count     
print('**** REPORT ****\n')
#print('tong so dong',len(data))
print('Total valid lines of data: ', valid_lines)
print('Total invalid lines of data: ', error_count,'\n')

write_file(score,filename)


high_score = 0
for i in points :
    if i > 80:
        high_score +=1
print('Total student of high scores: ', high_score,'\n')

mean_score = sum(points)/len(points)
print('Mean (average) score: ',"%.2f"%mean_score,'\n')

max_score = max(points)
print('Highest score: ', max_score)
min_score = min(points)
print('Lowest score: ', min_score)

print('Range of scores: ',max_score - min_score,'\n')

points = sorted(points)
if len(points)%2 == 0:
    median_score = (points[int(len(points)/2)-1] + points[int(len(points)/2)])/2
else :
    index =int((len(points)+1)/2)-1
    median_score = points[index]


print('Median score: ', "%.2f"%median_score,'\n')

max_skip = max(skip)
percent_max_skip = max_skip/valid_lines
text = ''
for i in range(len(skip)):
    if skip[i] == max_skip:
        text += str(i+1) +'-'+ str(max_skip) +'-'+ str("%.2f" %percent_max_skip) + ', '

print('Question that most people skip:', text)

max_wrong = max(wrong)
percent_max_wrong = max_wrong/valid_lines
text = ''
for i in range(len(wrong)):
    if wrong[i] == max_wrong:
        text += str(i+1)+'-'+ str(max_wrong) + '-' + str("%.2f"%percent_max_wrong)+', '
print('Question that most people answer incorrectly: ', text)

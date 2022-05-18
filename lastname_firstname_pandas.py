import pandas as pd

def read_file(filename):
    global file_data #boi vi goi lai ham read_file trong chinh function read_file 
    path_to_file = 'Data_Files/' + filename + '.txt'
    try:
        file_data = pd.read_csv(path_to_file,header=None,on_bad_lines= 'skip')
        print('Successfully opened '+filename+'.txt')
    except:
        print("Sorry, I can't find this file name")
        filename = input('Please enter file name again or "Quit" to exit program: ')
        if filename == 'Quit' :
            exit()
        else :
            read_file(filename)
    return file_data,filename
    
filename = input('Enter file name : ')

data,filename = read_file(filename)

print(data.head())
print(data)
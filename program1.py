import os
import shutil
input_path = str(input("Enter the input path: "))
destination = str(input("Enter the output path: "))
os.chdir(input_path)
#destination = 'D:\\test2'
for f in os.listdir():
    file_name, file_type = (os.path.splitext(f))
    if (file_type == '.txt'):
        print(file_name)
        #twarc hydrate tweet_ids.txt > tweets_hydrated.jsonl
        new_file_type = '.jsonl'
        new_name = '{}{}'.format(file_name, new_file_type)
        try:
            os.system('twarc hydrate ' + file_name + file_type + ' > ' + new_name + '.jsonl')
            shutil.move(new_name+'.jsonl', destination)
        except: 
            #print("skip")
            continue

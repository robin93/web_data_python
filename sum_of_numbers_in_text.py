import re
#input_text = open('regex_sum_42.txt','r+')   #1
input_text = open('regex_sum_207194.txt','r+')
full_sum = 0
for line in input_text.readlines():
     #print line
     list_of_numbers = re.findall('[0-9]+',line)
     if list_of_numbers:
         #print list_of_numbers,'\n'
         #print sum(map(int,list_of_numbers))   #2
         full_sum = full_sum + sum(map(int,list_of_numbers))

print 'final sum is : ',full_sum














#1 http://www.tutorialspoint.com/python/python_files_io.htm
#2 http://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int

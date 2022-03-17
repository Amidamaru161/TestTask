file_name=input("Укажите абсолютный путь к файлу: ")
file =open(file_name,'r')
str_list=[]
for line in file :
    n=line.rstrip('\n')
    str_list.append(n)
nums = [int(x) for x in str_list]
file.close()
m = sorted(nums)[len(nums) // 2]
print(sum(abs(v - m) for v in nums))
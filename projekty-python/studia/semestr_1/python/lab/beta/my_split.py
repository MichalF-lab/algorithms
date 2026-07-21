def my_split(numbers):
    a = []
    a_temp = ""
    i = 0
    for j in range(len(numbers)):
        if(numbers[j] == "," or numbers[j] == " "):
            if(len(a_temp) == 0): continue
            a.append(a_temp)
            a_temp = ""
            ++i
            continue
        a_temp+=(numbers[j])
    a.append(a_temp)
    return a


numbers_in_string ="9.9,22,1,44 , 22 ,22 ,121,3.14"
print(my_split(numbers_in_string))
import random
import os
if __name__ == '__main__':
    m = int(input("Please input machine number:"))
    n = int(input("Please input work number:"))
    if m > n :
        print("machine number has to greater than work number")
    work_time = []
    for i in range(n):
        work_time.append(random.randint(1,100))
        print(work_time[i],end = ' ')
    print('')
    average = sum(work_time)/m
    print("average = "+str(average))
    machine = []
    tmp_n = n
    for i in range(m-1):
        min = sum(work_time)
        tmp_machine = 0
        for j in range(2**tmp_n):
            tmp = []
            for k in range(tmp_n):
                if (j>>k) & 1 :
                    tmp.append(work_time[k])
            diff = abs(sum(tmp)-average)
            if diff < min:
                min = diff
                tmp_machine = j
        tmp = []
        for j in range(tmp_n):
            if (tmp_machine>>j) & 1 :
                tmp.append(work_time[j])
        machine.append(tmp)
        tmp_n = tmp_n - len(tmp)
        for j in range(len(tmp)):
            work_time.remove(tmp[j])
    machine.append(work_time)
    print("solution:")
    for i in range(m):
        print("Machine"+str(i+1)+":",end='')
        for j in range(len(machine[i])):
            print(machine[i][j],end=' ')
        print('')
    input_tmp = input("press to exit")
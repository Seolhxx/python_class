sum = 0
#i = 0
i = 5

#while i<5:
while (i): # 의미
    n = int(input("input number(>10): "))
    if n <= 10:
        print("Give me bigger one. (>10)")
        continue
        #i -= 1
        #number = 0
    sum += n #여기서부터 if에서 빠져나온건가
    #i += 1
    i-=1

avg = sum/5
print("sum{0}, avg={1}".format(sum, avg))
#print("sum=%d, avg=%.1f" %(sum,avg))


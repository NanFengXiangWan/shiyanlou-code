for values in range(1,101):
    if values % 7 == 0 or values % 10 == 7 or values // 10 == 7:
        continue
    else:
        print(values)
   

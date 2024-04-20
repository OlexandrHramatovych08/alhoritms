def binery_search(min,max,goal,count = 1):
    middle = (min+max)//2
    print("{}) {}".format(count,middle))
    if middle == goal:
        print (f"Done with {count} counts")
        return count
    while middle != goal:
        if middle > goal:
            count += 1
            binery_search(min,middle,goal,count)
        if middle < goal:
            count += 1
            binery_search(middle,max,goal,count)
        break

num1 = int(input("Enter the first number(minimum of diapason): "))

num2 = int(input("Enter the second number(maximum of diapason): "))
goal = int(input("Enter the goal that you want o achieve: "))
print(binery_search(num1,num2,goal))



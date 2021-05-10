#sum current no. and previous no. together





for i in range(10):
    i = i+1
    print("Current Number" + str(i))
    if i>=1:
        print("Previous Number" + str(i-1))
        print("Sum" + str(i+i-1))
    elif i==0:
        print("previous Number" + str(i))
        print("Sum" + str(i+i))
    else:
        break


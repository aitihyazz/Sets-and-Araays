import array as arr
arraynum=arr.array('i',[1,3,5,7,3])
print("original array",(arraynum))
print("Number of occurance"+str(arraynum.count(3)))
arraynum.reverse()
print("Reverse order of the items")
print(str(arraynum))
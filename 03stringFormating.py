
varString1=5

print("The number is {0}, Squre is {1}, Cube is {2}".format(varString1,varString1*varString1,varString1*varString1*varString1))

#No  Alignment
for i in range(5):
    print("The number is {0}, Squre is {1}, Cube is {2}".format(i,i*i,i*i*i))
    print(f"The number is {i}, Squre is {i*i}, Cube is {i*i*i}")

pi=22/7
print("Pi is {0}".format(pi))
print("Pi is {0:22}".format(pi))
print("Pi is {0:12f}".format(pi))
print("Pi is {0:12.50f}".format(pi))

#Right Alignment
print("pi is {0:52.50f}" .format(pi))
print("pi is {0:62.50f}" .format(pi))
print("pi is {0:55.2f}" .format(pi))

#Left Alignment
for i in range(13):
    print("The Number Left align {0:2}, squre is {1:<3}, Cube is {2:4}".format(i, i * i,
                                                                i * i * i))










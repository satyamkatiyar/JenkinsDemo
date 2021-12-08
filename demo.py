print('*** Hello - This is Demo ****')
print('*** Below is list of 25 test files to be executed ****')
TestList = ["File1.jmx", "File2.jmx", "File3.jmx", "File4.jmx", "File5.jmx"]
count = 0
for test in TestList:
    count += 1
    print("Test{}: {}".format(count, test.strip()))

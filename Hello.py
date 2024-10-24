from os import cpu_count
from sys import getswitchinterval
import printstream

cpu_count = cpu_count()
swtch_interval = getswitchinterval()

if True:
    print('max')
    #print(dir(os))
    #print(dir(sys))
    print(dir(printstream))
    print(cpu_count)
    print(swtch_interval)
    print(type(cpu_count))
    print(type(swtch_interval))
    print(type(cpu_count))
    print('My system\'s cpu count is ' , cpu_count)
    print('My system\'s cpu count is ' ,cpu_count, ' and My system switch interval count is ' , swtch_interval)
    print('First statement: {} and second statement: {}'.format(cpu_count,swtch_interval))
    print(f"First statement: {cpu_count} and second statement: {swtch_interval}")
    print(type(print))
else:
    print('min')

#A class will have variables and methods (functions)
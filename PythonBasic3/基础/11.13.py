import sys
def process(string):
    print('Process:',string)
for line in sys.stdin:
    process(line)
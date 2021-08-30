import argparse

parser=argparse.ArgumentParser()
parser.add_argument("nums",nargs='*')
args=parser.parse_args()
sum=0
for a in args.nums:
    sum+=a
print(sum)
    
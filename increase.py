import subprocess as sb
from random import choice as chc
from colorama import Fore,Back,Style

alphabets=[
    'a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z'
]

big_alph=[big.upper() for big in alphabets]

numbers=list(i for i in range(10))
#print(numbers)

le=chc(alphabets)
num=str(chc(numbers))
big=chc(big_alph)
to_change=big+le+num+num+big+le+le+num+big+num+le+big+big
for i in range(20):
    with open("keys.txt",'a') as f:
        f.write(to_change)

    git_add=sb.Popen(["git", "add","."], stdout=sb.PIPE, stderr=sb.PIPE, text=True)
    git_add.wait()
    print(git_add.communicate())
    git_commit=sb.Popen(["git", "commit","-m",to_change], stdout=sb.PIPE, stderr=sb.PIPE, text=True)
    git_commit.wait()
    print(git_commit.communicate()," ",f"  {Fore.GREEN} {i} {Fore.RESET}" )

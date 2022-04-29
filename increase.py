import os
import random as rd



howmany=int(input('Enter how many commits: '))


alphabets=[chr(i) for i in range(ord('a'),ord('z')+1)]
#big_alpha=list(filter(lambda x:x.upper(),alphabets))
big_alpha=[x.upper() for x in alphabets]
numbers=[str(x) for x in range(10)]
symbools=['!','@','#','$','%','^','&','*','(',')','-','+','=','_','{','}','[',']']



def commiter(limiter):
    for i in range(limiter):
        commit_msg=rd.choice(alphabets)+rd.choice(big_alpha)+rd.choice(numbers)+rd.choice(symbools)+rd.choice(alphabets)+rd.choice(big_alpha)+rd.choice(numbers)+rd.choice(symbools)+rd.choice(alphabets)+rd.choice(big_alpha)+rd.choice(numbers)+rd.choice(symbools)+rd.choice(alphabets)+rd.choice(big_alpha)+rd.choice(numbers)+rd.choice(symbools)+rd.choice(alphabets)+rd.choice(big_alpha)+rd.choice(numbers)+rd.choice(symbools)+rd.choice(alphabets)+rd.choice(big_alpha)+rd.choice(numbers)+rd.choice(symbools)
        with open('keys.txt','a') as f:
            f.write(commit_msg+'\n')
        os.system('git add keys.txt')
        print(os.system(f'git commit -m "Secret key added"'))

    

commiter(howmany)
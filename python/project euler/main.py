
primes=[2,3,5,7,11,13,17,19]

def is_prime (x):
    # for i in range (primes[0], int(x/2+1),2):
    if int(x/2+1)>primes[-1]:
        prime_hunter(int(x/2+1))
    for j in primes:
        if x %j ==0:
            return False
    return True

def prime_hunter(x):
    #find all primes before x
    if primes[-1] >= x :
        return
    for i in range (primes[-1], int(x/2+1),2):
        if is_prime(i):
            primes.append(i)

def prime_factors(x):
    factors= set()
    prime_hunter(x)
    for i in primes:
        if x%i ==0:
            factors.add(i)
            x/=i
        if x<i: break
    return len(factors)
    
def checklist(l):
    isgood=True
    for i in l.keys():
        if l[i] == 0:
            l[i] = checknum(i)
        if l[i]== False:
            isgood=False
    return isgood
    
def checknum(x):
    if prime_factors(x) ==4:
        return True
    else: return False


def orgasm(x):
    #find thw smallest number which has 4 consecutive integers with  numbers 

    cache = {x:0,x+1:0,x+2:0,x+3:0}
    while checklist(cache)==False:
        cache.pop(list(cache.keys())[0])
        cache[list(cache.keys())[2]+1]=0
        if cache[list(cache.keys())[2]+1]%100==0:
            print(cache)

    print(cache)



orgasm(700)
n = 1234567890987654321965
result = 0
import time
start = time.time()
def firstDigit(num):
    while num >= 10:
        num //= 10
    return num

def count(num):
    ctr = 1
    while num >= 10:
        num = num // 10
        ctr += 1
    return ctr

if n % 10 == 0:
    result = n-1

else:
    f = firstDigit(n)
    len_n = count(n)
    if f == 1: 
        sec = n // 10**(len_n-2)
        if sec % 10 != 0:                           ###  n ==> n-1 + 99999...
            place = len_n - 2
            result = (sec-1) * (10 ** place)
            
            while place >= 1:
                place -= 1
                result = result + 9 * (10 ** place)

        if result == 0:
            place = (len_n-2)
            while(sec%10 == 0):     ### Check for 1005
                place += 1
                sec = n // 10**(len_n-place)
            if place == len_n:result = n

        if result == 0:
            sec = n // 10**(len_n-2)
            place = len_n - 3
            while(sec%10 == 0): 
                sec = n // 10**(len_n-place)
                place += 1

            digit = len_n - (place-1)
            result = (sec-1)* (10 ** digit)

            while digit > 0:
                digit -= 1
                result = result + 9 * (10 ** digit)


    
    elif f != 1:
        place = len_n-1
        result = (f-1)* (10 ** place)
        while place >= 1:
            place -= 1
            result += 9 * (10 ** place)
        
    


print(result)
print(time.time() - start)
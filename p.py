#Project 11
#By Arturo Ortiz, arturo.ortiz1@marist.edu

def main(n):
    a = []
    b = []
    for i in range(2,n+1):
        if i not in a:
            b.append(i)
            #Adds another number to the list each loop
            for j in range(i*i,n+1,i):
                a.append(j)
                
        #New list with all the prime numbers
    return b
prime = int(input("Primes less than or equal to what number (n): "))
print(main(prime))

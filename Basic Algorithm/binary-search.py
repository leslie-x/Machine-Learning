#Binary search algorithm
#A must be a linear array, v is the value u want to search
def bsa(A,v):
    #def 'a' as head, 'b' as tail
    a=0
    b=len(A)-1
    while a<=b:
        c=(a+b)/2
        #c=int/int=float & list index must be an int,so let 'k' be an int
        k=int(c)
        if A[k]==v:
            return(f"find {v}!")   
        elif A[k]<v:
            #v is on the righthand of A[k], so move the head 'a'
            a=k+1
        else:
            #v is on the lefthand of A[k], so move the tail 'b'
            b=k-1
    return(f"can't find {v}!")
    
array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#use input() to get what u type as a string
value=input("search num: ")
#then use int() to make a string an int
value=int(value)

search=bsa(array,value)

print(search)
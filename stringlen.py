str=(input("Enter the string :"))
count=0
str.lower()
a=list(str)
s=len(a)
for i in range(s):
    if str[i] in str[:i]:
        count=count+1
print(s-count)
    
        
        
            
        

    
    

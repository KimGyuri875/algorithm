def function(n):
    a0 = 1 ;
    a1 = 0;
    temp = 0;
    for i in range(n):
        temp = a0;
        a0 = a0 + a1;
        a1 = temp;
    return a1;

n = int(input());
print(function(n)); 


"""
시간 초과
def function(i):
  if (i <= 1):
    return i;
  return function(i-1) + function(i-2);

n = int(input());
print(function(n)); 
"""

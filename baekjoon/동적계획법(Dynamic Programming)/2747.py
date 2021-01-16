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

호출된 각 함수가 계속해서 함수를 두 개씩 호출하게 된다. 
결국 시간복잡도가 O(2^N)이므로 n 제한이 n<=45인 해당 문제의 경우 제한시간 내에 답을 구할 수 없다.
"""

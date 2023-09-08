import torch 
import torch.nn as nn
# reshape() : 차원 모양 변경 가능 (입력깂: contiguous, non-contiguous 가능)
# view() : 차원 모양 변경 가능 (입력값: contiguous한 tensor만 가능)
a = torch.arange(1, 25)
print(a)

b= a.reshape(4,6)
print(b, b.size())
b= a.reshape(2,2,6)
print(b)
b= a.reshape(2,2,-1) # 음수는 자동으로 차원계산, 2 x 2 x 6
print(b)
c= b.reshape(3,-1)
print(c)

b= a.view(4,6)
print(b, b.size())
b= a.view(2,2,-1)
print(b)
c= b.view(3, -1)
print(c)  # reshape()과 view() 결과 동일

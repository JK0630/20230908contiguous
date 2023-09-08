import torch 

# permute() : 모든 차원을 교환가능, transpose(): 2개의 차원만 교환가능

a = torch.arange(1, 25)
print(a)

b = a.reshape(2,3,4)
print(b, b.size())
b = b.permute(1,2,0) # 차원 교환하기 2 x 3 x 4 -> 3 x 4 x 2
print(b, b.size())
c = b.reshape(3, -1)
print(c,c.is_contiguous())

b= a.view(2,3,4)
print(b, b.size())
b = b.transpose(2,0) # 차원 교환하기 2 x 3 x 4 -> 4 x 3 x 2
# b = b.transpose(2, 0).contiguous() # 2개의 차원 교환하기
                        # 2 x 3 x 4 -> 4 x 3 x 2

print(b, b.size(), b.is_contiguous())

c= b.reshape(3, -1) # contiguouse 한 tensor만 변경 가능
print(c, c.is_contiguous())
import torch 
a = torch.arange(1, 13)
print(a)
a = a.reshape(3,4)
print(a)

a = a.transpose(1,0)
print(a, a.is_contiguous()) # False
for i in range(4):
    for j in range(3):
        print(a[i][j].data_ptr()) # memory 주소 확인, non-contiguous
a = a.reshape(2,6)
print(a, a.is_contiguous()) # True
for i in range(2):
    for j in range(6):
        print(a[i][j].data_ptr()) # memory 주소 확인, contiguous

import torch 
import torch.nn as nn

x = torch.full((5,2),1.)

a = torch.tensor([1, 2, 3, 4, 5])
print(a.is_contiguous())
print(x.is_contiguous())
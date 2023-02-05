import torch
from pytorch_utils import moveTo

device = torch.device("mps")
some_tensors = [torch.tensor(1), torch.tensor(2)]
print(some_tensors)

print(moveTo(some_tensors, device))

exit()

import timeit
import torch

device = torch.device("mps")

x = torch.rand(2**11, 2**11)
time_cpu = timeit.timeit("x@x", globals=globals(), number=100)
print(time_cpu)

x = x.to(device)
time_gpu = timeit.timeit("x@x", globals=globals(), number=100)
print(time_gpu)



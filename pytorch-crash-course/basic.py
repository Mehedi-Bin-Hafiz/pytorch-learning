import torch
import time

time_start = time.time()

a = torch.randn(20000, 20000, device='cuda')
b = torch.randn(20000, 20000, device='cuda')
c = torch.matmul(a, b)

print(f"Time taken on GPU: {time.time() - time_start}")


time_start = time.time()
a = torch.randn(20000, 20000, device='cpu')
b = torch.randn(20000, 20000, device='cpu')
c = torch.matmul(a, b)
print(f"Time taken on CPU: {time.time() - time_start}")
import torch
def check_cuda():    if not torch.cuda.is_available():        print("Warning: CUDA not available. Falling back to CPU.")
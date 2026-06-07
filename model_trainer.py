import warnings

# Check for CUDA availability
if not torch.cuda.is_available():
    warnings.warn("CUDA is not available, falling back to CPU.")

# Rest of your code here...
def save_checkpoint(model, path='checkpoints/model.pth'):
    # Updated logic for saving checkpoint
    model.save(path)
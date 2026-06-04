def load_checkpoint(optimizer):
    # Load optimizer state
    optimizer.load_state_dict(torch.load('optimizer_state.pth'))
    return optimizer
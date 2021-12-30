
import torch
import semi_global_matching_cuda

def sgm_gpu(left, right):
    assert len(left.shape) == 2
    assert len(right.shape) == 2
    assert (left.shape[0] // 4 == 0) and (left.shape[1] // 4 == 0)
    assert (right.shape[0] // 4 == 0) and (right.shape[1] // 4 == 0)

    H, W = left.shape

    left = left.to(torch.uint8).cuda()
    right = right.to(torch.uint8).cuda()

    dispmap = semi_global_matching_cuda.sgm(
        left, right, 7, 86, H, W)

    return dispmap

if __name__ == '__main__':
    print('hi')

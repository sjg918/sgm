
import torch
import semi_global_matching_cuda
import cv2
import numpy as np

def mkDispmap(left, right, pathA, return_gpu=False):
    assert len(left.shape) == 2
    assert len(right.shape) == 2
    assert (left.shape[0] % 4 == 0) and (left.shape[1] % 4 == 0)
    assert (right.shape[0] % 4 == 0) and (right.shape[1] % 4 == 0)

    H, W = left.shape

    left = left.cuda()
    right = right.cuda()


    if pathA == 2:
        dispmap = semi_global_matching_cuda.sgm(left, right, 7, 84, H, W, 2)
    elif pathA == 4:
        dispmap = semi_global_matching_cuda.sgm(left, right, 7, 92, H, W, 4)
    elif pathA == 8:
        dispmap = semi_global_matching_cuda.sgm(left, right, 6, 96, H, W, 8)

    if return_gpu:
        return dispmap
    else:
        return dispmap.cpu().numpy()

if __name__ == '__main__':
    Limg = cv2.imread('left.png')
    Rimg = cv2.imread('right.png')
    h, w, _ = Limg.shape

    top_pad = 384 - h
    right_pad = 1248 - w
    assert top_pad > 0 and right_pad > 0
    # pad images
    Limg = np.lib.pad(Limg, ((top_pad, 0), (0, right_pad), (0, 0)), mode='constant', constant_values=0)
    Rimg = np.lib.pad(Rimg, ((top_pad, 0), (0, right_pad), (0, 0)), mode='constant', constant_values=0)

    Limg = cv2.cvtColor(Limg, cv2.COLOR_BGR2GRAY)
    Rimg = cv2.cvtColor(Rimg, cv2.COLOR_BGR2GRAY)

    Limg = torch.from_numpy(Limg).cuda()
    Rimg = torch.from_numpy(Rimg).cuda()
    disp = mkDispmap(Limg, Rimg, 4)

    if top_pad !=0 or right_pad != 0:
        disp = disp[top_pad:,:-right_pad]

    cv2.imshow('gg', disp)
    cv2.waitKey(0)

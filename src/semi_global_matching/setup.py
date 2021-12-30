from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='sigmoid_focal_loss',
    ext_modules=[
        CUDAExtension('sigmoid_focal_loss_cuda', [
            'src/sigmoid_focal_loss.cpp',
            'src/sigmoid_focal_loss_cuda.cu',
        ],
        extra_compile_args={'cxx': ['-g'],
                            'nvcc': ['-O2']})
    ],
    cmdclass={'build_ext': BuildExtension})

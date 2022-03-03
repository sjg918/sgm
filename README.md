
# semi global matching on gpu (pytorch build)
original repo: https://github.com/dhernandez0/sgm

# result on kitti
![sgm1](https://github.com/sjg918/sgm/blob/main/sgm1.png?raw=true)
original.
![sgmpy](https://github.com/sjg918/sgm/blob/main/sgmpy.png?raw=true)
my build.

# use
cd src<br/>
cd semi_global_matching<br/>
python setup.py build develop<br/>

# time performance
2path(7, 84) : 0.003261395271514925ms

4path(7, 92) : 0.003544897189676149ms

8path(6, 96) : 

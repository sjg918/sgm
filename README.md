
# semi global matching on gpu. (pytorch build)
original repo: https://github.com/dhernandez0/sgm

# result on kitti.
![sgm1](https://github.com/sjg918/sgm/blob/main/sgm1.png?raw=true)
original.
![sgmpy](https://github.com/sjg918/sgm/blob/main/sgmpy.png?raw=true)
my build. TOTALLY FUCKED. i dont know why.

# use.
cd src<br/>
cd semi_global_matching<br/>
python setup.py build develop<br/>

# RTX TITAN
2path(7, 84) : 0.0031381058044769937

4path(7, 92) : 0.0034623489736372018

8path(6, 96) : 0.004814395843885297

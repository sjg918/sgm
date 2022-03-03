
# semi global matching on gpu (pytorch build)
original repo: https://github.com/dhernandez0/sgm

# result on kitti (odometry)
![image](https://github.com/sjg918/sgm/blob/main/image.png?raw=true)
ori iamge
![2path](https://github.com/sjg918/sgm/blob/main/path-2.png?raw=true)
2path(7, 84) : 0.003261395271514925s
![4path](https://github.com/sjg918/sgm/blob/main/path-4.png?raw=true)
4path(7, 92) : 0.003544897189676149s
![8path](https://github.com/sjg918/sgm/blob/main/path-8.png?raw=true)
8path(6, 96) : 0.004807569295199617s

# use
cd src<br/>
cd semi_global_matching<br/>
python setup.py build develop<br/>

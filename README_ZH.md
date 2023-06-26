# DamnPythonEvasion
基于python pyd的免杀方式。众所周知，python是一种解释型语言，通过pyinstaller打包后，可以提取出pyc文件然后可以通过反编译器得到源代码。
但是我们可以通过将py源文件通过Cpython编译成pyd文件，然后pyinstaller打包的时候动态链接即可。由于pyd是通过c代码编译而成的二进制文件，所以
要从pyd得到源代码几乎不可能，从而达到保护代码的目的。

# 测试环境
1. python3.8 64位
2. vs2019(Cpython编译时需要用到)
3. pyinstaller

# 食用教程
```
1. 安装vs2019 python3
2. pip install pyinstaller
3. pip install cython
4. 修改 execute.py中的scbytes为你自己的shellcode
5. python setup.py build_ext --inplace
6. pyinstaller -F main.py -w  --noupx
```
现在如果一切顺利的话，你可以dist目录下找到打包好的main.exe文件 

# 测试结果
根据目前的测试效果，可以绕过360和火绒。

![image](https://raw.githubusercontent.com/baiyies/DamnPythonEvasion/main/images/1.png)
![image](https://raw.githubusercontent.com/baiyies/DamnPythonEvasion/main/images/2.png)
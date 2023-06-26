# DamnPythonEvasion
[中文][url-doczh]

An evasion method based on Python pyd. As we all know, Python is an interpreted language, and after packaging with PyInstaller, we can extract the pyc file and then decompile it to get the source code.
However, we can compile the py source file into a pyd file through CPython, and then dynamically link it when PyInstaller is packing. Since the pyd is a binary file compiled from C code,
it's almost impossible to get the source code from it, thereby achieving the purpose of protecting the code.

# Test Environment
1. python3.8 64-bit
2. vs2019(Needed for CPython compilation)
3. pyinstaller

# Usage Guide
```
1. Install VS2019 and Python3
2. pip install pyinstaller
3. pip install cython
4. Modify the scbytes in execute.py to your own shellcode
5. python setup.py build_ext --inplace
6. pyinstaller -F main.py -w  --noupx
```
Now if everything goes well, you can find the packaged main.exe file in the dist directory.

# Test Results
Based on current test results, it can bypass 360 and Huorong.

![image](https://raw.githubusercontent.com/baiyies/DamnPythonEvasion/main/images/1.png)
![image](https://raw.githubusercontent.com/baiyies/DamnPythonEvasion/main/images/2.png)

[url-doczh]: README_ZH.md
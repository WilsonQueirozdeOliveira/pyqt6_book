# Tec_do_Brasil

- qt6 book: Interfaces Gráficas com Python + PyQt6
- https://sqlitebrowser.org/

## miniconda not needed
## python 3.10.7
- pyinstaller-5.4.1 (bootloader compilation)
- w64devkit-1.16.1 #gcc compiler
- cd to the bootloader folder
- python.exe ./waf distclean all
- cd to root Pyinstaller directory you've created above Step 3
- Run this command: python.exe setup.py install
- optional#python.exe ./waf all --target-arch=64bit
- optional#python.exe ./waf all



## Dependecies to env (tec_py39) miniconda
- conda create -n tec_py39 python=3.9 anaconda
- for python gtk wsl : sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
- conda install -c conda-forge jupyterlab
- conda install -c anaconda pyqt
- conda install -c anaconda pip
- pip install numpy --upgrade
- pip install PyQt6
- conda install -c conda-forge nodejs
- conda install -c conda-forge opencv
- pip install auto-py-to-exe




## comands to env (tec_py39) miniconda
- jupyter lab
- python tec_system.py
- auto-py-to-exe
- pyinstaller tec_system_0.1_.py -F --noconsole


<p>miniconda Dependencies to (tec) python 3.6<br/>
miniconda<br/>
conda create --name tec python=3.6.9 ipykernel<br/>

python -m ipykernel install --user<br/>
conda install -c anaconda jupyter<br/>
conda install -c conda-forge opencv<br/>
conda install -c pytorch pytorch<br/>
conda install -c anaconda pip<br/>
pip install numpy --upgrade<br/>
conda install -c pytrch torchvision<br/>
conda install -c anaconda ipython<br/>
pip install PyQt6<br/>
pip install facenet-pytorch<br/>
pip install mmcv<br/>
conda install -c conda-forge tensorboard<br/>
conda install -c anaconda pandas<br/>
https://archive.org/download/lfw-dataset<br/>
<p/>

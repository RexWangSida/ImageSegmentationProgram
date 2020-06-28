# Image Segmentation Program
Small **Python** program performing image segmentation using **k-means clustering algorithm**

### Supported Image Types
- **JPEG(.jpg)**
- **PNG(.png)**

### Python Libraries
- **Scikit-Learn & Scikit-Image**
  - Basic usage of k-means algorithm and image image loading.
- **Numpy**
  - Matrix operations
- **Pillow(PIL)**
  - Image convert
- **Tkinter**
  - GUI
### Run the Program
- This can be done in **Windows PowerShell** or **Linux/Mac Terminal**, and it requires **git**, **python**, **Numpy**, **PIL**, **Tkinter** and **Scikit**, or at least **pip**.
- The instruction of how to install **python** can be found at [**HERE**](https://www.python.org/downloads/).
- The instruction of how to install **pip** can be found at [**HERE**](https://pip.pypa.io/en/stable/installing/).
- The instruction of how to install **git** can be found at [**HERE**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- The **Tkinter** is included in **python** standard libraries and does not need specific installation once **python** is installed.
- To install **numpy**(it requires pip to be installed), run:
```shell
pip install numpy
```
- To install **PIL**(it requires pip to be installed), run:
```shell
pip install Pillow
```
- To install **Scikit**(it requires pip to be installed), run:
```shell
pip install -U scikit-learn
```
and
```shell
pip install scikit-image
```
- To start the program, sequentially run:
```shell
git clone https://github.com/RexWangSida/ImageSegmentationProgram.git
```
```shell
cd ImageSegmentationProgram
```
```shell
python frame.py
```
## GUI
<div align='center'><img src='frame1.png' width=70%></img></div>
<div align='center'><img src='frame3.png' width=70%></img></div>

## Examples of the image processing
### Original Image
<div align='center'><img src='photo.jpg' width=70%></img></div>

### One Segment(One Cluster k == 1)
<div align='center'><img src='1.jpg' width=70%></img></div>

### Two Segments(Two Clusters k == 2)
<div align='center'><img src='2.jpg' width=70%></img></div>

### Three Segments(Three Clusters k == 3)
<div align='center'><img src='3.jpg' width=70%></img></div>

### Four Segments(Four Clusters k == 4)
<div align='center'><img src='4.jpg' width=70%></img></div>

### Five Segments(Five Clusters k == 5)
<div align='center'><img src='5.jpg' width=70%></img></div>

### Six Segments(Six Clusters k == 6)
<div align='center'><img src='6.jpg' width=70%></img></div>

### Seven Segments(Seven Clusters k == 7)
<div align='center'><img src='7.jpg' width=70%></img></div>

### Eight Segments(Eight Clusters k == 8)
<div align='center'><img src='8.jpg' width=70%></img></div>

### Nine Segments(Nine Clusters k == 9)
<div align='center'><img src='9.jpg' width=70%></img></div>

### Ten Segments(Ten Clusters k == 10)
<div align='center'><img src='10.jpg' width=70%></img></div>

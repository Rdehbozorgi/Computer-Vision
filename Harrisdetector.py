{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1871000cb00>"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "from skimage.io import imread\n",
    "from skimage.color import rgb2gray\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "\n",
    "img = imread('1pyfiles/box.jpg') # The root directory\n",
    "imggray = rgb2gray(img)\n",
    "plt.imshow(imggray)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import signal as sig\n",
    "import numpy as np\n",
    "def gradient_x(imggray):\n",
    "    ##Sobel operator kernels.\n",
    "    kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])\n",
    "    return sig.convolve2d(imggray, kernel_x, mode='same')\n",
    "def gradient_y(imggray):\n",
    "    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])\n",
    "    return sig.convolve2d(imggray, kernel_y, mode='same')\n",
    "I_x = gradient_x(imggray)\n",
    "I_y = gradient_y(imggray)\n",
    "#print(I_x)\n",
    "Ixx = I_x**2\n",
    "Ixy = I_y*I_x\n",
    "Iyy = I_y**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1870fedb320>"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from numpy import linalg as LA\n",
    "from PIL import Image\n",
    "offset=1\n",
    "k=0.04\n",
    "im = Image.open('1pyfiles/box.jpg')\n",
    "imgcopy = np.array(im)\n",
    "#import shutil  #using for copy of an image \n",
    "#shutil.copy(\"1pyfiles/box.jpg\",\"1pyfiles/box2.jpg\")\n",
    "width, height=im.size\n",
    "r = np.zeros((width-1, height-1))\n",
    " # or maybe this command height, width = np.array(im).shape\n",
    "for y in range(offset, height-offset):\n",
    "    for x in range(offset, width-offset):\n",
    "        Sxx = np.sum(Ixx[y-offset:y+1+offset, x-offset:x+1+offset])\n",
    "        Syy = np.sum(Iyy[y-offset:y+1+offset, x-offset:x+1+offset])\n",
    "        Sxy = np.sum(Ixy[y-offset:y+1+offset, x-offset:x+1+offset])\n",
    "        r1=np.array([[Sxx,Sxy],[Sxy,Syy]])\n",
    "        w, v = LA.eig(r1) \n",
    "        det=w[0]*w[1]\n",
    "        trace=w[0]+w[1]\n",
    "        r[x,y] = det - k*(trace**2)\n",
    "        if r[x,y]>0:\n",
    "            imgcopy[y,x]=[0,255,0]\n",
    "plt.imshow(imgcopy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#library for using Harris corner function\n",
    "#from skimage.feature import corner_harris, corner_peaks\n",
    "# print corner_harris(ximage)\n",
    "#coords = corner_peaks(corner_harris(imggray))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

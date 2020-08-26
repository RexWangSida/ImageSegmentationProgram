import numpy as np
from PIL import Image
import random
data = [np.array([random.randint(0,255),random.randint(0,255),random.randint(0,255)]) for i in range(100)]
data = np.array(data)
new_im = Image.fromarray(data)
new_im.save("test.png")

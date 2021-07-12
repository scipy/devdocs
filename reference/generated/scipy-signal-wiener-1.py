from scipy.misc import face
from scipy.signal.signaltools import wiener
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng()
img = rng.random((40, 40))    #Create a random image
filtered_img = wiener(img, (5, 5))  #Filter the image
f, (plot1, plot2) = plt.subplots(1, 2)
plot1.imshow(img)
plot2.imshow(filtered_img)
plt.show()

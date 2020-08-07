import numpy as np
import os


def read_images(path):
    images = []
    for (root, directories, files) in os.walk(path):
        files.sort()
        for file in files:
            A = np.fromfile(os.path.join(root, file), dtype='int16', sep='')
            A = A.reshape([512, 512])
            images.append(A)
    return images


def show_images(axs, images, titles):
    for i in range(len(axs)):
        axs[i].set_title(titles[i])
        axs[i].imshow(images[i], cmap="gray")

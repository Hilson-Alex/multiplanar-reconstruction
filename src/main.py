import matplotlib.pyplot as plt
from mpr.image_handler import read_images, show_images
from mpr.slicer import slicer


def input_range (min_value, max_value, label):
    while True:
        value = int(input(label))
        if max_value >= value >= min_value:
            return value
        print("Valores inválidos, o valor deve estar entre", min_value, "e", max_value)


path = "./resources/Arterielle/"
images = read_images(path)
while True:
    print("Dê valores para os Planos:")
    axial = input_range(0, 360, "Axial (de 0 à 360): ")
    coronal = input_range(0, 512, "Coronal (de 0 à 512): ")
    sagittal = input_range(0, 512, "Sagital (de 0 à 512): ")
    mpr_images = slicer(axial, coronal, sagittal, images)
    f, arr = plt.subplots(1, 3, num="MVP", figsize=(20, 10), gridspec_kw={'width_ratios': [10, 10, 10]})
    f.tight_layout()
    show_images(arr, mpr_images, ["Axial (Slide {}):".format(axial),
                                  "Coronal (Slide {}):".format(coronal),
                                  "Sagital (Slide {}):".format(sagittal)])
    plt.show()

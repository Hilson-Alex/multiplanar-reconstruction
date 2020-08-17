

def slicer(axial, coronal, sagittal, images):
    axial_image = images[axial]
    coronal_image = []
    sagittal_image = []
    for i in images:
        coronal_image.append(i[coronal])
        sagittal_image.append([row[sagittal] for row in i])
    return [axial_image, coronal_image, sagittal_image]

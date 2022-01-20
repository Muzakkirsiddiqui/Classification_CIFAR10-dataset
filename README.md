# Classification_CIFAR10-dataset
Transfer Learning uses information gained by training of a model on one set of data, to make training/testing on some other set of (similar) data more efficient.

This is a Keras model based on VGG16 architecture for CIFAR-10 and CIFAR-100. it can be used either with pretrained weights file or trained from scratch.

This package contains 2 classes one for each datasets, the architecture is based on the VGG-16 [1] with adaptation to CIFAR datasets based on [2]. By running the py files you can get a sample of a trining and estimation of validation error.

The CIFAR-10 reaches a validation accuracy of 73.56% CIFAR-100 reaches validation accuracy of 72.48%. On instantiation the model can either be trained or loaded from previous saved weight file.

# extract the last layer from third block of vgg16 model
#Add Classification layer on top of it
#we make our top model
#construct our full model

# Classification_CIFAR10-dataset
Transfer Learning uses information gained by training of a model on one set of data, to make training/testing on some other set of (similar) data more efficient.

This is a Keras model based on VGG16 architecture for CIFAR-10 and CIFAR-100. it can be used either with pretrained weights file or trained from scratch.

This package contains 2 classes one for each datasets, the architecture is based on the VGG-16 [1] with adaptation to CIFAR datasets based on [2]. By running the py files you can get a sample of a trining and estimation of validation error.

The CIFAR-10 reaches a validation accuracy of 73.56% CIFAR-100 reaches validation accuracy of 72.48%. On instantiation the model can either be trained or loaded from previous saved weight file.

 #Extract the last layer from third block of VGG16 model

 #Add Classification layer on top of it

 #We make our top model

 #Construct our full model

The second model trained for classes 5..9 used transfer learning to expedite the training process. It achieved an accuracy of 76.06% after 10 epochs. More importantly the training time was down to just 6 minnutes and 49 seconds.

Therefore, transfer learning significantly brought down the time for processing of data.

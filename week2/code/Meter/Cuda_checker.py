import tensorflow as tf
import torch

if tf.test.gpu_device_name():
    print('Default GPU Device of TF:{}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
    
print(f'Torch CUDA: {torch.cuda.is_available()}')
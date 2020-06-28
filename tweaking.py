import numpy as np
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
form keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.datasets import mnist
from keras.utils import np_utils as npu
from keras.backend import clear_session

(train_x,train_y,(test_x,test_y) = mnist.load_data("mymnist.data")
train_x = x_train.reshape(-1,28,28,1)
test_x = x_test.reshape(-1,28,28,1)
train_x = x_train.astype('float32')
test_x = x_test.astype('float32')
train_y = npu.to_categorical(train_y)
test_y = npu.to_categorical(test_y)

accuracy = open("accuracy.txt","r")
accuracy = float(accuracy.read())
accuracy = accuracy*100

neurons = 10
epochs = 1
test = 1
flag = 0
kernel = 8
batch_size = 128
#filter = 3


while int(accuracy)<90:
   if flag == 1:
     model = keras.backend.clear_session()
     neurons = neurons+10
     epochs = epochs+1
     test = test+1
     kernel = kernel+1
     test = test+1
   print("***TRAIL*****:", test ,"------------")
   model = Sequential()
   model.add(Conv2D(kernel,(3,3), input_shape= (28,28,1), activation= 'relu')
   model.add(MaxPoolin2D(pool_size = (2,2)))
   model.add(Flatten())
   model.add(Dense(neurons, activation = 'relu'))
   model.add(Dense(10, activation = 'softmax'))
   model.compile(optimizers = "Adam" , loss = 'categorical_cross_entropy' , metrics = ['accuracy']
   train_x.shape
   model_predict = model.fit(train_x,train_y,batch_size=batch_size,
                             verbose= 1,epochs=epochs,
                             validation_data=(test_x,test_y),shuffle=True)
   scores = model.evaluate(test_x,test_y,verbose=False
   print("Test loss:" , scores[0]*100)
   print("**ACCURACY OF THE MODEL IS :", scores[1]*100)
   accuracy = scores[1]*100
   print("----------------------")
   print()
   print()
   flag = 1
print("Total number of epochs:", epochs)
print("Total numner of filters:", kernel)
print("Total number of neurons:", neurons)
print("FINAL ACCURACY:", accuracy)


import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("sumayyakhatoon58@gmail.com","summaiya@26")
message_success "ACHIEVED YOUR DESIRED ACCURACY.CONGRATS"

s.sendmail("sumayyakhatoon58@gmail.com",message_success)
s.quit()

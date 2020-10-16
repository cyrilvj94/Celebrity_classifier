from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from tensorflow.keras.preprocessing.image import  ImageDataGenerator


class CNN_model:
    """
    Contains all the files necessary for creating the model

    """
    def __init__(self):
        pass

    def obtain_data(self, directory_path, target_size = (256, 256), batch_size = 32, ):
        """
        Creates the tuple directory iterator of shape (batch_size, target_height, target_width, channesls), (batch_size)

        :param : directory_path : directory containing all the training batch files
        :param target_size : target size of the output image
        :param batch_size : batch size
        :return: directory iterator

        """
        self.target_size = target_size
        data_gen = ImageDataGenerator(rescale= 1.0/255)
        data  = data_gen.flow_from_directory(directory_path , target_size=target_size,
                                            class_mode='categorical', batch_size = batch_size,)
        self.labels  = data.class_indices
        return data

    def create_model(self):
        """
        Creates model architecture
        :return:
        """
        model = Sequential()
        model.add(layer=Conv2D(filters=32, kernel_size=(16, 16), strides=(2, 2),
                               activation='relu',
                               input_shape=(256, 256, 3)
                               ))
        model.add(layer=MaxPool2D(pool_size=(2, 2)))
        model.add(layer=BatchNormalization())
        model.add(layer=Conv2D(filters=64, kernel_size=(4, 4), strides=(2, 2),
                               activation='relu',
                               ))

        model.add(layer=MaxPool2D(pool_size=(2, 2)))
        model.add(layer=Flatten())
        model.add(layer=Dense(120, activation='relu'))
        model.add(layer=Dropout(rate=0.2))
        model.add(layer=Dense(60, activation='relu'))
        model.add(layer=Dense(4, activation='softmax'))
        print(model.summary())
        return model

    def compile_train(self, model, train_set, test_set, epochs = 6 ,):
        model.compile(loss='categorical_crossentropy', optimizer='adam',
                      metrics=['accuracy'])
        model.fit(train_set, test_set, batch_size=64, epochs=epochs, verbose=1,
                  validation_split=0.2, shuffle=True)
        return model





import numpy
import os

# check direcotries and create them
if not os.path.exists('./data'):
    os.mkdir('./data')
else:
    pass
if not os.path.exists('./metrics'):
    os.mkdir('./metrics')
else:
    pass

# generate data
data = numpy.random.random(size=(100,20))

# save data
numpy.save('./data/raw_data.npy', data)
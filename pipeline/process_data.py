import numpy
from yaml import dump as yaml_dump
from yaml import safe_load as yaml_load

# get the parameters
with open("./params.yaml", "r") as stream:
    params = yaml_load(stream)['process_data']

# get the data
data = numpy.load('./data/raw_data.npy')

# split the data
train_last_index = int((1-params['test_size']) * len(data))
data = numpy.random.shuffle(data)
train = data[:train_last_index,:]
test = data[train_last_index:,:]

# compute some metrics
metrics = dict(
    number_train = len(train),
    number_test = len(test)
)   
with open('./metrics/process_data_metrics.yaml', "w") as stream:
    yaml_dump(metrics, stream)

# save output
numpy.save('./data/train_data.npy', train)
numpy.save('./data/test_data.npy', test)


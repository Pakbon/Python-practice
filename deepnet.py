import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('C:\\tmp\\data\\', one_hot=True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100

#h * w
x = tf.placeholder('float',[None, 784])
y = tf.placeholder('float')

def netmodel(data):
    hl1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])), 'biases':tf.Variable(tf.random_normal(n_nodes_hl1))}
    hl2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])), 'biases':tf.Variable(tf.random_normal(n_nodes_hl2))}
    hl3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl3])), 'biases':tf.Variable(tf.random_normal(n_nodes_hl3))}
    
    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])), 'biases':tf.Variable(tf.random_normal([n_classes]))}

    l1 = tf.add(tf.matmul(data, hl1_layer['weights']), hl1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hl2_layer['weights']), hl2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hl3_layer['weights']), hl3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']), hl3_layer['biases']
    return output

def train_nn(x):
    prediction = netmodel(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction,y))


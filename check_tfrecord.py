import tensorflow as tf

for example in tf.python_io.tf_record_iterator("data/train.record"):
    result = tf.train.Example.FromString(example)

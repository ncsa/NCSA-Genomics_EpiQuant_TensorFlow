import tensorflow as tf
import os

def startSession():
    """ Starts an interactive session to run the tensorflow graph. """
    # os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
    # os.environ["CUDA_VISIBLE_DEVICES"]="0,1"
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.InteractiveSession(config = config)
    # tf.global_variables_initializer().run()
    sess.run(tf.initialize_all_variables())
    return sess

def printTensors(sess, layer, snpData, phenoData, i):
    """ Prints intermediate tensors. """
    w, b = sess.run(
        [layer.w, layer.b],
        feed_dict = {
            layer.x: snpData,
            layer.y: [phenoData[i]]
        }
    )
    print(w)
    print(b)
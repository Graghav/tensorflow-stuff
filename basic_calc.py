import tensorflow as tf

a = tf.placeholder("float"); 
b = tf.placeholder("float"); 

addition = tf.add(a, b); 
multiply = tf.mul(a, b);

sess = tf.Session(); 

print "Addition: 1 + 2 = %f " % sess.run(addition, feed_dict={a: 1, b: 2}) 
print "Multiplication: 3 * 5 = %f" % sess.run(multiply, feed_dict={a: 3, b: 5})
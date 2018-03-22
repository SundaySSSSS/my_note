!# TensorFlow练习

!## 前提
```python
import tensorflow as tf
```

!## 线性函数
Y = WX + b
W, X为随机矩阵, b为随机列向量
W的维度为(4, 3), X:(3,1) b:(4,1)
```python
def linear_function():
    """
    Implements a linear function:
            Initializes W to be a random tensor of shape (4,3)
            Initializes X to be a random tensor of shape (3,1)
            Initializes b to be a random tensor of shape (4,1)
    Returns:
    result -- runs the session for Y = WX + b
    """

    np.random.seed(1)

    X = tf.constant(np.random.randn(3, 1), name="X")
    W = tf.constant(np.random.randn(4, 3), name="W")
    b = tf.constant(np.array(np.random.randn(4, 1)), name="b")
    Y = tf.add(tf.matmul(W, X), b)

    # Create the session using tf.Session() and run it with sess.run(...) on the variable you want to calculate

    sess = tf.Session()
    result = sess.run(Y)

    # close the session
    sess.close()

    return result
```

!## 计算激活函数sigmoid
```
def sigmoid(z):
    """
    Computes the sigmoid of z
    Arguments:
    z -- input value, scalar or vector
    Returns: 
    results -- the sigmoid of z
    """

    # Create a placeholder for x. Name it 'x'.
    x = tf.placeholder(tf.float32, name="x")

    # compute sigmoid(x)
    sigmoid = tf.sigmoid(x)

    # Create a session, and run it. Please use the method 2 explained above. 
    # You should use a feed_dict to pass z's value to x. 
    with tf.Session() as sess:
        # Run session and call the output "result"
        result = sess.run(sigmoid, feed_dict={x:z})

    return result
```
调用
```
print ("sigmoid(0) = " + str(sigmoid(0)))
print ("sigmoid(12) = " + str(sigmoid(12)))
```
输出
```
sigmoid(0) = 0.5
sigmoid(12) = 0.999994
```

!## 计算成本函数(cost function)
```python
def cost(logits, labels):
    """
    Computes the cost using the sigmoid cross entropy
    Arguments:
    logits -- vector containing z, output of the last linear unit (before the final sigmoid activation)
    labels -- vector of labels y (1 or 0) 
    Note: What we've been calling "z" and "y" in this class are respectively called "logits" and "labels" 
    in the TensorFlow documentation. So logits will feed into z, and labels into y. 
    Returns:
    cost -- runs the session of the cost
    """
    # Create the placeholders for "logits" (z) and "labels" (y) (approx. 2 lines)
    z = tf.placeholder(tf.float32, name="z")
    y = tf.placeholder(tf.float32, name="y")
    # Use the loss function
    cost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
    # Create a session
    sess = tf.Session()
    # Run the session
    cost = sess.run(cost, feed_dict={z:logits, y:labels})
    # Close the session
    sess.close()

    return cost
```
调用
```
logits = sigmoid(np.array([0.2,0.4,0.7,0.9]))
cost = cost(logits, np.array([0,0,1,1]))
print ("cost = " + str(cost))
```
输出
```
cost = [ 1.00538719  1.03664088  0.41385433  0.39956614]
```

from OpenSSL import crypto

cert_file = 'license.crt'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
subject = cert.get_subject()
issued_to = subject.CN    # the Common Name field
issuer = cert.get_issuer()
issued_by = issuer.CN

print(issued_to)
print(issued_by)
print(cert.get_notAfter().title())
print(cert.get_notBefore().title())
print(cert.get_signature_algorithm().title())
print((cert.get_pubkey()))

#
# import tensorflow as tf
# from numpy.random import RandomState
#
#
# class Study1:
#     #常亮初始化
#     global_step = tf.Variable(0)
#     learn_rate = tf.train.exponential_decay(learning_rate=0.01, global_step=global_step, decay_steps=100, decay_rate=0.96, staircase=True) #决定传播算法的每次迭代优化幅度,这里使用指数衰减学习率，通过迭代次数变化逐步减小学习率已达到更好的收敛效果
#     batch_size = 8
#     #参数初始化
#     w1 = tf.Variable(tf.random_normal(shape=(2,3), stddev=1, seed = 1))
#     w2 = tf.Variable(tf.random_normal(shape=(3,1), stddev=1, seed = 1))
#     #输入数据占位符定义
#     x = tf.placeholder(dtype=tf.float32, shape=(None, 2), name='x-input')
#     y_ = tf.placeholder(dtype=tf.float32, shape=(None,1), name='y-input')
#     #层间运算定义
#     a = tf.matmul(x,w1)
#     y = tf.matmul(a,w2)
#     #定义损失函数及参数优化算法
#     y = tf.sigmoid(y)
#     cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))+ (1-y_)*tf.log(tf.clip_by_value(1-y, 1e-10,1.0)))
#     #cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_, logits=y)
#     train_step = tf.train.GradientDescentOptimizer(learn_rate).minimize(cross_entropy,global_step=global_step)
#     #生成测试数据
#     rdm = RandomState(1)
#     dataset_size = 128
#     X = rdm.rand(dataset_size, 2)
#     Y = [[int(x1+x2<1)] for (x1, x2) in X] #很聪明的标注值生成办法
#     #配置回话及执行网络
#     config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True) #无gpu可用自动使用cpu;记录节点所在设备日志
#     with tf.Session(config=config) as sess:
#         #初始化所有变量
#         init_opt = tf.global_variables_initializer()
#         sess.run(init_opt)
#         #
#         STEP = 5000
#         for i in range(STEP):
#             start = i * batch_size % dataset_size #聪明的窗口滑动办法
#             end = min(start+batch_size, dataset_size)
#             sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]}) #feed_dict传入每一批次的训练数据，属性名对应上面的占位符变量
#             if i % 1000 ==0:
#                 totol_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
#                 print("After %d training step(s), cross entropy on all data is %g and learning_rate is %g",(i, totol_cross_entropy, learn_rate))
#
#
# class Study2:
#
#     def get_weight(self, shape, lamba):
#         v = tf.Variable(tf.random_normal(shape=shape), dtype=tf.float32)
#         tf.add_to_collection('losses', tf.contrib.layers.l2_regularizer(lamba)(v))
#         return v
#


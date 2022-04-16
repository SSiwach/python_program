class Activation_Softmax:
  def forward(self, inputs):

    exp_values = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))

    probablities = exp_values / np.sum(exp_values, axis = 1, keepdims = True)

    self.output = probablities

softmax = Activation_Softmax()

softmax.forward([[1,2,3]])

print(softmax.output)

softmax.forward([[-2,-1,0]])
print(softmax.output)

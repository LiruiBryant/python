import jax.numpy as np
from jax import grad, jit, vmap
from functools import partial


def predict(params, inputs):
    for W, b in params:
        outputs = np.dot(inputs, W) + b
        inputs = np.tanh(outputs)
    return outputs


def logprob_fun(params, inputs, targets):
    preds = predict(params, inputs)
    return np.sum((preds - targets) ** 2)


# compiled gradient evaluation function
grad_fun = jit(grad(logprob_fun))
# fast per-example grads
perex_grads = jit(vmap(grad_fun, in_axes=(None, 0, 0)))

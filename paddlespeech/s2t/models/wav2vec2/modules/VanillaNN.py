# Authors
# * Elena Rastorgueva 2020
# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Modified from speechbrain(https://github.com/speechbrain/speechbrain/blob/develop/speechbrain/lobes/models/VanillaNN.py).
import paddle

from paddlespeech.s2t.models.wav2vec2.modules import containers
from paddlespeech.s2t.models.wav2vec2.modules import linear


class VanillaNN(containers.Sequential):
    """A simple vanilla Deep Neural Network.
    Arguments
    ---------
    activation : paddle class
        A class used for constructing the activation layers.
    dnn_blocks : int
        The number of linear neural blocks to include.
    dnn_neurons : int
        The number of neurons in the linear layers.
    Example
    -------
    >>> inputs = paddle.rand([10, 120, 60])
    >>> model = VanillaNN(input_shape=inputs.shape)
    >>> outputs = model(inputs)
    >>> outputs.shape
    paddle.shape([10, 120, 512])
    """

    def __init__(
            self,
            input_shape,
            activation=paddle.nn.LeakyReLU,
            dnn_blocks=2,
            dnn_neurons=512, ):
        super().__init__(input_shape=input_shape)

        for block_index in range(dnn_blocks):
            self.append(
                linear.Linear,
                n_neurons=dnn_neurons,
                bias=True,
                layer_name="linear", )
            self.append(activation(), layer_name="act")

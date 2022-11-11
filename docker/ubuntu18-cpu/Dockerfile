FROM registry.baidubce.com/paddlepaddle/paddle:2.2.2
LABEL maintainer="paddlesl@baidu.com"

RUN apt-get update 
RUN apt-get install -y libsndfile-dev 
RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/PaddlePaddle/PaddleSpeech.git /home/PaddleSpeech  
RUN pip3 uninstall mccabe -y ; exit 0;
RUN pip3 install multiprocess==0.70.12 importlib-metadata==4.2.0 dill==0.3.4

WORKDIR /home/PaddleSpeech/
RUN python setup.py bdist_wheel
RUN pip install dist/*.whl 

CMD ['bash']

FROM python:3.6.8
WORKDIR /new_work_dir
ADD dnn_model /new_work_dir
COPY dnn_model .
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg' \
 'libsm6'\
 'libxext6' -y
RUN pip3 install --upgrade pip
RUN pip3 install opencv-python-headless==4.6.0.66 numpy requests 'fastapi[all]'


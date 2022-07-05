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
#ADD . /new_work_dir
#RUN apt-get update && apt-get install -y \
#opencv-python-headless
#python3-opencv \
#libsm6 \
#ffmpeg \
#libxext6 \
#libgl1
#libgl1-mesa-glx \ 
#libopencv-dev \
#libjpeg-dev \
#libpng-dev 

#RUN pip install --upgrade pip uvicorn "fastapi[all]" requests opencv-contrib-python opencv-python

#RUN pip install --upgrade pip "fastapi[all]" requests opencv-python-headless

#COPY . /new_work_dir/

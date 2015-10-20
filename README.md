0x01
==

    # apt-get install apache2 php5 libapache2-mod-php5
    # apt-get install libjpeg-dev
    # apt-get install libv4l-dev
    # apt-get install install git fswebcam
    # wget http://terzo.acmesystems.it/download/webcam/mjpg-streamer.tar.gz
    # ln -s /usr/include/libv4l1-videodev.h /usr/include/linux/videodev.h
    # nano Makefile # Comment out the line below
    PLUGINS += input_gspcav1.so
    # cd mjpg-streamer
    

0x01
==

## Ubilinux, Picture Streaming

    # apt-get install apache2 php5 libapache2-mod-php5
    # apt-get install libjpeg-dev
    # apt-get install libv4l-dev
    # apt-get install install make git
    # apt-get install fswebcam
    # wget http://terzo.acmesystems.it/download/webcam/mjpg-streamer.tar.gz
    # ln -s /usr/include/libv4l1-videodev.h /usr/include/linux/videodev.h
    # nano Makefile # Comment out the line below
    PLUGINS += input_gspcav1.so
    # cd mjpg-streamer
    # make
    # ./mjpg_streamer -i "./input_uvc.so -f 15 -r 640x480" -o "./output_http.so -w ./www"
    # ./mjpg_streamer -i "./input_uvc.so -f 15 -r 1280x720" -o "./output_http.so -w ./www"
    # ./mjpg_streamer -i "input_uvc.so -y -n -f 30 -r 320x240" -o "output_http.so -p 8080 -n -w /www/webcam"
    

This repository consists of IoT based conditon monitoring system for induction motors.

It uses an MPU6050 sensor which is connected to an Arduino Nano board to send vibration data in frequency domain to Node.js server using HTTP

Python libraries used:
1. numpy
2. pandas
3. scipy
4. requests
5. matplotlib
6. serial

Vibration data is read from Arduino Serial using Python serial library and then is sent to node server using requests library.

NPM packages used can be found in package.json in "iotcms_deploy" directory

The website is being hosted on Heroku. Click <a href="iotcms.herokuapp.com">here/a>

For converting raw valuesfrom MPU6050 to acceleration values you can use [this](https://github.com/jrowberg/i2cdevlib/tree/master/Arduino/MPU6050) Arduino library. I am using a differenet one which I was unable to find at this moment.

Open up an issue or reach me @ vashishthmayur@gmail.com if you have any queries.


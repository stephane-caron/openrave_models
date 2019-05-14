## JAXON model for OpenRAVE

JAXON is a 33-DOF humanoid robot developed by the [Jouhou System Kougaku
(JSK)](http://www.jsk.t.u-tokyo.ac.jp/) laboratory of the University of Tokyo.
It is an extension of the
[HRP-2](http://global.kawada.jp/mechatronics/hrp2.html) biped, two copies of
which took part in the [DARPA Robotics
Challenge](http://www.theroboticschallenge.org/) in June 2015. Its VRML model
files were released during the [Japanese Virtual Robotics
Challenge](http://www.jvrc.org/). I have converted them to COLLADA using the
``openhrp-export-collada`` tool from
[openhrp3](https://github.com/fkanehiro/openhrp3).

You can download and display the robot model by:
```
$ git clone https://github.com/stephane-caron/openrave_models
$ cd openrave_models
$ python show_model.py JAXON
```
Mechanically, JAXON has has 8-DOF arms, 6-DOF legs and a 3-DOF torso:

<img src="https://scaron.info/images/openrave/jaxon.png" width="600">

This model is licensed under a [Creative Commons Attribution-ShareAlike 4.0
International License](http://creativecommons.org/licenses/by-sa/4.0/). 

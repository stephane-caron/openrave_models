## Romeo model for OpenRAVE

Romeo is a 37-DOF humanoid robot designed by [Aldebaran
Robotics](https://www.ald.softbankrobotics.com/). It is publicly distributed in
the [romeo\_description](http://wiki.ros.org/romeo_description>) package under
a BSD license. The official files are in URDF, which cannot be used directly in
OpenRAVE. Here is how to get an alternative COLLADA version:
```
$ git clone https://github.com/stephane-caron/openrave_models
$ cd openrave_models
$ python show_model.py Romeo
```
The robot appears in false colors as OpenRAVE doesn't read textures:

<img src="https://scaron.info/images/openrave/romeo.png" width="600">

This model is under the BSD license. The robot's kinematic and inertial
properties are publicly available in the [Romeo
documentation](https://projetromeo.com/documentation/).

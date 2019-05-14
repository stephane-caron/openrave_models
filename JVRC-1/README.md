## JVRC-1 model for OpenRAVE

The JVRC-1 is a 44-DOF humanoid model designed for the [Japanese Virtual
Robotics Challenge](http://www.jvrc.org/) by Takasuke Sonoyama. It is publicly
distributed in the [jvrc/model](https://github.com/jvrc/model) repository on
GitHub. The official files are in VRML, which cannot be used in OpenRAVE
directly. I have converted them to COLLADA using the ``openhrp-export-collada``
tool from [openhrp3](https://github.com/fkanehiro/openhrp3).

You can download and display the robot model by:

```
$ git clone https://github.com/stephane-caron/openrave_models
$ cd openrave_models
$ python show_model.py JVRC-1
```

The model is in false colors as OpenRAVE doesn't read textures:

<img src="https://scaron.info/images/openrave/jvrc-1.png" width="600">

The [license](http://www.jvrc.org/en/humanoid/JVRC-1/agreement.html) (Japanese
only) published on the JVRC website basically grants noncommercial use under
attribution. If you use it in your project, you can cite it as: "Sample
humanoid model for a simulation competition, Japanese National Institute of
Advanced Industrial Science and Technology, ref. H27PRO-1843"
(シミュレーション競技会用サンプルヒューマノイドモデル、産業技術総合研究所
H27PRO-1843).

Conveniently, JVRC-1 has roughly the same kinematic chain as HRP-4. See [its
interface in
pymanoid](https://github.com/stephane-caron/pymanoid/blob/master/pymanoid/robots/jvrc1.py)
for details.

#!/usr/bin/env python

"""
Load robot model with additional six DOFs for the floating base.
"""

import IPython
import openravepy
import os.path
import sys

free_flyer_xml = """
<environment>
    <robot>
        <kinbody>
            <body name="FLYER_TX_LINK">
                <mass type="mimicgeom">
                    <total>0</total>
                </mass>
            </body>
        </kinbody>
        <kinbody>
            <body name="FLYER_TY_LINK">
                <mass type="mimicgeom">
                    <total>0</total>
                </mass>
            </body>
        </kinbody>
        <kinbody>
            <body name="FLYER_TZ_LINK">
                <mass type="mimicgeom">
                    <total>0</total>
                </mass>
            </body>
        </kinbody>
        <kinbody>
            <body name="FLYER_ROLL_LINK">
                <mass type="mimicgeom">
                    <total>0</total>
                </mass>
            </body>
        </kinbody>
        <kinbody>
            <body name="FLYER_PITCH_LINK">
                <mass type="mimicgeom">
                    <total>0</total>
                </mass>
            </body>
        </kinbody>
        <kinbody>
            <body name="FLYER_YAW_LINK">
                <mass type="mimicgeom">
                    <total>0</total>
                </mass>
            </body>
        </kinbody>
        <robot file="%s" name="%s">
            <kinbody>
                <joint name="FLYER_TX" type="slider" circular="true">
                    <body>FLYER_TX_LINK</body>
                    <body>FLYER_TY_LINK</body>
                    <axis>1 0 0</axis>
                    <limits>-10 +10</limits>
                </joint>
                <joint name="FLYER_TY" type="slider" circular="true">
                    <body>FLYER_TY_LINK</body>
                    <body>FLYER_TZ_LINK</body>
                    <axis>0 1 0</axis>
                    <limits>-10 +10</limits>
                </joint>
                <joint name="FLYER_TZ" type="slider" circular="true">
                    <body>FLYER_TZ_LINK</body>
                    <body>FLYER_ROLL_LINK</body>
                    <axis>0 0 1</axis>
                    <limits>-10 +10</limits>
                </joint>
                <joint name="FLYER_ROLL" type="hinge" circular="true">
                    <body>FLYER_ROLL_LINK</body>
                    <body>FLYER_PITCH_LINK</body>
                    <axis>1 0 0</axis>
                </joint>
                <joint name="FLYER_PITCH" type="hinge" circular="true">
                    <body>FLYER_PITCH_LINK</body>
                    <body>FLYER_YAW_LINK</body>
                    <axis>0 1 0</axis>
                </joint>
                <joint name="FLYER_YAW" type="hinge" circular="true">
                    <body>FLYER_YAW_LINK</body>
                    <body>%s</body>
                    <axis>0 0 1</axis>
                </joint>
            </kinbody>
        </robot>
    </robot>
</environment>
"""

if __name__ == "__main__":
    if not sys.argv[-1].endswith('.dae'):
        print "Usage: %s model.dae" % sys.argv[0]
        sys.exit()
    elif not os.path.isfile(sys.argv[-1]):
        print "Could not open file %s" % sys.argv[-1]
        sys.exit()
    fpath = sys.argv[-1]
    name = os.path.basename(os.path.splitext(fpath)[0])
    root_body = \
        'BODY' if 'JAXON' in name else \
        'PELVIS_S' if 'JVRC' in name else \
        'base_link'  # for Romeo
    env = openravepy.Environment()
    env.LoadData(free_flyer_xml % (fpath, name, root_body))
    env.SetViewer('qtcoin')
    viewer = env.GetViewer()
    viewer.SetBkgndColor([.8, .85, .9])  # RGB tuple
    viewer.SetCamera(
        [[-0.6292849, 0.34538411, -0.69621141, 1.87324536],
         [0.7768542, 0.25382043, -0.57625753, 1.55049443],
         [-0.02231752, -0.90348492, -0.42803846, 1.20491762],
         [0., 0., 0., 1.]])
    robot = env.GetRobots()[0]
    if IPython.get_ipython() is None:
        IPython.embed()

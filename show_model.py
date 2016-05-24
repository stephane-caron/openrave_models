#!/usr/bin/env python

import IPython
import openravepy
import os
import sys


if __name__ == "__main__":
    dirs = sorted([
        os.path.basename(d) for d in os.listdir('.')
        if os.path.isdir(d) and d[0] != '.'])
    if len(sys.argv) < 2 or sys.argv[1] not in dirs:
        print "Usage: %s [%s]" % (sys.argv[0], '|'.join(dirs))
        exit(0)
    env = openravepy.Environment()
    env.Load('%s/env.xml' % sys.argv[1])
    env.SetViewer('qtcoin')
    viewer = env.GetViewer()
    viewer.SetBkgndColor([.8, .85, .9])  # RGB tuple
    viewer.SetCamera(
        [[-0.6292849, 0.34538411, -0.69621141, 1.87324536],
         [0.7768542, 0.25382043, -0.57625753, 1.55049443],
         [-0.02231752, -0.90348492, -0.42803846, 1.20491762],
         [0., 0., 0., 1.]])
    robot = env.GetRobots()[0]
    IPython.embed()

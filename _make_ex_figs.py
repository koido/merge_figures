#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import module
import cv2
import numpy as np

# make exmaple figures
max_i = 50
for i in range(max_i):
    img = np.full((250, 400, 3), 255, np.uint8)
    cv2.line(img, (0, 0), (400, 250), (0, 0, i * 5), 10)
    cv2.putText(img, 'example %s' % (i + 1),
                org=(0, 50),
                fontFace=cv2.FONT_HERSHEY_PLAIN,
                fontScale=4, color=(0, 0, 0),
                thickness=5, lineType=cv2.LINE_AA)
    cv2.imwrite('./example/input/ex%02d.jpg' % (i + 1), img)

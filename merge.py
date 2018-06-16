#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import module
import cv2
import sys
import numpy as np
import argparse

# get arguments
parser = argparse.ArgumentParser(
    description='Merge figures in a tiff figure. Size of the merging figures must be the same. Size of the merged figure is {(height of inputs[0]) * nrow, {width of inputs[0]) * ncol}.')
parser.add_argument('-o', '--output', required=True, type=str,
                    help='Output file name. Automatically add suffix.')
parser.add_argument('-i', '--inputs', required=True,
                    type=str, nargs='*', help='Input files. According to the order, input files are merged.')
parser.add_argument('-r', '--nrow', default=3, type=int,
                    help='Number of row of figure.')
parser.add_argument('-c', '--ncol', default=3, type=int,
                    help='Number of col of figure.')
args = parser.parse_args()
# print(args)

inputs = args.inputs
output = args.output
nrow = args.nrow
ncol = args.ncol

# image merge


def main(inputs, output, nrow, ncol):
    # open image
    img = []
    for i in range(0, len(inputs)):
        img.append(cv2.imread(inputs[i]))

    # get size of the first element of the inputs
    base_h = img[0].shape[0]
    base_w = img[0].shape[1]
    img_blank = np.full((base_h, base_w, 3), 255, np.uint8)

    # get number of canvas
    q, mod = divmod(len(inputs), nrow*ncol)
    if mod != 0:
        q += 1

    # concat
    indx_fig = 0
    for i in range(0, q):

        # new canvas and output name
        out_file = output + '_no' + str(i + 1) + '.tiff'

        # paste figure
        for _row in range(0, nrow):
            for _col in range(0, ncol):

                # exception -> bind blank image
                if len(img) == indx_fig:
                    img.append(img_blank)
                # concat
                if _col == 0:
                    _im = img[indx_fig]
                else:
                    _im = cv2.hconcat([_im, img[indx_fig]])
                indx_fig += 1
            if _row == 0:
                __im = _im
            else:
                __im = cv2.vconcat([__im, _im])
            del _im
        cv2.imwrite(out_file, __im)


if __name__ == '__main__':
    main(inputs, output, nrow, ncol)

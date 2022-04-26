#!/bin/bash

# cp optdigits_tra.dat D.dat
# cp optdigits_cv.dat D_cv.dat

cp optdigits_tra_trans.dat D.dat
cp optdigits_cv_trans.dat D_cv.dat

sed -e "s/^nunits = .*/nunits = $1;/;s/^maxT = .*/maxT = $2;/;s/^alpha = .*/alpha = $3;/;s/^change_thresh = .*/change_thresh = $4;/;s/^change_err_thresh = .*/change_err_thresh = $5;/;" learn_nnet_template.m > learn_nnet.m

octave -q learn_nnet.m
##to extract loss、lr in training interations and accuracy、loss in test interations
##from logs
import sys
import os
import re
import random
import copy
import string

fileList=os.listdir('./')
fileList.remove('caffe.INFO')
fileList.remove('result_base_lr.py')
#fileList.remove('caffe.k20-2.jiadan.log.INFO.20160413-023557.27974')
print fileList,len(fileList)
for f in fileList:
    logh=open(f)
    lineList=logh.readlines()
    logh.close()
    result_dict={}
    k=0
    print f
    result_train=[]
    result_test=[]
    for line in lineList:
        if line.find('base_lr')!=-1:
            result_dict['base_lr']=re.search(r'\d+\.?\d*e?\+?-?\d*',line).group()
            print result_dict['base_lr']
        #extract train results
        elif (line.find('Iteration')!=-1)&(line.find('loss =')!=-1):
            val_train=[]
            line=line.split(']')[1]
            #iter_train=re.search(r'\d+',line).group()
            iter_train=re.split(' |, | = ',line.strip('\n'))[2]
            #val_loss_train=re.search(r'\d+\.\d*e?\+?-?\d*',line).group()
            val_loss_train=re.split(' |, | = ',line.strip('\n'))[5]
        elif (line.find('Iteration')!=-1)&(line.find('lr =')!=-1):
            line=line.split(']')[1]
            #iter_train1=re.search(r'\d+',line).group()
            iter_train1=re.split(' |, | = ',line.strip('\n'))[2]
           # print iter_train1
            #val_lr_train=re.search(r'\d+\.\d*e?\+?-?\d*',line).group()
            val_lr_train=re.split(' |, | = ',line.strip('\n'))[5]
            if iter_train==iter_train1:
                val_train.append(iter_train)
                val_train.append(val_loss_train)
                val_train.append(val_lr_train)
                result_train.append(val_train)
    #            print val_train
        #extract test results
        elif (line.find('Iteration')!=-1)&(line.find('Testing net')!=-1):
     #       print 3,line
            val_test=[]
            line=line.split(']')[1]
            iter_test=re.search(r'\d+',line).group()
            val_test.append(iter_test)
            nextline=lineList[k+1]
            nextline=nextline.split(']')[1]
            val_accu=re.search(r'\d+\.\d*e?\+?-?\d*',nextline).group()
            val_test.append(val_accu)
            nextline=lineList[k+2]
            nextline=nextline.split(']')[1]
            val_loss=re.search(r'\d+\.\d*e?\+?-?\d*',nextline).group()
            val_test.append(val_loss)
            result_test.append(val_test)
    #        print val_test
        k=k+1

    fname_w='../result/base_lr/base_lr_'+result_dict['base_lr']
    if os.path.exists(fname_w):
        os.remove(fname_w)
    fh_w=open(fname_w,'a')
    fh_w.writelines(f)
    fh_w.write('\n')
    fh_w.writelines('base_lr =:'+result_dict['base_lr'])
    fh_w.write('\n')
    fh_w.writelines('result_train\n')
    for rl in result_train:
        fh_w.writelines('\t'.join(rl))
        fh_w.write('\n')
    fh_w.writelines('result_test\n')
    for rl in result_test:
        fh_w.writelines('\t'.join(rl))
        fh_w.write('\n')
    fh_w.close()

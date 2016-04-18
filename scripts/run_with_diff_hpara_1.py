#run train_lenet.sh with diffrent hyper-parameter settings,hyper-parameters include base_lr、
#momentum、weight_decay、gamma、power，whose ranges are define in a .txt file.
import sys

import os
import re
import random
import copy
import string
import re

fh_para = open('para_range.txt','r')
flist_para = fh_para.readlines()
fh_para.close()
k=0
para_dict={}

for item in flist_para:
    if item.find('base_lr')!=-1:
        print(item)
        tmp=flist_para[k+1];
        para_dict['base_lr']=list(eval(tmp))
    if item.find('momentum')!=-1:
        print(item) 
        tmp=flist_para[k+1];
        para_dict['momentum']=list(eval(tmp))
    if item.find('weight_decay')!=-1:
        print(item) 
        tmp=flist_para[k+1];
        para_dict['weight_decay']=list(eval(tmp))
    if item.find('gamma')!=-1:
        print(item) 
        tmp=flist_para[k+1];
        para_dict['gamma']=list(eval(tmp))
    if item.find('power')!=-1:
        print(item) 
        tmp=flist_para[k+1];
        para_dict['power']=list(eval(tmp))
    k=k+1 
for key in para_dict: 
    print key,para_dict[key]
    print type(para_dict[key])
fname = sys.argv[1]
fh = open(fname,'r')
flist = fh.readlines()
fh.close()
k=0

replace_reg=re.compile(r'0.\d+')
for key in para_dict:
    print key,para_dict[key]
    if key=='#base_lr':
        for para_iter in para_dict[key]:
            fk=0
            for item in flist:
                if item.find('base_lr')!=-1:
                    print para_iter,type(para_iter)
                    item=replace_reg.sub('%f' % para_iter,item)
                    print item,para_iter
                    flist[fk]=item
                fk=fk+1
            fh=open(fname,'w')
            fh.writelines(flist)
            fh.close()
            # run 
            os.system('./train_lenet_base_lr.sh')
#---reset to default value base_lr
        fh=open(fname,'r')
        flist = fh.readlines()
        fh.close()
        fk=0
        for item in flist:
            if item.find('base_lr')!=-1:
                print para_iter,type(para_iter)
                item=replace_reg.sub('%f' % 0.01,item)
                print item,para_iter
                flist[fk]=item
            fk=fk+1
        fh=open(fname,'w')
        fh.writelines(flist)
        fh.close()

    if key=='momentum':
        for para_iter in para_dict[key]:
            fk=0
            for item in flist:
                if item.find('momentum')!=-1:
                    print para_iter,type(para_iter)
                    item=replace_reg.sub('%f' % para_iter,item)
                    print item,para_iter
                    flist[fk]=item
                fk=fk+1
            fh=open(fname,'w')
            fh.writelines(flist)
            fh.close()
            # run 
            os.system('./train_lenet_momentum.sh')

#---reset to default value momentum
        fh=open(fname,'r')
        flist = fh.readlines()
        fh.close()
        fk=0
        for item in flist:
            if item.find('momentum')!=-1:
                print para_iter,type(para_iter)
                item=replace_reg.sub('%f' % 0.9,item)
                print item,para_iter
                flist[fk]=item
            fk=fk+1
        fh=open(fname,'w')
        fh.writelines(flist)
        fh.close()
    if key=='weight_decay':
        for para_iter in para_dict[key]:
            fk=0
            for item in flist:
                if item.find('weight_decay')!=-1:
                    print para_iter,type(para_iter)
                    item=replace_reg.sub('%f' % para_iter,item)
                    print item,para_iter
                    flist[fk]=item
                fk=fk+1
            fh=open(fname,'w')
            fh.writelines(flist)
            fh.close()
            # run 
            os.system('./train_lenet_weight_decay.sh')
#---reset to default value weight_decay
        fh=open(fname,'r')
        flist = fh.readlines()
        fh.close()
        fk=0
        for item in flist:
            if item.find('weight_decay')!=-1:
                print para_iter,type(para_iter)
                item=replace_reg.sub('%f' % 0.0005,item)
                print item,para_iter
                flist[fk]=item
            fk=fk+1
        fh=open(fname,'w')
        fh.writelines(flist)
        fh.close()

    if key=='#gamma':
        for para_iter in para_dict[key]:
            fk=0
            for item in flist:
                if item.find('gamma')!=-1:
                    print para_iter,type(para_iter)
                    item=replace_reg.sub('%f' % para_iter,item)
                    print item,para_iter
                    flist[fk]=item
                fk=fk+1
            fh=open(fname,'w')
            fh.writelines(flist)
            fh.close()
            # run 
            os.system('./train_lenet_gamma.sh')
#---reset to default value gamma
        fh=open(fname,'r')
        flist = fh.readlines()
        fh.close()
        fk=0
        for item in flist:
            if item.find('gamma')!=-1:
                print para_iter,type(para_iter)
                item=replace_reg.sub('%f' % 0.0001,item)
                print item,para_iter
                flist[fk]=item
            fk=fk+1
        fh=open(fname,'w')
        fh.writelines(flist)
        fh.close()

    if key=='#power':
        for para_iter in para_dict[key]:
            fk=0
            for item in flist:
                if item.find('power')!=-1:
                    print para_iter,type(para_iter)
                    item=replace_reg.sub('%f' % para_iter,item)
                    print item,para_iter
                    flist[fk]=item
                fk=fk+1
            fh=open(fname,'w')
            fh.writelines(flist)
            fh.close()
            # run 
            os.system('./train_lenet_power.sh')
#---reset to default value power
        fh=open(fname,'r')
        flist = fh.readlines()
        fh.close()
        fk=0
        for item in flist:
            if item.find('power')!=-1:
                print para_iter,type(para_iter)
                item=replace_reg.sub('%f' % 0.75,item)
                print item,para_iter
                flist[fk]=item
            fk=fk+1
        fh=open(fname,'w')
        fh.writelines(flist)
        fh.close()

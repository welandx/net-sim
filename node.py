#!/usr/bin/env python3
class node:
    def __init__(self,num):
        self.active=[0 for i in range(num)]

    def gen_message(self,ID):
        self.active[ID]=1
    
    def send(self,ID):
        self.active[ID]=0

    def get_status(self,ID):
        return self.active[ID]

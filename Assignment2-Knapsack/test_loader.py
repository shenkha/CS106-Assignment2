import re
import os
from os.path import join,isfile


def list_dir(path):
    return [f for f in os.listdir(path)]

#print(list_dir("test_case"))

class test_loader:
    def __init__(self,root):
        self.root = root
    
    def load_types(self):
        dirs = list_dir(self.root)
        self.types = dirs
        return self.types

    def set_type(self,type_tmp):
        self.type = type_tmp

    def get_type(self):
        return self.type

    def load_sizes(self):
        dirs = list_dir(join(self.root,self.type))
        self.sizes = [d for d in dirs]
        return self.sizes

    def set_size(self,size_tmp):
        self.size = size_tmp

    def get_size(self):
        return self.size
    
    def load_ranges(self):
        dirs = list_dir(join(self.root,self.type,self.size))
        self.ranges = [d for d in dirs]
        return self.ranges
    
    def set_range(self,range_tmp):
        self.range = range_tmp
    
    def get_range(self):
        return self.range
    
    def load_tests(self):
        dirs = list_dir(join(self.root,self.type,self.size,self.range))
        self.tests = [d for d in dirs]
        #self.tests = self.tests[0:3]
        self.tests = self.tests[0:2]
        return self.tests
    
    def set_test(self,test_tmp):
        self.test = test_tmp

    def get_test(self):
        return self.test

    def read_kp_file(self):
        file_path = join(self.root,self.type,self.size,self.range,self.test)
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        n = int(lines[1].strip())
        c = int(lines[2].strip())
        
        values = []
        weights = []
        for i in range(4, n+4):
            p, w = map(int, lines[i].strip().split())
            values.append(p)
            weights.append(w)
        
        return n, c, values, [weights]
    
    def get_all_info(self):
        info = dict()

        info['type'] = self.type
        info['size'] = self.size
        info['range'] = self.range
        info['test'] = self.test

        return info



#test = test_loader("test_case")
#for t in test.load_types():
#    test.set_type(t)
#    for s in test.load_sizes():
#        test.set_size(s)
#        for r in test.load_ranges():
#            test.set_range(r)
#            for i in test.load_tests():
#                test.set_test(i)
#                info = test.get_all_info()
#print(info)
            

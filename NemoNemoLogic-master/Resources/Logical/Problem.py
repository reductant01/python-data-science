############
#Start here#
############
import numpy as np

class Problem():
    def __init__(self, arr, size=16):
        # size must be in [8, 16, 32]
        self.size = size
        self.pixel_size = 1024//self.size
        self.origin_arr = arr
        self.ans_arr = np.ones((self.size, self.size))
        self.preview = np.ones((1024,1024,3))*255
        self.calc_answer()

    def calc_answer(self):
        for x in range(self.size):
            for y in range(self.size):
                temp_arr = self.origin_arr[self.pixel_size*x:self.pixel_size*(x+1), self.pixel_size*y:self.pixel_size*(y+1),:]
                temp_arr_layer = temp_arr[:,:,-1].astype(np.uint)//255
                if temp_arr_layer.sum() <= (self.pixel_size**2)//2:
                    self.ans_arr[x,y] = 0
                    self.preview[self.pixel_size*x:self.pixel_size*(x+1), self.pixel_size*y:self.pixel_size*(y+1),:] = 0
##########
#End here#
##########
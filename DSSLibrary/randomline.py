import random
import numpy as np
class dss_random_line():
    def __init__(self, dss):
        self = self.set_dss(dss)
        self = self.__set_numberoflines()
        self = self.__set_numberoflinetypes()
    def set_dss(self,dss):
        self.dss = dss
        return self
    def __set_numberoflines(self):
        self.__numberoflines = self.dss.lines_count()
        return self
    def __set_numberoflinetypes(self):
        self.__numberoflinetypes = self.dss.linecodes_count()
        return self        
    def NumberOfLineTypes(self):
        return self.__numberoflinetypes
    def NumberOfLines(self):
        return self.__numberoflines
    def random_int_allocation(self):
        random_lines      = [random.randint(1,self.NumberOfLineTypes()) for k in range(self.NumberOfLines())]
        return random_lines
    def random_bin_allocation(self):
        xb = [np.binary_repr(x,self.NumberOfLineTypes()) for x in self.random_int_allocation()]
        return "".join(xb)
    def dec2bin(self,xd):
        xb = [np.binary_repr(x,self.NumberOfLineTypes()) for x in xd]
        return "".join(xb)
    def bin2dec(self,xb):
        self   = self._set_xb(xb)
        self   = self._set_Nbits()
        self   = self._set_bit_start_pointers()
        self   = self._set_bit_end_pointers()
        return self._convert_bin2dec()
    def _set_Nbits(self):
        self._Nbits =  len(self._xb)
        return self
    def _set_Nint(self):
        self._Nint = len(self._bit_start_pointers)
        return self
    def _set_xb(self,xb):
        self._xb = xb
        return self
    def _set_bit_start_pointers(self):
        self._bit_start_pointers     = np.arange(0, self._Nbits, self.NumberOfLineTypes())
        self._bit_start_pointers[1:] = self._bit_start_pointers[1:]+1
        return self
    def _set_bit_end_pointers(self):
        self._bit_end_pointers = np.arange(self.NumberOfLineTypes(), self._Nbits+self.NumberOfLineTypes(), self.NumberOfLineTypes());
        return self
    def _convert_bin2dec(self):
        xd=[]
        for line in range(self.NumberOfLines()):
            xd.append(
                int(self._xb[self._bit_start_pointers[line]:self._bit_end_pointers[line]],2)
                )
        return xd       
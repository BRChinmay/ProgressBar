from time  import sleep
class progressbar :
    ncol = 13
    def __init__(self,iterable):
        self._iterable = iterable
        self._n = len(iterable)
        self._i = 0
        self._frac = float(self._i/self._n)
        self._rjust = int(self._frac * progressbar.ncol)
        print(''.join(['[', ''.rjust(progressbar.ncol,'|'), ']', str(int(self._frac*100)).rjust(3,' '),'%'] ) ,end="")

    def __iter__(self) :
        iterable = self._iterable
        try :
            for obj in iterable :
                yield obj
                self._i += 1 
                self._frac = float(self._i/self._n)
                self._rjust = int(self._frac*progressbar.ncol)
                print(''.join(['\r','[','>'.rjust(self._rjust+1,'='),''.ljust(progressbar.ncol-self._rjust-1,'|'),']',str(int(self._frac*100)).rjust(3,' '),'%']),end="")
        finally :
            print('\n')
#            self.close()

if __name__ == "__main__":
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in progressbar(l) :
        sleep(0.2)

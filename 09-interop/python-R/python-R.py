from numpy import *
import scipy as sp
from pandas import *
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import rpy2

from rpy2.robjects import pandas2ri
pandas2ri.activate()

ro.r('x=c()')
ro.r('x[1]=22')
ro.r('x[2]=44')
print(ro.r('x'))

# mtcars

ro.r('data(mtcars)')

from rpy2.robjects import r
r.data('mtcars')
print(r['mtcars'].head())

# let's do an lm on mtcars
ro.r('''fit=lm(mpg ~ wt + cyl, data=mtcars)''')
print(ro.r('summary(fit)'))


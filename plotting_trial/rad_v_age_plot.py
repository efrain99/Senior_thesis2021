#plotting program for radius vs age using history output file

import pylab as pb
import mesa_reader as mr
import numpy as np

#Importing history output file
m = mr.MesaData('/home/ecp5kf/whitedwarfs/plottingtrial/LOGS_to_wd/history.data')

#convert age data into log scale
age = m.star_age
rad = m.log_R
log_age = np.log(age)

#plotting stuff
pb.plot(log_age,rad)

pb.title('Radius vs Age using History Output')
pb.xlabel('Age')
pb.ylabel('Radius[M] ')
pb.savefig('rad_v_age.pdf')

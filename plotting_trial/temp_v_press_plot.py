#plotting Tempurature vs Pressure

import pylab as pb
import mesa_reader as mr

#Use mesa_reader to import data and extract params
h = mr.MesaData('/home/ecp5kf/whitedwarfs/plottingtrial/LOGS_to_wd/profile1.data')
pb.loglog(h.pressure,h.temperature)

pb.title('Tempurature vs. Pressure')
pb.xlabel('Pressure')
pb.ylabel('Tempurature')

pb.savefig("tvsp.pdf")

import ephem
import Dynamixel


target=[1.0,1.0] #alt,az in radians



f = open('DateTimeLoc.txt', 'r')
datetimeloc=f.readline().rstrip('\n').split(',')
# 0-date; 1-time; 2-lat; 3-lon; 4-elevation, 5-temp
f.close()

for i in xrange(24):
    hour=str(i).zfill(2)
    time=hour+":00:00"


    gatech = ephem.Observer()
    gatech.date = datetimeloc[0]+' '+time #'1984/5/30 16:22:56'
    gatech.lat = datetimeloc[2]  #'33.775867'
    gatech.lon = datetimeloc[3] #'-84.39733'

    gatech.elevation = int(datetimeloc[4])
    gatech.temp = float(datetimeloc[5])

    sol_obj = ephem.Sun(gatech)
    sol=[sol_obj.alt, sol_obj.az]

    icarus_desired=[0.5*target[0]+0.5*sol[0],0.5*target[1]+0.5*sol[1]]
    print('%s %s %s %f %f' % (time, sol_obj.alt, sol_obj.az,icarus_desired[0],icarus_desired[1]))


movedyn(400,400)
resetdyn()
import ephem
import helios_functions as hf 
import time as t

target=[1.0,1.0] #alt,az in radians

rad2deg=180./3.14159


f = open('DateTimeLoc.txt', 'r')
datetimeloc=f.readline().rstrip('\n').split(',')
# 0-date; 1-time; 2-lat; 3-lon; 4-elevation, 5-temp
f.close()

print "Date:", datetimeloc[0]
print "Time:", datetimeloc[1]
print "Lat:", datetimeloc[2]
print "Lon:", datetimeloc[3]
print "Ele:", datetimeloc[4]
print "Temp:", datetimeloc[5]



for i in xrange(200):
    hour=str(i).zfill(2)
    time=hour+":00:00"


    gatech = ephem.Observer()
    gatech.date = '2015/09/12 00:57:00' #datetimeloc[0]+' '+time #'1984/5/30 16:22:56'
    gatech.lat = '37.77648' #datetimeloc[2]  #'33.775867'
    gatech.lon = '-122.41755' #datetimeloc[3] #'-84.39733'

    gatech.elevation = int(datetimeloc[4])
    gatech.temp = float(datetimeloc[5])

    sol_obj = ephem.Sun(gatech)
    sol=[sol_obj.alt, sol_obj.az]

    #icarus_desired=[0.5*target[0]+0.5*sol[0],0.5*target[1]+0.5*sol[1]]
    #print('%s %s %s %f %f' % (time, sol_obj.alt, sol_obj.az,icarus_desired[0],icarus_desired[1]))
    
    sol_alt=sol[0]*rad2deg
    sol_az=sol[1]*rad2deg

    print('%s %s %s %i %i' % (time, sol_obj.alt, sol_obj.az,hf.alt_to_pos2(sol_alt),hf.az_to_pos1(sol_az)))

    if(hf.az_to_pos1(sol_az) >= 205 and hf.az_to_pos1(sol_az) <= 819):
        if(hf.alt_to_pos2(sol_alt) >= 205 and hf.alt_to_pos2(sol_alt) <= 819): 
            hf.movedyn(hf.az_to_pos1(sol_az),hf.alt_to_pos2(sol_alt))
            t.sleep(2)
	    

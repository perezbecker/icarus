import ephem
import helios_functions as hf 
import time as t
import datetime

target=[1.570795,3.14159] #alt,az in radians

rad2deg=180./3.14159

print "Obtaining GPS data"
j=0
while j<1: 
    datetimeloc=hf.get_gps()
    if(datetimeloc[0] != "No data" and datetimeloc[1] != "No data" and datetimeloc[2] != "No data"):
        print "GPS sync successful"
        j=1
    else:
        j=0


# GET DateTimeLoc FROM FILE
# f = open('DateTimeLoc.txt', 'r')
# datetimeloc=f.readline().rstrip('\n').split(',')
# # 0-date; 1-time; 2-lat; 3-lon; 4-elevation, 5-temp
# f.close()
# 
# print "Date:", datetimeloc[0]
# print "Time:", datetimeloc[1]
# print "Lat:", datetimeloc[2]
# print "Lon:", datetimeloc[3]
# print "Ele:", datetimeloc[4]
# print "Temp:", datetimeloc[5]


gps_datetime=datetime.datetime.strptime(str(datetimeloc[0]), "%Y-%m-%dT%H:%M:%S.%fZ")
gps_lat=datetimeloc[1]
gps_lon=datetimeloc[2]
gps_alt=datetimeloc[3]

print "DateTime:",gps_datetime.strftime("%Y/%m/%d %H:%M:%S"),"Lat: ",str(gps_lat),"Lon:",str(gps_lon),"Alt:",str(gps_alt)

for i in xrange(1):
    #hour=str(i).zfill(2)
    #time=hour+":00:00"


    gatech = ephem.Observer()
    gatech.date = gps_datetime.strftime("%Y/%m/%d %H:%M:%S") #datetimeloc[0]+' '+time #'1984/5/30 16:22:56'
    gatech.lat =  str(gps_lat) #'37.77648' #datetimeloc[2]  #'33.775867'
    gatech.lon =  str(gps_lon) #'-122.41755' #datetimeloc[3] #'-84.39733'

    gatech.elevation = gps_alt
    gatech.temp = 23.0 #float(datetimeloc[5])


    sol_obj = ephem.FixedBody()
    sol_obj._ra = 2.50
    sol_obj._dec = 89.25
    sol_obj.compute(gatech)



    #sol_obj = ephem.Polaris(gatech)
    sol=[sol_obj.alt, sol_obj.az]

    icarus_desired=[0.5*target[0]+0.5*sol[0],0.5*target[1]+0.5*sol[1]]
    #print('%s %s %s %f %f' % (time, sol_obj.alt, sol_obj.az,icarus_desired[0],icarus_desired[1]))
    
    sol_alt=sol[0]*rad2deg
    sol_az=sol[1]*rad2deg
    
    icarus_alt=icarus_desired[0]*rad2deg
    icarus_az=icarus_desired[1]*rad2deg
    

    #print('%s %s %s %i %i' % (time, sol_obj.alt, sol_obj.az,hf.alt_to_pos2(sol_alt),hf.az_to_pos1(sol_az)))

    # if(hf.az_to_pos1(sol_az) >= 1 and hf.az_to_pos1(sol_az) <= 1023):
    #     if(hf.alt_to_pos2(sol_alt) >= 205 and hf.alt_to_pos2(sol_alt) <= 819): 
    #         hf.movedyn(hf.az_to_pos1(sol_az),hf.alt_to_pos2(sol_alt))
    #         t.sleep(5)
    
    if(hf.az_to_pos1(icarus_az) >= 1 and hf.az_to_pos1(icarus_az) <= 1023):
        if(hf.alt_to_pos2(icarus_alt) >= 205 and hf.alt_to_pos2(icarus_alt) <= 819): 
            hf.movedyn(hf.az_to_pos1(icarus_az),hf.alt_to_pos2(icarus_alt))
            t.sleep(5)
	    

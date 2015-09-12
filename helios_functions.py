import time as ti
import Dynamixel as dm
import gps
from subprocess import call


call(["sudo", "killall", "gpsd"])
call(["sudo", "gpsd", "/dev/ttyAMA0","-F","/var/run/gpsd.sock"])


READDATA = 2
WRITE_DATA = 3


def resetdyn():
    
    #Reset Dynamixel 2
    
    speed = 100
    ID = 2
    SPEED_REG = 32
    POS_REG = 30
    positions_delay = list([(512,2)])
    ax12 = dm.dynamixel()
    #test serial ports
    #print ax12.port.test_ports()
    #test motors
    #print "moving dynamixel"
    ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
    #test that the speed is set corectly
    return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
    #print return_speed
    return_speed=[100]
    if return_speed:
        #print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
        #if speed == return_speed[0]:
            #print"data send recieve test passed"  
        for pos, delay in positions_delay:
            ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
            ti.sleep(delay)
    #else:
        #print "error setting and getting ax data"
    #print "test complete"
    
    #Reset Dynamixel 1
    
    speed = 100
    ID = 1
    SPEED_REG = 32
    POS_REG = 30
    positions_delay = list([(512,2)])
    ax12 = dm.dynamixel()
    #test serial ports
    #print ax12.port.test_ports()
    #test motors
    #print "moving dynamixel"
    ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
    #test that the speed is set corectly
    return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
    #print return_speed
    return_speed=[100]
    if return_speed:
        #print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
        #if speed == return_speed[0]:
            #print"data send recieve test passed"  
        for pos, delay in positions_delay:
            ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
            ti.sleep(delay)
    #else:
        #print "error setting and getting ax data"
    #print "test complete"
    
    

def movedyn(position_ID1, position_ID2):

    if(position_ID1 >= 1 and position_ID1 <= 1023 and position_ID2 >= 205 and position_ID2 <= 819):
    
        #Move Dynamixel 1
    
        speed = 100
        ID = 1
        SPEED_REG = 32
        POS_REG = 30
        positions_delay = list([(position_ID1,2)])
        ax12 = dm.dynamixel()
        #test serial ports
        #print ax12.port.test_ports()
        #test motors
        #print "moving dynamixel"
        ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
        #test that the speed is set corectly
        return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
        #print return_speed
        return_speed=[100]
        if return_speed:
            #print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
            #if speed == return_speed[0]:
                #print"data send recieve test passed"  
            for pos, delay in positions_delay:
                ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
                ti.sleep(delay)
        #else:
            #print "error setting and getting ax data"
        #print "test complete"
    
        #Move Dynamixel 2
    
        speed = 100
        ID = 2
        SPEED_REG = 32
        POS_REG = 30
        positions_delay = list([(position_ID2,2)])
        ax12 = dm.dynamixel()
        #test serial ports
        #print ax12.port.test_ports()
        #test motors
        #print "moving dynamixel"
        ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
        #test that the speed is set corectly
        return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
        #print return_speed
        return_speed=[100]
        if return_speed:
            #print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
            #if speed == return_speed[0]:
                #print"data send recieve test passed"  
            for pos, delay in positions_delay:
                ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
                ti.sleep(delay)
        #else:
            #print "error setting and getting ax data"
        #print "test complete"
    else:
        print "Error: Position out of safety bounds"

def alt_to_pos2(alt):
    pos2 = int((alt + 60.)*1024./300.)
    return pos2


def az_to_pos1(az):
    pos1 = 512-1*(int((az -30.)*1024./300.)-512) 
    return pos1

def get_gps():
    # Listen on port 2947 (gpsd) of localhost
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    
    datetime="No data"
    lat="No data"
    lon="No data"
    alt="No data"
    
    i=0 
    while i<1:

        try:
            report = session.next()
            # Wait for a 'TPV' report and display the current time
            # To see all report data, uncomment the line below
            #print report
            if report['class'] == 'TPV':
                if hasattr(report, 'lon'):
                    lon=report.lon
                if hasattr(report, 'lat'):
                    lat=report.lat
                if hasattr(report, 'time'):
                    datetime=report.time
                if hasattr(report, 'alt'):
                    alt=report.alt
                    i=1
            else:
                pass
        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print "GPSD has terminated"

    return (datetime,lat,lon,alt)

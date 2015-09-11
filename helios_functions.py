import time
import Dynamixel


def resetdyn():
    
    #Reset Dynamixel 2
    
    speed = 100
    ID = 2
    SPEED_REG = 32
    POS_REG = 30
    positions_delay = list([(512,1)])
    ax12 = dynamixel()
    #test serial ports
    print ax12.port.test_ports()
    #test motors
    print "moving dynamixel"
    ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
    #test that the speed is set corectly
    return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
    print return_speed
    return_speed=[100]
    if return_speed:
        print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
        if speed == return_speed[0]:
            print"data send recieve test passed"  
        for pos, delay in positions_delay:
            ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
            time.sleep(delay)
    else:
        print "error setting and getting ax data"
    print "test complete"
    
    #Reset Dynamixel 1
    
    speed = 100
    ID = 1
    SPEED_REG = 32
    POS_REG = 30
    positions_delay = list([(512,1)])
    ax12 = dynamixel()
    #test serial ports
    print ax12.port.test_ports()
    #test motors
    print "moving dynamixel"
    ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
    #test that the speed is set corectly
    return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
    print return_speed
    return_speed=[100]
    if return_speed:
        print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
        if speed == return_speed[0]:
            print"data send recieve test passed"  
        for pos, delay in positions_delay:
            ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
            time.sleep(delay)
    else:
        print "error setting and getting ax data"
    print "test complete"
    
    

def movedyn(position_ID1, position_ID2):
    
    #Move Dynamixel 1
    
    speed = 100
    ID = 1
    SPEED_REG = 32
    POS_REG = 30
    positions_delay = list([(position_ID1,1)])
    ax12 = dynamixel()
    #test serial ports
    print ax12.port.test_ports()
    #test motors
    print "moving dynamixel"
    ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
    #test that the speed is set corectly
    return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
    print return_speed
    return_speed=[100]
    if return_speed:
        print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
        if speed == return_speed[0]:
            print"data send recieve test passed"  
        for pos, delay in positions_delay:
            ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
            time.sleep(delay)
    else:
        print "error setting and getting ax data"
    print "test complete"
    
    #Move Dynamixel 2
    
    speed = 100
    ID = 2
    SPEED_REG = 32
    POS_REG = 30
    positions_delay = list([(position_ID2,1)])
    ax12 = dynamixel()
    #test serial ports
    print ax12.port.test_ports()
    #test motors
    print "moving dynamixel"
    ax12.set_ax_reg(ID, SPEED_REG, ([(speed%256),(speed>>8)]))
    #test that the speed is set corectly
    return_speed =  ax12.get_reg(ID, ins=READDATA, regstart=SPEED_REG, rlength=1)
    print return_speed
    return_speed=[100]
    if return_speed:
        print "set speed = ", speed, " dynamixel returned speed of ", return_speed[0]
        if speed == return_speed[0]:
            print"data send recieve test passed"  
        for pos, delay in positions_delay:
            ax12.set_ax_reg(ID, POS_REG, ([(pos%256),(pos>>8)]))
            time.sleep(delay)
    else:
        print "error setting and getting ax data"
    print "test complete"
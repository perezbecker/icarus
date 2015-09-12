import gps
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

i=0 
while i<1:
  
    try:
    	report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
	print report
        if report['class'] == 'TPV':
            if hasattr(report, 'lon'):
                longitude=report.lon
            if hasattr(report, 'lat'):
                latitude=report.lat
            if hasattr(report, 'time'):
                time=report.time
            if hasattr(report, 'alt'):
                alt=report.alt
                i=1
                print time,lat,lon,alt
                
    except KeyError:
		pass
    except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "GPSD has terminated"

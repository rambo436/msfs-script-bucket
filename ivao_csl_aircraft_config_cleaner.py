import os, re, fileinput
ivao_dir = os.path.dirname(os.path.abspath(__file__))
airplane_folders = [ f.path for f in os.scandir(ivao_dir) if f.is_dir() ]
# print(ivao_dir)
# print(airplane_folders)
# ------------------------------------------------------------------------------
def flightSimHeaderNumber(header):
    header = header
    number = int(re.search(r'\d+', header).group())
    return number

def isFlightSimHeader(line):
    common_fltsim_string = "[FLTSIM."
    if common_fltsim_string in line:
        return True
    else:
        return False


for airplane in airplane_folders:
    filename = airplane + "\\aircraft.cfg"
    common_fltsim_string = "FLTSIM."
    flt_zero = "[FLTSIM.0]"
    fltsim_number = 0
    line_counter = 0
    fltsim_config_items = []
    config_dict = {}
    copy = False
    # print("Opening: " + filename)
    aircaft_cfg_file = open(filename, "r")
    aircraft_cfg_contents = aircaft_cfg_file.read()
    aircaft_cfg_file.close()

    # Add Services (Not sure if this works in sim yet).
    aircraft_cfg_contents = aircraft_cfg_contents.replace("PUSHBACK=0","PUSHBACK=1")
    aircraft_cfg_contents = aircraft_cfg_contents.replace("MARSHALLER=0","MARSHALLER=1")
    aircraft_cfg_contents = aircraft_cfg_contents.replace("JETWAY=0","JETWAY=1")
    aircraft_cfg_contents = aircraft_cfg_contents.replace("isAirTraffic=0","isAirTraffic=1")
    aircraft_cfg_contents = aircraft_cfg_contents.replace("BOARDING_RAMP=0","BOARDING_RAMP=1")
    aircraft_cfg_contents = aircraft_cfg_contents.replace("SMALL_PUSHBACK=1","SMALL_PUSHBACK=0")

    # Save changes.
    f = open(filename, "w")
    f.write(aircraft_cfg_contents)
    f.close()

    # print(aircraft_cfg_contents)
    fltsim_dict = {}
    with open(filename, "r") as aircraft_cfg:
        config_in_mem = aircraft_cfg.readlines()

    with open(filename, "w") as out_file:
        for line in config_in_mem:
            # print(line)
            if line not in "icao_airline": # Some files/entries have icao_airline="" this will ensure those are not written to config and only we add that field.
                if isFlightSimHeader(line):
                    copy = True
                    fltsim_number = flightSimHeaderNumber(line)
                    # fltsim_dict.append(fltsim_number: [])
                elif "[" in line and not isFlightSimHeader(line):
                    copy = False

                elif "Texture=" in line:
                    icao_airline = line.split("=",1)[1].upper() # Splits text into a list where "=" is the delimeter; grabs second item in list (value).
                                    # fltsim_config_items[-1].update({'texture': line, 'icao_airline': icao_airline}) # Finds last item in list and adds new dictionary key:value pairs.
                                    # print(fltsim_config_items)
                    line = line + "icao_airline=" +icao_airline[0:3] #+ "\n"
                out_file.write(line)

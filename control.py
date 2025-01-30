import tinytuya
import json

class DiffuserState:

    def __init__(self, data=None):

        # Default values
        self.power = False
        self.spray = "off"
        self.clr_mode = "2"
        self.clr = "#f39c9c"
        self.brightness = 255

        # If data provided
        if isinstance(data, dict):
            self.power = data["dps"]["1"]
            self.spray = data["dps"]["103"]
            self.clr_mode = data["dps"]["110"]
            self.clr = data["dps"]["108"]
            self.brightness = data["dps"]["111"]

    def __repr__(self):
        return f"MyClass(power={self.power}, spray={self.spray}, clr_mode={self.clr_mode}, clr={self.clr}, brightness={self.brightness})"



# Connect to Device
d = tinytuya.DiffuserDevice(
    dev_id='bf0b43e24218f44c8axniv',
    address='Auto',      # Or set to 'Auto' to auto-discover IP address
    local_key='t~Yb#8Y\'d1fh<fFi', 
    version=3.4)

# Test state class
myState = d.status()
print(repr(myState))




# Get Status
#data = d.set_intermittence()
#d.turn_on()

#d.set_colour("00fff9")
#d.set_brightness(255)

data = d.status()
print(data["dps"]["1"])
jsonObject = json.loads(json.dumps(data))


print(repr(data))
cleanedStr = repr(data).replace("'", "\"").replace(" ", "")
print(cleanedStr)
jdata = json.loads(cleanedStr)
print(jdata)
#print(data[1])
#print('set_status() result %r' % data)





# Turn On
#d.turn_on()


# Turn Off
#d.turn_off()

#Get functions
#d.getfunctions('bf0b43e24218f44c8axniv')
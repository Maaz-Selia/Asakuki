import colorsys

def _rgb_to_tuya(r, g, b):
        """
        Convert an RGB value to the hex representation expected by Tuya Bulb.

        format: rrggbb0hhhssvv

        Args:
            r(int): Value for the colour red as int from 0-255.
            g(int): Value for the colour green as int from 0-255.
            b(int): Value for the colour blue as int from 0-255.
        """
        rgb = [r, g, b]
        hsv = colorsys.rgb_to_hsv(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)

        """
        # Bulb Type A
        if bulb == "A":
        """
        # h:0-360,s:0-255,v:0-255|hsv|
        hexvalue = ""
        for value in rgb:
            temp = str(hex(int(value))).replace("0x", "")
            if len(temp) == 1:
                temp = "0" + temp
            hexvalue = hexvalue + temp

        hsvarray = [int(hsv[0] * 360), int(hsv[1] * 255), int(hsv[2] * 255)]
        hexvalue_hsv = ""
        for value in hsvarray:
            temp = str(hex(int(value))).replace("0x", "")
            if len(temp) == 1:
                temp = "0" + temp
            hexvalue_hsv = hexvalue_hsv + temp
        if len(hexvalue_hsv) == 7:
            hexvalue = hexvalue + "0" + hexvalue_hsv
        else:
            hexvalue = hexvalue + "00" + hexvalue_hsv

        """
        # Bulb Type B
        if bulb == "B":
            # h:0-360,s:0-1000,v:0-1000|hsv|
            hexvalue = ""
            hsvarray = [int(hsv[0] * 360), int(hsv[1] * 1000), int(hsv[2] * 1000)]
            for value in hsvarray:
                temp = str(hex(int(value))).replace("0x", "")
                while len(temp) < 4:
                    temp = "0" + temp
                hexvalue = hexvalue + temp
        """

        return hexvalue

def _hex_to_rgb(hexvalue):
        """
        Converts the hexvalue used by Tuya for colour representation into
        an RGB value.

        Args:
            hexvalue(string): The hex representation generated by BulbDevice._rgb_to_hexvalue()
        """
        r = int(hexvalue[0:2], 16)
        g = int(hexvalue[2:4], 16)
        b = int(hexvalue[4:6], 16)

        """
        elif bulb == "B":
            # hexvalue is in hsv
            h = float(int(hexvalue[0:4], 16) / 360.0)
            s = float(int(hexvalue[4:8], 16) / 1000.0)
            v = float(int(hexvalue[8:12], 16) / 1000.0)
            rgb = colorsys.hsv_to_rgb(h, s, v)
            r = int(rgb[0] * 255)
            g = int(rgb[1] * 255)
            b = int(rgb[2] * 255)
        else:
            # Unsupported bulb type
            raise ValueError(f"Unsupported bulb type {bulb} - unable to determine RGB values.")
        """
        return (r, g, b)

def _hex_to_hsv(hexvalue):
    """
    Converts the hexvalue used by Tuya for colour representation into
    an HSV value.

    Args:
        hexvalue(string): The hex representation generated by BulbDevice._rgb_to_hexvalue()
    """

    h = int(hexvalue[7:10], 16) / 360.0
    s = int(hexvalue[10:12], 16) / 255.0
    v = int(hexvalue[12:14], 16) / 255.0
    """
    elif bulb == "B":
        # hexvalue is in hsv
        h = int(hexvalue[0:4], 16) / 360.0
        s = int(hexvalue[4:8], 16) / 1000.0
        v = int(hexvalue[8:12], 16) / 1000.0
    else:
        # Unsupported bulb type
        raise ValueError(f"Unsupported bulb type {bulb} - unable to determine HSV values.")
    """
    
    return (h, s, v)

def _hex_to_tuya(hexvalue):
    return _rgb_to_tuya(_hex_to_rgb(hexvalue))
     
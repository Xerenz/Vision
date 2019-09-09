import numpy as np
import cv2

'''To change RGB type images to HSV'''

def rgb_to_hsv(image):
    rows, columns, channels = image.shape

    for row in image:
        MAX = [max(row[i]) for i in range(rows)] # for hue
        val = MAX
        
        MIN = [min(row[i]) for i in range(rows)] # for saturation
        
        diff = [] # for hue
        for px in row:
            x, y = [num for num in row if num != max(row)]
            diff.append(x - y)
    
        if max(MAX) == 0:
            # hue and saturation
            
            hue = sat = [0]*rows
        else:
            sat = map(lambda x, y: (x-y)/x, MAX, MIN)

            _hue = map(lambda d, x, y: d/(x-y), diff, MAX, MIN)

            hue = [] # real hue
            for _h in _hue:
                if _h < 0:
                    h = _h/6 + 1
                else:
                    h = _h/6
                hue.append(h)

        # combine hue, saturation, value

        _image = [hue, sat, val]

        # get transpose
        _image = np.array(_image)
        image = _image.T

        return image
        
        

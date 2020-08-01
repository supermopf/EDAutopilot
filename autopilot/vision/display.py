from dataclasses import dataclass

import cv2
import d3dshot  # <--- Apparently fastest screenshot method on windows
import numpy

_d3d = d3dshot.create(capture_output="numpy")

display = _d3d.display
displays = _d3d.displays
width = display.resolution[0]
height = display.resolution[1]


@dataclass
class Configuration:
    width: int
    height: int


def screenshot(left, top, right, bottom):
    """Gets screenshot in cv2 friendly BGR numpy array format specified by given region"""
    left, top, right, bottom = round(left), round(top), round(right), round(bottom)
    # _d3d,create above has output set to numpy but it doesn't seem to care :/ output is pil
    pil_image = _d3d.screenshot(region=(left, top, right, bottom))
    # So need to convert to cv2 numpy array
    numpy_rgb_image = numpy.array(pil_image)
    # Finally, cv2 mostly uses BGR as default, so expediting conversion
    numpy_bgr_image = cv2.cvtColor(numpy_rgb_image, cv2.COLOR_RGB2BGR)
    return numpy_bgr_image


if __name__ == '__main__':
    print(screenshot(100.5, 100, 300, 300))
    print(_d3d.displays[0])
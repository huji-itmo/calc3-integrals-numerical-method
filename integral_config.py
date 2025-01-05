

import math

# https://www.desmos.com/Calculator/3yyizfiinx
# кривая L задается как x^2+y^2=16, x+y<0;
def natural_parametrization_path(t: float) -> tuple[float, float]:
    if (t < 0 or t > 4 * math.pi + 8):
        return (float('nan'), float('nan'))
    if (t >= 0 and t < 4 * math.pi):
        return (4 * math.cos((3/4)*math.pi+t/4),4 * math.sin((3/4)*math.pi+t/4));
    else:
        return (2*math.sqrt(2)-(math.sqrt(2)/2) * (t-4*math.pi),-2*math.sqrt(2)+ (math.sqrt(2)/2) * (t-4*math.pi))

def f_1(xy: tuple[float, float]):
    x, y = xy
    return x*(y**2)

def f_2(xy: tuple[float, float]):
    x, y = xy
    return -(x**2)*y

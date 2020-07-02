from math import sqrt

#lists for basic types (i.e. int, float, str, etc.)
numTypes = (int, float)

class vec2():
    def __init__(self, x, y):
        if type(x) in numTypes and type(y) in numTypes:
            self.x = x
            self.y = y
        else:
            raise TypeError('Invalid parameter supplied.')

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return 'vec2({}, {})'.format(self.x, self.y)

    def __int__(self):
        return int(self.__float__())

    def __float__(self):
        return sqrt((self.x ** 2) + (self.y ** 2))

    def __add__(self, v):
        if type(v) is vec2:
            return vec2(self.x + v.x, self.y + v.y)
        else:
            raise TypeError('cannot add vec2 and {}'.format(type(v)))

    def __sub__(self, v):
        if type(v) is vec2:
            return vec2(self.x - v.x, self.y - v.y)
        else:
            raise TypeError('cannot add vec2 and {}'.format(type(v)))

    def __mul__(self, v):
        if type(v) in numTypes:
            return vec2(self.x * v, self.y * v)
        else:
            return NotImplemented

    def __truediv__(self, v):
        if type(v) in numberTypes:
            vals = ()
            vals.append(self.x / v)
            vals.append(self.y / v)
            
            for val in vals:
                if val == int(val):
                    val = int(val)

            return vec3(vals[0], vals[1])
        else:
            return NotImplemented

    def __radd__(self, v):
        return self.__add__(v)

    def __rsub__(self, v):
        return self.__sub__(v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __rtruediv__(self, v):
        return self.__truediv__(v)

class vec3():
    def __init__(self, x, y, z):
        if type(x) in numTypes and type(y) in numTypes and type(z) in numTypes:
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError('Invalid parameter supplied.')

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return 'vec3({}, {}, {})'.format(self.x, self.y, self.z)

    def __int__(self):
        return int(self.__float__())

    def __float__(self):
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def __add__(self, v):
        if type(v) is vec3:
            return vec3(self.x + v.x, self.y + v.y, self.z + v.z)
        else:
            raise TypeError('cannot add vec3 and {}'.format(type(v)))

    def __sub__(self, v):
        if type(v) is vec3:
            return vec3(self.x - v.x, self.y - v.y, self.z - v.z)
        else:
            raise TypeError('cannot add vec3 and {}'.format(type(v)))

    def __mul__(self, v):
        if type(v) in numTypes:
            return vec3(self.x * v, self.y * v, self.z * v)
        else:
            return NotImplemented

    def __truediv__(self, v):
        if type(v) in numTypes:
            vals = ()
            vals.append(self.x / v)
            vals.append(self.y / v)
            vals.append(self.z / v)
            
            for val in vals:
                if val == int(val):
                    val = int(val)

            return vec3(vals[0], vals[1], vals[2])
        else:
            return NotImplemented

    def __radd__(self, v):
        return self.__add__(v)

    def __rsub__(self, v):
        return self.__sub__(v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __rtruediv__(self, v):
        return self.__truediv__(v)

class vec4():
    def __init__(self, x, y, z, w):
        if type(x) in numTypes and type(y) in numTypes and type(z) in numTypes and type(w) in numTypes:
            self.x = x
            self.y = y
            self.z = z
            self.w = w
        else:
            raise TypeError('Invalid parameter supplied.')

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return 'vec4({}, {}, {}, {})'.format(self.x, self.y, self.z, self.w)

    def __int__(self):
        return int(self.__float__())

    def __float__(self):
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2) + (self.w ** 2))

    def __add__(self, v):
        if type(v) is vec4:
            return vec4(self.x + v.x, self.y + v.y, self.z + v.z, self.w + v.w)
        else:
            raise TypeError('cannot add vec4 and {}'.format(type(v)))

    def __sub__(self, v):
        if type(v) is vec4:
            return vec4(self.x - v.x, self.y - v.y, self.z - v.z, self.w - v.w)
        else:
            raise TypeError('cannot add vec4 and {}'.format(type(v)))

    def __mul__(self, v):
        if type(v) in numTypes:
            return vec4(self.x * v, self.y * v, self.z * v, self.w * v)
        else:
            return NotImplemented

    def __truediv__(self, v):
        if type(v) in numberTypes:
            vals = ()
            vals.append(self.x / v)
            vals.append(self.y / v)
            vals.append(self.z / v)
            vals.append(self.w / v)
            
            for val in vals:
                if val == int(val):
                    val = int(val)

            return vec3(vals[0], vals[1], vals[2], vals[3])
        else:
            return NotImplemented

    def __radd__(self, v):
        return self.__add__(v)

    def __rsub__(self, v):
        return self.__sub__(v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __rtruediv__(self, v):
        return self.__truediv__(v)
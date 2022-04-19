# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gb_visual_detection_3d_msgs/BoundingBox3d.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class BoundingBox3d(genpy.Message):
  _md5sum = "6e20dcf06c2cb2c3714e76bbf196e60c"
  _type = "gb_visual_detection_3d_msgs/BoundingBox3d"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string Class
float64 probability
float64 xmin
float64 ymin
float64 xmax
float64 ymax
float64 zmin
float64 zmax
"""
  __slots__ = ['Class','probability','xmin','ymin','xmax','ymax','zmin','zmax']
  _slot_types = ['string','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Class,probability,xmin,ymin,xmax,ymax,zmin,zmax

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BoundingBox3d, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Class is None:
        self.Class = ''
      if self.probability is None:
        self.probability = 0.
      if self.xmin is None:
        self.xmin = 0.
      if self.ymin is None:
        self.ymin = 0.
      if self.xmax is None:
        self.xmax = 0.
      if self.ymax is None:
        self.ymax = 0.
      if self.zmin is None:
        self.zmin = 0.
      if self.zmax is None:
        self.zmax = 0.
    else:
      self.Class = ''
      self.probability = 0.
      self.xmin = 0.
      self.ymin = 0.
      self.xmax = 0.
      self.ymax = 0.
      self.zmin = 0.
      self.zmax = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.Class
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.zmin, _x.zmax))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Class = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Class = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.zmin, _x.zmax,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.Class
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.zmin, _x.zmax))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Class = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Class = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.probability, _x.xmin, _x.ymin, _x.xmax, _x.ymax, _x.zmin, _x.zmax,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d

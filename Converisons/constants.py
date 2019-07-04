import enum

class AnnotationOutputFormat(enum.Enum):
    TIKA_XML=1
    TIKA_JSON=2
    PASCALVOC_XML=3
    COCO_JSON=4
    YOLO_TXT=5
class AnnotationOutputMode(enum.Enum):
    FILE=1
    OBJECT=2
    DIR=3
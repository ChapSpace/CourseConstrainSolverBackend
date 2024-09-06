from enum import Enum

class Quarter(Enum):
    FALL = 1
    WINTER = 2
    SPRING = 3
    SUMMER = 4


class GER(Enum):
    WAY_A_II = "way a-ii"
    WAY_AQR = "way aqr"
    WAY_CE = "way ce"
    WAY_EDP = "way edp"
    WAY_ER = "way er"
    WAY_FR = "way fr"
    WAY_SI = "way si"
    WAY_SMA = "way sma"
    WRITING_1 = "writing 1"
    WRITING_2 = "writing 2"
    SLE = "sle"
    COLLEGE = "college"
    LANGUAGE = "language"


class Grade(Enum):
    A_PLUS = 4.3
    A = 4.0
    A_MINUS = 3.7
    B_PLUS = 3.3
    B = 3.0
    B_MINUS = 2.7
    C_PLUS = 2.3
    C = 2.0
    C_MINUS = 1.7
    D_PLUS = 1.3
    D = 1.0
    D_MINUS = 0.7
    NP = 0.0
    INCOMPLETE = 0.0
    CREDIT = "credit"
    NO_CREDIT = "no credit"
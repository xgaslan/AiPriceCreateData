from datetime import date
import sys


class AccommodationDistance():

    def __init__(self, saleDate, startDate):

        self.startDate = startDate
        self.saleDate = saleDate
        self.difference = (startDate - saleDate).days

        try:
            if (self.difference < 0):
                print("girilen baslangic tarihi satis tarihinden buyuk olamaz")
        except:
            #print(SystemError(sys.exc_info()[0]))
            print(sys.exc_info()[0])

    def accomondationDistanceWeight(self):
        distancaWeight = {
            0: 2.75,
            1: 2.5,
            2: 2.25,
            3: 2.2,
            4: 2,
            5: 1.9,
            6: 1.8,
            7: 1.75,
            8: 1.744,
            9: 1.732,
            10: 1.72,
            11: 1.708,
            12: 1.696,
            13: 1.684,
            14: 1.672,
            15: 1.66,
            16: 1.648,
            17: 1.636,
            18: 1.624,
            19: 1.612,
            20: 1.6,
            21: 1.588,
            22: 1.576,
            23: 1.564,
            24: 1.552,
            25: 1.54,
            26: 1.528,
            27: 1.516,
            28: 1.504,
            29: 1.492,
            30: 1.48,
            31: 1.468,
            32: 1.456,
            33: 1.444,
            34: 1.432,
            35: 1.42,
            36: 1.408,
            37: 1.396,
            38: 1.384,
            39: 1.372,
            40: 1.36,
            41: 1.348,
            42: 1.336,
            43: 1.324,
            44: 1.312,
            45: 1.3,
            46: 1.288,
            47: 1.276,
            48: 1.264,
            49: 1.252,
            50: 1.24,
            51: 1.228,
            52: 1.216,
            53: 1.204,
            54: 1.192,
            55: 1.18,
            56: 1.168,
            57: 1.156,
            58: 1.144,
            59: 1.132,
            60: 1.12,
            61: 1.108,
            62: 1.096,
            63: 1.084,
            64: 1.072,
            65: 1.06,
            66: 1.048,
            67: 1.036,
            68: 1.024,
            69: 1.012,
            70: 1,
            71: 1,
            72: 1,
            73: 1,
            74: 1,
            75: 1,
            76: 1,
            77: 1,
            78: 1,
            79: 1,
            80: 1,
            81: 1,
            82: 1,
            83: 1,
            84: 1,
            85: 1,
            86: 1,
            87: 1,
            88: 1,
            89: 1,
            90: 1,
            91: 1,
            92: 1,
            93: 1,
            94: 1,
            95: 1,
            96: 1,
            97: 1,
            98: 1,
            99: 1,
            100: 0.9,
            101: 0.9,
            102: 0.9,
            103: 0.9,
            104: 0.9,
            105: 0.9,
            106: 0.9,
            107: 0.9,
            108: 0.9,
            109: 0.9,
            110: 0.9,
            111: 0.9,
            112: 0.9,
            113: 0.9,
            114: 0.9,
            115: 0.9,
            116: 0.9,
            117: 0.9,
            118: 0.9,
            119: 0.9,
            120: 0.8,
            121: 0.8,
            122: 0.8,
            123: 0.8,
            124: 0.8,
            125: 0.8,
            126: 0.8,
            127: 0.8,
            128: 0.8,
            129: 0.8,
            130: 0.8,
            131: 0.8,
            132: 0.8,
            133: 0.8,
            134: 0.8,
            135: 0.8,
            136: 0.8,
            137: 0.8,
            138: 0.8,
            139: 0.8,
            140: 0.8,
            141: 0.8,
            142: 0.8,
            143: 0.8,
            144: 0.8,
            145: 0.8,
            146: 0.8,
            147: 0.8,
            148: 0.8,
            149: 0.8,
            150: 0.7,
            151: 0.7,
            152: 0.7,
            153: 0.7,
            154: 0.7,
            155: 0.7,
            156: 0.7,
            157: 0.7,
            158: 0.7,
            159: 0.7,
            160: 0.7,
            161: 0.7,
            162: 0.7,
            163: 0.7,
            164: 0.7,
            165: 0.7,
            166: 0.7,
            167: 0.7,
            168: 0.7,
            169: 0.7,
            170: 0.7,
            171: 0.7,
            172: 0.7,
            173: 0.7,
            174: 0.7,
            175: 0.7,
            176: 0.7,
            177: 0.7,
            178: 0.7,
            179: 0.7,
            180: 0.7,
        }

        return distancaWeight[self.difference]

class NumService:
    number = 0

    @classmethod
    def getNumber(cls):
        return cls.number
    
    @classmethod
    def uppNumber(cls):
        cls.number += 1
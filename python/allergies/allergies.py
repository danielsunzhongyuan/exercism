class Allergies(object):
    def __init__(self, n):
        self.allergies = self.get_list(n%256)

    def get_list(self, n):
        allergy_score = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        ret = []
        tmp = 0
        while n > 0:
            if n % 2 == 1:
                ret.append(allergy_score[tmp])
            n /= 2
            tmp += 1
        lst = ret
        return ret

    def is_allergic_to(self, allergy):
        return allergy in self.allergies

    @property
    def lst(self):
        return self.allergies

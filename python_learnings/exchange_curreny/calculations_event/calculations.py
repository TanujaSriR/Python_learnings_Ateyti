class events:
    def __init__(self,quantity,per_person,per_gift,clothes,jwellery):
        self.quantity=quantity
        self.per_person=per_person
        self.per_gift=per_gift
        self.clothes=clothes
        self.jwellery=jwellery
    def banquet_hall(self):
        for_lunch_200=self.quantity*self.per_person
        for_tiffin=100*150
        total_banquet_cost=for_lunch_200+for_tiffin
        return total_banquet_cost
    def decor(self):
        return 45000
    def makeup(self):
        return 10000
    def gifts(self):
        for_gifts=200*self.per_gift
        return for_gifts
    def shopping(self):
        for_shopping=self.clothes+self.jwellery
        return for_shopping
    
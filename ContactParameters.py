import random

class ContactParameters:
    def __init__(self):
        self.FirstName = random.randint(1, 1000000)
        self.MiddleName = random.randint(1, 1000000)
        self.LastName = random.randint(1, 1000000)
        self.NickName = random.randint(1, 1000000)
        self.Title = random.randint(1, 1000000)
        self.Company = random.randint(1, 1000000)
        self.Address = random.randint(1, 1000000)
        self.HomeTelephone = random.randint(1, 1000000)
        self.MobileTelephone = random.randint(1, 1000000)
        self.WorkTelephone = random.randint(1, 1000000)
        self.Fax = random.randint(1, 1000000)
        self.Email = random.randint(1, 1000000)
        self.HomePage = random.randint(1, 1000000)

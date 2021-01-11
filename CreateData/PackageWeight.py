class PackageWeight:

    def __init__(self, id):
        self.id = id

    def packageWeight(self):

        packages = {
            0: 1,        # Yalnızca Oda
            1: 1.05,     # Kahvalti
            2: 1.15,     # Kahvalti + Ogle Yemegi
            3: 1.25,     # Kahvalti + Ogle Yemegi + Aksam Yemegi
            4: 1.6,      # Hersey Dahil
            5: 1.75      # Ultra Hersey Dahil
        }

        return packages[self.id]

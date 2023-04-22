class Warehouse:
    purpose = 'storage'
    region = 'east'


if __name__ == '__main__':
    w1 = Warehouse()
    print('w1 {0}', w1.region)
    w2 = Warehouse()
    w2.region = 'west'
    print('w2 {0}', w2.region)
    print('w1 {0}', w1.region)
    print('Class {0}', Warehouse.region)
    w3 = Warehouse()
    print('w3 {0}', w3.region)

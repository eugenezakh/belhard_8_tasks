from gardener import Gardener
from tomato import Tomato
from tomato_bush import TomatoBush

if __name__ == '__main__':
    bush_1 = TomatoBush(Tomato(1), Tomato(2), Tomato(3))
    bush_2 = TomatoBush(Tomato(4), Tomato(5), Tomato(6), Tomato(7))
    bush_3 = TomatoBush(Tomato(8), Tomato(9))

    staff = Gardener("Василий Павлович", bush_1, bush_2, bush_3)
    staff.work()
    while True:
        if staff.harvest() is None:
            print('Собирать пока нечего')
            staff.work()
        else:
            print(f'{staff.name} собрал {len(staff.harvest())} томатов!')
            break

# 1. Итератор

class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = copy.deepcopy(list_of_list)
        pass

    def __iter__(self):
        self.ind_out = 0
        return self



    def __next__(self):
        while self.ind_out != len(self.lists):
            item = self.lists[self.ind_out].pop(0)
            if len(self.lists[self.ind_out]) == 0:
                self.ind_out += 1
            return item

        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



if __name__ == '__main__':
    import copy
    test_1()



# 2. Генератор

import types

def flat_generator(list_of_lists):

    for list in list_of_lists:
        for item in list:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()




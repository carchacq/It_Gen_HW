# 1. Итератор

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        pass

    def __iter__(self):
        self.ind_out = 0
        return self

# Этот код не работает. Не понимаю, почему. Ведь StopIteration происходит, когда все списки уже пустые
    # def __next__(self):
    #     item = self.list_of_list[self.ind_out].pop(self.ind_in)
    #     if len(self.list_of_list[self.ind_out]) == 0:
    #         self.ind_out += 1
    #     if self.ind_out == len(self.list_of_list):
    #         raise StopIteration
    #     return item

    def __next__(self):
        while self.ind_out != len(self.list_of_list):
            item = self.list_of_list[self.ind_out].pop(0)
            if len(self.list_of_list[self.ind_out]) == 0:
                self.ind_out += 1
            return item

        raise StopIteration

def test_1():
    import copy
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    copy1 = copy.deepcopy(list_of_lists_1)
    copy2 = copy.deepcopy(list_of_lists_1)

    for flat_iterator_item, check_item in zip(
            FlatIterator(copy1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item


    assert list(FlatIterator(copy2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()



# 2. Генератор

# import types
#
# def flat_generator(list_of_lists):
#
#     ...
#     yield
#     ...
#
#
# def test_2():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
#
#
# if __name__ == '__main__':
#     test_2()



# class HelloWorld:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         self.cursor = 0
#         return self
#
#     def __next__(self):
#         if self.cursor >= self.n:
#             raise StopIteration
#         self.cursor += 1
#         return 'hello world'
#
#
# if __name__ == '__main__':
#     for item in HelloWorld(4):
#         print(item)

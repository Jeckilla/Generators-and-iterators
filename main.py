class FlatIterator:

    def __init__(self, list_of_list):
        self.cursor = -1
        self.list_of_list = list_of_list
        self.list_len = len(list_of_list)
        self.flat_iterator_item = []

    def __iter__(self):
        self.cursor += 1
        self.list_cursor = 0
        return self

    def __next__(self):
        if self.list_cursor == len(self.list_of_list[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.list_cursor += 1
        return self.list_of_list[self.cursor][self.list_cursor - 1]

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
    test_1()
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    print(list(FlatIterator(list_of_lists_1)))



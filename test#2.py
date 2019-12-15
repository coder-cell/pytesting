numerical_list = range(0, 10)


class TestNumerals(object):

    def test_1(self):
        assert 9 in numerical_list

    def test_2(self):
        assert 11 in numerical_list

    def test_3(self):
        assert len(numerical_list) == 10

    def test_4(self):
        assert numerical_list

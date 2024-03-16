# ფუნქცია ამოწმებს მარტივია თუ არა რიცხვი. (მარტივია თუ მხოლოდ 1_ზე და საკუთარ თავზე იყოფა)


import unittest


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# გატესტე ფუნქცია'unittest'_ის დახმარებით.


class TestIsPrime(unittest.TestCase):

    def setUp(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.not_primes = [0, 1, 4, 6, 8, 10, 12, 27, 32, 33]

    def test_is_prime(self):
        for i in self.primes:
            self.assertTrue(is_prime(i))
        for j in self.not_primes:
            self.assertFalse(is_prime(j))


if __name__ == "__main__":
    unittest.main()

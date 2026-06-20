from main import is_prime

class TestPrime:
    def test_prime(self):
        assert is_prime(7) == True
        assert is_prime(4) == False
        assert is_prime(1) == False
    def test_edge_cases(self):
        assert is_prime(2) == True
        assert is_prime(0) == False
        assert is_prime(-5) == False
if __name__ == "__main__":
    test = TestPrime()
    test.test_prime()
    test.test_edge_cases()
    print("All tests passed!")
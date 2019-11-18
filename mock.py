from unittest.mock import Mock
import unittest

class B:
	def call(self):
		return True

class A:
	def __init__(self, B):
		self.b = B()

	def call(self):
		return self.b.call()

class TestCases(unittest.TestCase):

	def test_call(self):
		c = Mock
		a = A(c)
		print(a.b)
		a.b.call.return_value = 5

		print('calling...',a.call())



if __name__ == '__main__':
	unittest.main()



		# def test_update_catch(self):
	# 	hex_disp = HexDispData(0x20, 0x8)
	# 	hex_disp = Mock()
	# 	hex_disp.return_value = 5
	# 	self.serial.read_timeo.return_value = "0x0001=51"
	# 	self.assertEqual(self.micro_obj.__getitem__(0x0001), 51)
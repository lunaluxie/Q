import unittest

import math
import numpy as np

from Q import *

class TestQuBitInit(unittest.TestCase):

	def test_init_none(self):
		qb = Qubit()
		self.assertIsNotNone(qb)

	def test_init_basic(self):
		qb = Qubit(0, 1)
		self.assertIsNotNone(qb)

		qb = Qubit(1, 0)
		self.assertIsNotNone(qb)

	def test_init_linear(self):
		qb = Qubit(0, 1)
		self.assertIsNotNone(qb)

		qb = Qubit(1, 0)
		self.assertIsNotNone(qb)

	def test_init_wrong_magnitude(self):
		with self.assertRaisesRegex(ValueError, 'Magnitude of a QuBit must be equal to 1'):
			qb = Qubit(1,1)

class TestQuBitSetAndGet(unittest.TestCase):

	def test_set_state_basic(self):
		qb = Qubit()
		self.assertIsNotNone(qb)

		qb.set_state(0,1)
		self.assertEqual(qb.alpha, 0)
		self.assertEqual(qb.beta, 1)

		qb.set_state(1,0)
		self.assertEqual(qb.alpha, 1)
		self.assertEqual(qb.beta, 0)

	def test_set_state_wrong_magnitude(self):
		with self.assertRaisesRegex(ValueError, 'Magnitude of a QuBit must be equal to 1'):
			qb = Qubit()
			qb.set_state(0,0)

		with self.assertRaisesRegex(ValueError, 'Magnitude of a QuBit must be equal to 1'):
			qb = Qubit(1,1)

	def test_get_state(self):
		qb = Qubit(1,0)

		self.assertEqual(qb.get_state(), (1,0))

	def test_set_partial_state(self):
		qb = Qubit(1)
		self.assertEqual(qb.get_state(), (1,0))

		qb = Qubit(beta=1)
		self.assertEqual(qb.get_state(), (0,1))

	def test_measure_unset_state(self):
		with self.assertRaisesRegex(ValueError, 'State must be set before measured'):
			qb = Qubit()
			qb.measure_state()

class TestQuBitApplyGate(unittest.TestCase):

	def test_apply_gate_simple(self):
		qb = Qubit(1,0)

		h_gate = 1/math.sqrt(2) * np.array([[1,1],[1,-1]])
		n_gate = np.array([[0,1],[1,0]])

		qb.apply_gate(h_gate)
		qb.apply_gate(n_gate)

		self.assertEqual(round(qb.get_state()[0],2), 0.71)
		self.assertEqual(round(qb.get_state()[1],2), 0.71)

	def test_apply_gate_bad(self):
		with self.assertRaisesRegex(ValueError, 'Gate must be unitary'):
			bad_gate = np.array([[1,1],[1,1]])
			qb = Qubit(1,0)

			qb.apply_gate(bad_gate)

if __name__ == '__main__':
	unittest.main()

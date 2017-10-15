class Qubit:
	"""
	A simulated qubit. 
	"""
	def __init__(self, alpha=None, beta=None, precision=2):
		self.precision = precision
		self.set_state(alpha, beta)

	def __str__(self):
		if self.alpha == None or self.beta == None:
			return "QuBit: State not set"
		return "QuBit: {}|0> {}|1>".format(self.alpha, self.beta)

	def _is_unitary(self, m):
		import numpy as np
		m = np.matrix(m)
		return np.allclose(np.eye(m.shape[0]), m.H * m)

	def _is_valid_state(self, alpha, beta):
		if round(abs(alpha)**2 + abs(beta)**2, self.precision) == 1:
			return True
		else:
			return False

	def set_state(self, alpha=None, beta=None):
		if alpha == None and beta == None:
			self.alpha = alpha
			self.beta = beta
			return (self.alpha, self.beta)

		# calculate the other if only one is specified
		if alpha == None:
			import math
			alpha = math.sqrt(1-abs(beta)**2)
		if beta  == None:
			import math
			beta = math.sqrt(1-abs(alpha)**2)

		# if both are specified check that they are valid and set the state
		if self._is_valid_state(alpha, beta):
			self.alpha = alpha
			self.beta = beta
			return (self.alpha, self.beta)
		else: 
			raise ValueError("Magnitude of a QuBit must be equal to 1")

	def get_state(self):
		return (self.alpha, self.beta)

	def measure_state(self):
		"""
		Simulates measuring a physical qubit.

		Returns 0 with alpha squared probability, 
		and 1 with beta squared probability
		"""
		if self.alpha == None or self.beta == None:
			raise ValueError("State must be set before measured")

		from numpy.random import choice

		alpha_prob = self.alpha**2
		beta_prob = self.beta**2

		draw = choice([0,1], 1, p=[alpha_prob, beta_prob])[0]

		return draw

	def apply_gate(self, gate):
		"""
		Applies a gate matrix to the QuBit.

		Returns the new state.
		"""
		import numpy as np
		if not self._is_unitary(gate):
			raise ValueError("Gate must be unitary")

		state = np.array([self.alpha, self.beta])

		new_state = tuple(np.matmul(np.array(gate), state))

		self.alpha, self.beta = new_state

		return new_state

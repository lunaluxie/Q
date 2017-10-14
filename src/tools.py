def is_unitary(m):
	return np.allclose(np.eye(m.shape[0]), m.H * m)

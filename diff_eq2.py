def test_ForwardEuler_against_linear_solution():
"""Use knowledge of an exact numerical solution for testing."""
def f(u, t):
return 0.2 + (u - u_exact(t))**4
def u_exact(t):
return 0.2*t + 3
u, t = ForwardEuler(f, U0=u_exact(0), T=3, n=5)
u_e = u_exact(t)
error = np.abs(u_e - u).max()
success = error < 1E-14
assert success, ’|exact - u| = %g != 0’ % error

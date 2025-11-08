def approximate_pi(n_terms):
  leibniz_series = [(-1)**i / (2*i + 1) for i in range(n_terms)]
  approx_pi = sum(leibniz_series) * 4
  return approx_pi
  

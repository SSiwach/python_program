def Gaussian_elimination(A):
  rank = 0
  m,n = np.shape(A)
  i =0
  for j in range(n):
    p = np.argmax(abs(A[i:m,j]))
    if p > 0 :
      A[[i,p+i]] = A[[p+i,i]]
    if A[i,j] != 0:
      rank += 1
      for r in range(i+1, m):
        A[r,j:]  -= (A[r,j]/A[i,j]*A[i,j:])
      i += 1
    if i > m:
      break
  return A, rank

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 6  // Size of matrix

void find_eigenvectors(double A[N][N], double lambda, double x[N]) {
  double I[N][N];  // Identity matrix
  double y[N];  // Intermediate result

  // Initialize identity matrix
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      I[i][j] = (i == j) ? 1 : 0;
    }
  }

  // Solve the equation (A - lambda * I) * y = 0 to find y
  for (int i = 0; i < N; i++) {
    y[i] = 0;
    for (int j = 0; j < N; j++) {
      y[i] += (A[i][j] - lambda * I[i][j]) * x[j];
    }
  }

  // Normalize the eigenvector
  double norm = 0;
  for (int i = 0; i < N; i++) {
    norm += x[i] * x[i];
  }
  norm = sqrt(norm);

  // Divide each element of the eigenvector by the length
  for (int i = 0; i < N; i++) {
    x[i] /= norm;
  }
}

int main(void) {
  double A[N][N] = {{2 ,-1,0 ,0, 1},
                    {-1,2 ,1 ,0, 0},
                    {0 ,1 ,1 ,1, 0},
                    {0 ,0 ,1 ,2,-1},
                    {1 ,0 ,0 ,-1,2}};
  double lambda = 0.38917;  // Eigenvalue
  double x[N];  // Eigenvector
  find_eigenvectors(A, lambda, x);
  for (int i = 0; i < N; i++) {
    printf("%f ", x[i]);
  }
  printf("\n");
  return 0;
}

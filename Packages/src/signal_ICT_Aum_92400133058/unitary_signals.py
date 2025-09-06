import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """
    Generate unit-step signal of length n.
    Uses index vector centered at 0: n_vec = [-n//2 ... n-1-n//2].
    Returns: numpy array of 0/1 of length n. Also plots stem.
    """
    half = n // 2
    n_vec = np.arange(-half, -half + n)
    u = (n_vec >= 0).astype(int)
    plt.figure()
    plt.stem(n_vec, u, basefmt=" ", use_line_collection=True)
    plt.title(f"Unit Step (length={n})")
    plt.xlabel("n")
    plt.ylabel("u[n]")
    plt.grid(True)
    plt.show()
    return u

def unit_impulse(n):
    """
    Generate unit impulse (delta) signal of length n.
    Centered index vector like unit_step. delta[ index==0 ] = 1.
    """
    half = n // 2
    n_vec = np.arange(-half, -half + n)
    delta = (n_vec == 0).astype(int)
    plt.figure()
    plt.stem(n_vec, delta, basefmt=" ", use_line_collection=True)
    plt.title(f"Unit Impulse (length={n})")
    plt.xlabel("n")
    plt.ylabel("delta[n]")
    plt.grid(True)
    plt.show()
    return delta

def ramp_signal(n):
    """
    Generate a causal ramp: r[n] = n for n>=0 else 0.
    Length n, indices centered same as step.
    """
    half = n // 2
    n_vec = np.arange(-half, -half + n)
    ramp = np.where(n_vec >= 0, n_vec, 0).astype(float)
    plt.figure()
    plt.stem(n_vec, ramp, basefmt=" ", use_line_collection=True)
    plt.title(f"Ramp Signal (length={n})")
    plt.xlabel("n")
    plt.ylabel("r[n]")
    plt.grid(True)
    plt.show()
    return ramp

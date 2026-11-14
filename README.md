# Assignment6
d)
i. The maximum absolute difference between my central difference result and np.gradient is 0.0, meaning that in the interior np.gradient uses exactly the same second order central difference: (f(i+1) − f(i−1)) / (2h).
ii. At the edges, there is no neighbor on one side, so np.gradient uses a first order difference. The absolute error at the edges is 0.0252 K/m, while the relative error is 34%; in comparison, the absolute error in the interior point next to the edge is 6.0e-03 K/m, while the relative error is 4.6%. 
The two schemes have different truncation errors, which come from the terms dropped from the Taylor series. For the one-sided difference the leading error term is (h/2)·f'', which is O(h). For the central difference the f″ terms cancel and the leading error term is (h^2/6)·f''', which is O(h^2). Since h = 0.1 m, h^2 is ten times smaller than h, so the central difference is more accurate.

e) The arrows shown in t_plate_flow.png po outward because -∇T points in the direction of decreasing temperature. Moreover, the lines are perpendicular to the contours, since it's perpendicular to the lines of constant value.

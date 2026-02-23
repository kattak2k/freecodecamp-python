def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target
    else:
        low = 0
        high = max(1, square_target)
        root = None

        for _ in range(max_iterations):
            mid = (low + high) / 2
            square = mid ** 2

            if abs(high - low) <= tolerance:
                root = mid
                break
            elif square < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations")
            return None

        print(f"The square root of {square_target} is approximately {root}")
        return root



square_root_bisection(0.25, 1e-7, 50)
square_root_bisection(225, 1e-3, 100)
square_root_bisection(225, 1e-7, 100)
square_root_bisection(225, 1e-7, 10)
square_root_bisection(225, 1e-7, 10)


# The square root of 0.25 is approximately 0.4999999701976776
# The square root of 225 is approximately 15.000200271606445
# The square root of 225 is approximately 15.000000022700988
# Failed to converge within 10 iterations
# Failed to converge within 10 iterations




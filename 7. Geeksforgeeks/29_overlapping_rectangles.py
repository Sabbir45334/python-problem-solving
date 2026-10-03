# Check whether two rectangles overlap.
#
# Rectangle 1: (l1, b1) and (r1, t1)
# Rectangle 2: (l2, b2) and (r2, t2)
#
# l = left, r = right
# b = bottom, t = top


def do_rectangles_overlap(rect1, rect2):
    l1, b1, r1, t1 = rect1
    l2, b2, r2, t2 = rect2

    # If one rectangle is completely to the left/right
    # or completely above/below the other, they do not overlap.
    if r1 <= l2 or r2 <= l1 or t1 <= b2 or t2 <= b1:
        return False

    return True


rectangle1 = tuple(map(int, input("Enter Rectangle 1 coordinates: ").split()))
rectangle2 = tuple(map(int, input("Enter Rectangle 2 coordinates: ").split()))

if do_rectangles_overlap(rectangle1, rectangle2):
    print("Rectangles overlap.")
else:
    print("Rectangles do not overlap.")
##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    randSelect.py
#    randomized selection
#
#    includes functions provided and function students need to implement
#
##########################################################################


# TODO: implement this function
# ray is a list of ints
# index is an int
import random


def randSelect(ray, index):
    print("Looking for value with rank " + str(index) + " in the array:")
    print(ray)
    ray_len = len(ray)
    if index < 0 or index > ray_len - 1:
        raise ValueError("invalid index value!")
    # brute force
    elif ray_len < 5:
        for i in range(ray_len):
            # bubbling biggest of 0 to i-th at i
            for j in range(i):
                if ray[j] > ray[i]:
                   n = ray[i]
                   ray[i] = ray[j]
                   ray[j] = n
        t = ray[index]
        print("array's length is less than 5, brute force find: " + str(t) + " ; its rank is " + str(index)
              + "; Thus, We are done.")
        return t
    else:
        rand = random.randrange(0, ray_len)
        pivot = ray[rand]
        # swap pivot and ray[0]
        p_0 = ray[0]
        ray[0] = pivot
        ray[rand] = p_0
        # sentinel from 1
        left = 1
        right = ray_len - 1
        # no cross
        while left < right:
            while ray[left] < pivot:
                if left == ray_len - 1:
                    break
                else:
                    left += 1
            while ray[right] > pivot:
                if left == 0:
                    break
                else:
                    right -= 1
            # if no cross, then swap
            if left < right:
                inter = ray[left]
                ray[left] = ray[right]
                ray[right] = inter
        # swap pivot and right
        r_inter = ray[right]
        ray[right] = pivot
        ray[0] = r_inter
        pivot_rank = right
        # find rank
        if pivot_rank == index:
            print("Selected " + str(pivot) + " as the pivot; its rank is " + str(pivot_rank)
                  + "; Thus, we recurse on nothing. We are done.")
            return pivot
        # less than rank
        elif pivot_rank < index:
            print("Selected " + str(pivot) + " as the pivot; its rank is " + str(pivot_rank)
                  + "; Thus, we recurse on right.")
            return randSelect(ray[pivot_rank + 1:], index - (pivot_rank + 1))
        # more than rank
        else:
            print("Selected " + str(pivot) + " as the pivot; its rank is " + str(pivot_rank)
                  + "; Thus, we recurse on left.")
            return randSelect(ray[:pivot_rank], index)


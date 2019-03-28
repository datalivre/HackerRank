# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference

def difference(m, n):
    return '\n'.join(sorted(m.symmetric_difference(n), key=int))


if __name__ == "__main__":
    m_arr, n_arr = [set(input().split()) for _ in range(4)][1::2]
    print(difference(m_arr, n_arr))

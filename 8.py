from main import matrix_mul


def output_matrix_mul(v1, v2, M):
    """
    a function that requires 2 matrixes and an integer representing their length gives us an output of the
    multiplication method of the two matrixes
    :param v1: vertical matrix
    :param v2:horizontal matrix
    :param M: the length of the matrixes
    :return: None
    """
    v3 = matrix_mul(v1, v2, M)
    for i in range(len(v3)):
        print(*(str(v1) + "X" if i == int((M - 1) / 2) else (" " for i2 in range(M + 9))), v2[i],
              *(" " for i3 in range(M)), v3 if i == int((M - 1) / 2) else "")

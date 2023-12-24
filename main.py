def BoubleSort(arr:list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def Reverse(arr:list) -> list:
    pass


if __name__ == "__main__":
    mass = [1,2,9,3,8,23,9,228,3]
    mass = BoubleSort(mass)
    mass2 = Reverse(mass)
    mass.reverse()
    if mass == mass2:
        print("Ok")
    else:
        print("Not Work")

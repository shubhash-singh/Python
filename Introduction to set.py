def average(array):
    set_Array = set(array)
    result_array = list(set_Array)
    average = sum(result_array)/len(result_array)
    return average
    
if __name__ == '__main__':
    n = int(input("Enter the length"))
    arr = list(map(int, input("Enter the element with a space gap: ").split()))
    result = average(arr)
    print(result)
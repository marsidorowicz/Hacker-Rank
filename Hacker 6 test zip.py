def compare_triplets1(a, b):
    results = []
    x=y=0
    for a_value, b_value in zip(a, b):
        results.append((x+=1) if a_value > b_value else -1 if a_value < b_value else 0)

    return results
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = map(int, raw_input().rstrip().split())
    a = [5, 6, 7]
    #b = map(int, raw_input().rstrip().split())
    b = [3, 6, 10]
    result = compare_triplets1(a, b)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

# test
print(compare_triplets1([1, 2, 3], [3, 2, 1]))
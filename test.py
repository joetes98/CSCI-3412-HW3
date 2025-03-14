def main():

    # for i in range(-1, 8):
    #     print(i)

    data = [1, 7, 4, 1, 10, 9, -2]
    pivot = data[6]
    data[0], data[6] = data[6], data[0]
    print(data)
    print(pivot)
    
if __name__ == '__main__':
    main()
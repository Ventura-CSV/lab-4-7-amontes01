def main():
    numbers = []
    
    previous_input = int(input("Enter an integer: "))
    numbers.append(previous_input)
    while True:
        current_input = int(input("Enter an integer: "))
        if current_input > previous_input:
            break
        else:
            numbers.append(current_input)
            previous_input = current_input

    

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()

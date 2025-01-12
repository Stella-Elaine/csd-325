def main():
    number_of_bottles = int(input("Enter number of bottles: "))
    while number_of_bottles > 0:
        if number_of_bottles == 1:
            print(f"{number_of_bottles} bottle of beer on the wall, {number_of_bottles} bottle of beer.")
            print(f"Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")

            break
        else:
            print(f"{number_of_bottles} bottle(s) of beer on the wall, {number_of_bottles} bottle(s) of beer.")
            number_of_bottles = number_of_bottles - 1
            print(f"Take one down and pass it around, {number_of_bottles} bottle(s) of beer on the wall.\n")
    print("Time to buy more bottles of beer.")
main()

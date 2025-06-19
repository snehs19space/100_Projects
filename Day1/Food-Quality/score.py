def check_food_quality(score):
    if score > 50:
        return "Good Quality"
    else:
        return "Bad Quality"
      
def main():
    try:
        score = float(input("Enter food quality score (0–100): "))
        if score < 0 or score > 100:
            print("Invalid score. Enter a number between 0 and 100.")
        else:
            result = check_food_quality(score)
            print("Food is of", result)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

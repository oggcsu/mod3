def main():
  valid = False

  while not valid:
    try: 
      meal_charge = float(input("Enter the meal charge:"))
      valid = True
    except:
      pass

  tip = 0.18 * meal_charge 
  tax = 0.07 * (meal_charge + tip)
  total = meal_charge + tip + tax

  print(f"The meal costs: {meal_charge:.2f} ")
  print(f"The tip is: {tip:.2f}")
  print(f"The tax is: {tax:.2f}")
  print(f"The total price is: {total:.2f}")

if __name__ == "__main__":
  main()
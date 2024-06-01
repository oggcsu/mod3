def main():
  valid = False
  while not valid:
    try: 
      current_time = int(input("Enter the current time in hours: "))
      valid = True
      if current_time > 23 or current_time < 0:
        raise ValueError("The hour must be between 0 and 23")
      set_alarm = int(input("How many hours until the alarm: "))
      if set_alarm < 0:
        raise ValueError("The time must be positive")
    except:
      pass 
  alarm_time = (current_time + set_alarm) % 24 
  print(f"The alarm will go off at hour: {alarm_time}")
  
if __name__ == '__main__':
  main()

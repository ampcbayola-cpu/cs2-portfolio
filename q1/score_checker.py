score = int(input("Enter your score!: "))

if score < 0 or score > 100:
    print("Invalid Score.")
  #dont forget indents ohmydays #learning
elif score >= 90:
    print("Outstanding-!!!")
elif score >= 80:
    print("Very Satisfactory")
elif score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement...")

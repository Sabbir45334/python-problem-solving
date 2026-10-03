# # Write a menu driven program - 1.cm to ft  2.kl to miles  3.GBP to BDT  4.exit
while True:
    print("\nMenu:")
    print("1. Convert centimeters to feet")
    print("2. Convert kilometers to miles")
    print("3. Convert GBP to BDT")
    print("4. Exit")

    print("\nPlease select an option (1-4):")
    choice = input()

    if choice == '1':
        cm = float(input("Enter length in centimeters: "))
        ft = cm / 30.48
        print(f"{cm} cm is equal to {ft:.2f} ft.")
    elif choice == '2':
        kl = float(input("Enter distance in kilometers: "))
        miles = kl * 0.621371
        print(f"{kl} km is equal to {miles:.2f} miles.")
    elif choice == '3':
        gbp = float(input("Enter amount in GBP: "))
        bdt = gbp * 115.00  # Assuming 1 GBP = 115 BDT
        print(f"{gbp} GBP is equal to {bdt:.2f} BDT.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")





# import time
# import os

# def clear():
#     os.system("cls" if os.name == "nt" else "clear")

# def loading():
#     print("\033[96mLoading", end="")
#     for i in range(3):
#         time.sleep(0.4)
#         print(".", end="")
#     print("\033[0m")
#     time.sleep(0.3)

# while True:
#     clear()

#     print("\033[96m╔══════════════════════════════════════╗\033[0m")
#     print("\033[96m║       🌟 UNIT CONVERTER 🌟          ║\033[0m")
#     print("\033[96m╠══════════════════════════════════════╣\033[0m")
#     print("\033[93m║  1️⃣  CM  → Feet                     ║\033[0m")
#     print("\033[92m║  2️⃣  KM  → Miles                    ║\033[0m")
#     print("\033[95m║  3️⃣  USD → INR                      ║\033[0m")
#     print("\033[91m║  4️⃣  Exit                           ║\033[0m")
#     print("\033[96m╚══════════════════════════════════════╝\033[0m")

#     choice = input("\n\033[97m👉 Enter your choice: \033[0m")

#     if choice == "1":
#         loading()
#         cm = float(input("\nEnter centimetres: "))
#         feet = cm / 30.48
#         print(f"\033[92m✅ {cm} cm = {feet:.2f} feet\033[0m")
#         input("\nPress Enter to continue...")

#     elif choice == "2":
#         loading()
#         km = float(input("\nEnter kilometres: "))
#         miles = km * 0.621371
#         print(f"\033[92m✅ {km} km = {miles:.2f} miles\033[0m")
#         input("\nPress Enter to continue...")

#     elif choice == "3":
#         loading()
#         usd = float(input("\nEnter USD: "))
#         inr = usd * 88
#         print(f"\033[92m✅ ${usd} = ₹{inr:.2f}\033[0m")
#         input("\nPress Enter to continue...")

#     elif choice == "4":
#         print("\n\033[96m✨ Thank you for using Unit Converter! ✨\033[0m")
#         time.sleep(1)
#         break

#     else:
#         print("\033[91m❌ Invalid choice! Please select 1-4.\033[0m")
#         time.sleep(1.5)
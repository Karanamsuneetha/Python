def main():
    s = input("Enter the day: ").strip().lower()
    a = int(input("Enter the number of days: "))
    m = {
        "mon": 6, "tue": 5, "wed": 4,
        "thu": 3, "fri": 2, "sat": 1,
        "sun": 0
    }
    if s not in m:
        print("Invalid day input. Please enter a valid day abbreviation.")
        return

    ans = 0

    if a - m[s[:3]] >= 1:
        ans = 1 + (a - m[s[:3]]) // 7
    print(ans)
if __name__ == "__main__":
    main()

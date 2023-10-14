print("1.CPM \n2.TMC \n3.BJP")
vote = int(input("Caste your vote:"))
choice = ["CPM","TMC","BJP"]

match vote:
    case 1:
        print(f"Vote casted to {choice[0]}")
    case 2:
        print(f"Vote casted to {choice[1]}")
    case 3:
        print(f"Vote casted to {choice[2]}")
    case _:
        print("Invalid choice")
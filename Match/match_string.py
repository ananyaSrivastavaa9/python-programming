command = "start"
match command:
    case "start":
        print("System Started")
    case "stop":
        print("System Stopped")
    case "restart":
        print("System Restarted")
    case _:
        print("INVALID")
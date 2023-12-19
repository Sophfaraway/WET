
pozdrav = "Helloo"

if pozdrav == "Helloo":
    print("Helloo")
elif pozdrav == "Hii":
    print("Hii")

match pozdrav: #switch in js 

    case "Helloo"|"Hello":
        print("Helloo")
    case "Hii":
        print("Hii")
    case "What up":
        print("What up")
    case _: #default
        print("gretting wasn't chosen")
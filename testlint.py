Captain = "Picard"


def InitiateWarpSpeed(order):
    if order == "engage":
        print("initiating warp speed")
    else:
        print("you are not the captain of this vessel")


InitiateWarpSpeed("engage")

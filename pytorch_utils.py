def moveTo(obj, device):
    """
    obj: The python object to move to device, or to move its content to a device
    device: the compute device to move objects to
    """

    if isinstance(obj, list):
        return [moveTo(x,device) for x in obj]
    elif isinstance(obj, tuple):
        return tuple(moveTo(list(obj), device))
    elif isinstance(obj, set):
        return set(moveTo(list(obj), device))
    elif isinstance(obj, dict):
        to_ret = dict()
        for key, value in obj.items():
            to_ret[moveTo(key, device)] = moveTo(value, device)
        return to_ret
    elif hasattr(obj, "to"):
        return obj.to(device)
    else: 
        return obj
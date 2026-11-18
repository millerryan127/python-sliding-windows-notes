

def solve(value):
    return [value["items"][i:i+value["width"]] for i in range(len(value["items"])-value["width"]+1)] if value["width"] > 0 else (_ for _ in ()).throw(ValueError("width must be positive"))

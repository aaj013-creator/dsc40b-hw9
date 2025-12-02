def learn_theta(data, colors):
    max_blue = float("-inf")
    min_red = float("inf")
    for x, c in zip(data, colors):
        if c == "blue":
            if x > max_blue:
                max_blue = x
        else:
            if x < min_red:
                min_red = x
    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):
    loss = 0
    for x, c in zip(data, colors):
        if c == "red" and x <= theta:
            loss += 1
        elif c == "blue" and x > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    pairs = list(zip(data, colors))
    pairs.sort()
    xs = [x for x, c in pairs]
    cs = [c for x, c in pairs]

    best_theta = None
    best_loss = float("inf")

    for i in range(len(xs) - 1):
        theta = (xs[i] + xs[i+1]) / 2
        loss = compute_ell(xs, cs, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return best_theta


def minimize_ell_sorted(data, colors):
    total_blue = colors.count("blue")
    blue_leq = 0
    red_leq = 0

    best_theta = None
    best_loss = float("inf")

    for i in range(len(data) - 1):
        if colors[i] == "blue":
            blue_leq += 1
        else:
            red_leq += 1

        blue_gt = total_blue - blue_leq
        loss = red_leq + blue_gt
        theta = (data[i] + data[i+1]) / 2

        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return best_theta

solution = []

def shorten_solution(segment):
    y_count = segment.count("y")
    y_prime_count = segment.count("y\'")
    U_count = segment.count("U")
    U_prime_count = segment.count("U\'")

    result = []

    # 'y' 최적화
    y = y_count - y_prime_count
    if y < 0:
        y = -y
        if y >= 4:
            y = y % 4
        if y == 1:
            result.append("y\'")
        elif y == 2:
            result.append("y\'")
            result.append("y\'")
        elif y == 3:
            result.append("y")
    else:
        if y >= 4:
            y = y % 4
        if y == 1:
            result.append("y")
        elif y == 2:
            result.append("y")
            result.append("y")
        elif y == 3:
            result.append("y\'")

    # 'U' 최적화
    U = U_count - U_prime_count
    if U < 0:
        U = -U
        if U >= 4:
            U = U % 4
        if U == 1:
            result.append("U\'")
        elif U == 2:
            result.append("U\'")
            result.append("U\'")
        elif U == 3:
            result.append("U")
    else:
        if U >= 4:
            U = U % 4
        if U == 1:
            result.append("U")
        elif U == 2:
            result.append("U")
            result.append("U")
        elif U == 3:
            result.append("U\'")

    return result


# y, y', U, U' 걸러내기

def split_by_target(seq, targets={"y", "y'", "U", "U'"}):
    if not seq:
        return []

    result = []
    current = [seq[0]]
    in_target = seq[0] in targets

    for move in seq[1:]:
        now_target = move in targets
        if now_target == in_target:
            current.append(move)
        else:
            result.append(current)
            current = [move]
            in_target = now_target

    result.append(current)
    return result

def process_with_shortening(moves, targets={"y", "y'", "U", "U'"}):
    segments = split_by_target(moves, targets)
    result = []

    for segment in segments:
        if segment[0] in targets:
            result.extend(shorten_solution(segment))
        else:
            result.extend(segment)

    return result

solution = process_with_shortening(solution)
# version 1.0

SUBJECTS = ["국어", "영어", "수학", "과탐"]


def get_scores():
    scores = {}

    for subject in SUBJECTS:
        score = float(input(f"{subject} 점수: "))
        scores[subject] = score

    return scores


def calculate_average(scores):
    return sum(scores.values()) / len(scores)


def find_highest(scores):
    return max(scores, key=scores.get)


def find_lowest(scores):
    return min(scores, key=scores.get)


def print_results(scores, average):
    print("점수 결과")

    for subject, score in scores.items():
        print(f"{subject}: {score}")

    print("평균:", average)

    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("최고 점수 과목:", highest)
    print("최저 점수 과목:", lowest)


if __name__ == "__main__":
    scores = get_scores()

    average = calculate_average(scores)

    print_results(scores, average)
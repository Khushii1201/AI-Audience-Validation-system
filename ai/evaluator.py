def evaluate_answer(
        user_answer,
        correct_answer
):

    if not user_answer:
        return 0

    user_answer = user_answer.lower().strip()
    correct_answer = correct_answer.lower().strip()

    if user_answer == correct_answer:
        return 100

    user_words = set(
        user_answer.split()
    )

    correct_words = set(
        correct_answer.split()
    )

    common_words = user_words.intersection(
        correct_words
    )

    if len(correct_words) == 0:
        return 0

    similarity = (
        len(common_words)
        /
        len(correct_words)
    )

    return int(
        similarity * 100
    )
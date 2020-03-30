def get_answer(prompt=""):
    """
    :param prompt: Some question
    :return: Get Yes or Not answer from user. returns True or False
    """
    prompt += "?" if prompt.endswith("?") else ""

    answers = {
        "yes": True,
        "no": False
    }
    while True:
        user_input = input(f"{prompt} (Yes/No)").lower()
        answer = answers.get(user_input)
        if answer is not None:
            return answer


def main():
    answer = get_answer()


if __name__ == "__main__":
    main()

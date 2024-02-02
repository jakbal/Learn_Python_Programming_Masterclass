def banner_text(text: str = " ", user_width: int = 80) -> None:
    """
    Print banner text when simply text is specified
    or print series of `*` when just `*` is given

    :param text: string value specified by user
    :param user_width: integer value specified by user
    :raises ValueError: if the supplied string is too long to fit
    """
    screen_width = user_width
    if len(text) >= screen_width - 4:
        raise ValueError("String {0} is larger than specified widht {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)

banner_text("*")

from urllib import request

HEADERS = {"User-Agent": "ign"}
BASE_URL = "https://www.toptal.com/developers/gitignore/api"


def get_template_list() -> list[str]:
    response = (
        request.urlopen(
            request.Request(f"{BASE_URL}/list", headers=HEADERS)
        )
        .read()
        .decode("utf-8")
    )

    template_list = []
    for line in map(str, response.split("\n")):
        template_list.extend(line.split(","))

    return template_list


def get_gitignore(gi_stack: list[str]) -> str:
    """HTTP Get gitignore.

    Args:
        gi_stack: A list of strings of names of tech to include ex. ['sass', 'node', 'macos']

    Returns:
        HTTP response text.

    """

    template_list = get_template_list()

    for tech in gi_stack:
        if tech.lower() not in template_list:
            raise ValueError(tech)  # Reports iffy item in the list

    comma_delimited = ",".join(gi_stack)
    response = (
        request.urlopen(
            request.Request(f"{BASE_URL}/" + comma_delimited, headers=HEADERS,)
        )
        .read()
        .decode("utf-8")
    )

    return response

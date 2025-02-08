import re


def main():
    print(parse(input("HTML: ")))

#  src="https://www.youtube.com/embed/xvFZjo5PgG0"
def parse(s):
    if x := re.search(r'^.*iframe src=\"(?:https?://)?(?:w{3}\.)?youtube\.com/(?:embed/)?([a-zA-Z0-9_-]{11})\".*$', s, re.IGNORECASE): # youtube video id length is 11
        return f"https://youtu.be/{x.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
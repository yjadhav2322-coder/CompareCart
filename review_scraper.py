import requests
from bs4 import BeautifulSoup


url = "https://dl.flipkart.com/s/XYAygrNNNN"


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-IN,en;q=0.9"
}


response = requests.get(
    url,
    headers=headers,
    timeout=15
)


print("Status Code:", response.status_code)
print("Final URL:", response.url)


soup = BeautifulSoup(
    response.text,
    "html.parser"
)


reviews = soup.select(
    '[data-hook="review"]'
)


print("Reviews found:", len(reviews))


for review in reviews[:5]:

    reviewer = review.select_one(
        '[class="a-profile-name"]'
    )

    rating = review.select_one(
        '[data-hook="review-star-rating"]'
    )

    if rating is None:
        rating = review.select_one(
            '[data-hook="cmps-review-star-rating"]'
        )

    comment = review.select_one(
        '[data-hook="review-body"]'
    )


    print("\n----------------------")

    print(
        "Name:",
        reviewer.get_text(
            " ",
            strip=True
        )
        if reviewer
        else "Not found"
    )

    print(
        "Rating:",
        rating.get_text(
            " ",
            strip=True
        )
        if rating
        else "Not found"
    )

    print(
        "Review:",
        comment.get_text(
            " ",
            strip=True
        )
        if comment
        else "Not found"
    )
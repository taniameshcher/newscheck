import datetime

import requests


def from_utc(utcTime, fmt="%Y-%m-%dT%H:%M:%fZ"):
    """
    Convert UTC time string to time.struct_time
    """
    # change datetime.datetime to time, return time.struct_time type

    return datetime.datetime.strptime(utcTime, fmt)  # . .replace(second=0, microsecond=0))


# printing title, Posted datetime and description
response = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=edf78a83063943ffabc69e15c78e2f93')
data = response.json()

for article in data["articles"]:
    publishedAt = str(article["publishedAt"])
    timestamp = from_utc(publishedAt)
    timeToPrint = '{}-{}-{} {}:{}'.format(timestamp.day, timestamp.month, timestamp.year, timestamp.hour,
                                          timestamp.minute)
    print("------------------------")
    print("Title:\t\t", article["title"], "\nPosted on:\t", timeToPrint)
    print("Text:\t\t", article["description"])
print("------------------------")

print(type(data))




# from_utc("2007-03-04T21:08:12.123Z")
# gt(data["articles"][0]["publishedAt"])

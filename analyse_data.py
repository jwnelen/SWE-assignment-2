import json

if __name__ == '__main__':
    result = []

    with open('fetched_tweets.txt', 'r') as tf:
        for line in tf:
            result.append(json.loads(line))

    print(len(result))
    for obj in result:
        print(obj)
        print(obj["user"]["location"])

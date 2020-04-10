import requests


def main():
    ID = 1
    POST_PATH = "addDataPoint/{}".format(ID)
    SERVER_HOST = "ec2-18-189-21-31.us-east-2.compute.amazonaws.com"

    data = requests.get("http://127.0.0.1/api/weather").json()
    print(data)
    r = requests.post("http://{SERVER_HOST}/{POST_PATH}".format(SERVER_HOST=SERVER_HOST, POST_PATH=POST_PATH),
                      json=data)
    print(r.content)


if __name__ == "__main__":
    main()

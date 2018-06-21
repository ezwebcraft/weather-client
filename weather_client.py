import requests

def main():
    # print header
    print_the_header()

    # get zipcode from user
    code = input("Enter Zip code for the weather info you want")
    # get html from web
    get_html_from_web(code)
    # parse the html
    # display for the forcast
    print("Main section")


def print_the_header():
    print('--------------------------------------------------')
    print('                   Weather App                    ')
    print('--------------------------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    print(response.status_code)


if __name__ == '__main__':
    main()

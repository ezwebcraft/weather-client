import requests

import bs4

def main():
    # print header
    print_the_header()

    # get zipcode from user
    code = input("Enter Zip code for the weather info you want")
    # get html from web
    html = get_html_from_web(code)
    # parse the html
    get_weather_from_html(html)
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
    #print(response.status_code)
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html)
    print(soup)

if __name__ == '__main__':
    main()

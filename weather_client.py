import requests
import bs4


def main():
    # print header
    print_the_header()
    # get zipcode from user
    code = input("Enter Zip code for the weather info you want (11102): ")
    # get html from web
    html = get_html_from_web(code)
    # parse the html
    get_weather_from_html(html)
    # display for the forcastp
    print("Main section")


def print_the_header():
    print('--------------------------------------------------')
    print('                   Weather App                    ')
    print('--------------------------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    return response.text


def get_weather_from_html(html):
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-value').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    print(condition, temp, scale)


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()

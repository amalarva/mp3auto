# -*- coding: utf-8 -*-

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time
import os
import eyed3

path = input('경로를 입력하시오:', )
file_list = os.listdir(path)
file_list_mp3 = [file for file in file_list if file.endswith(".mp3")]
print("file_list_py: {}".format(file_list_mp3))


def exist(xpath):  #xpath의 존재여부 확인 함수
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)  # 업데이트 있으면 업데이트
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920,1080')
    driver.implicitly_wait(10)

driver.get('https://music.bugs.co.kr/')
driver.execute_script('window.open("https://www.melon.com/");')

Mlist = file_list_mp3
i = 0

while len(Mlist) > i:   #음악 리스트 = 작동 횟수
    try:
        mp3 = Mlist[i]
        a = len(mp3)
        b = a - 4
        title = mp3[:b]  #음악 이름-.mp3
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        if exist('//*[@id="header"]/div[2]/a'):
            driver.find_element_by_xpath('//*[@id="header"]/div[2]/a').send_keys(Keys.ENTER)
        search_box = driver.find_element_by_xpath('//*[@id="headerSearchInput"]')
        search_box.send_keys(title)
        search_box.send_keys(Keys.RETURN)

        if exist('//*[@id="DEFAULT0"]/table/tbody/tr[1]/td[3]/a'):
            driver.find_element_by_xpath('//*[@id="DEFAULT0"]/table/tbody/tr[1]/td[3]/a').send_keys(Keys.ENTER)

            if exist('//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[2]/td/a'):
                watch = driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[2]/td/a').text

            name = driver.find_element_by_xpath('//*[@id="container"]/header/div/h1').text  #공식 음악 이름
            print('제목:', name)
            if exist('//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a'):  #아티스트 뽑기
                art1 = driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a').text
                arti = art1
                if exist('//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[2]'):
                    art1 = driver.find_element_by_xpath(
                        '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[2]').text
                    arti = arti + ',' + art1
                    if exist('//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[3]'):
                        art1 = driver.find_element_by_xpath(
                            '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[3]').text
                        arti = arti + ',' + art1
                        if exist('//*[@id="container"]/section[ 1]/div/div[1]/table/tbody/tr[1]/td/a[4]'):
                            art1 = driver.find_element_by_xpath(
                                '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[4]').text
                            arti = arti + ',' + art1
                            if exist('//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[5]'):
                                art1 = driver.find_element_by_xpath(
                                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[5]').text
                                arti = arti + ',' + art1
                                if exist('//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[6]'):
                                    art1 = driver.find_element_by_xpath(
                                        '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[1]/td/a[6]').text
                                    arti = arti + ',' + art1

            print('아티스트:', arti)


                #앨범 이름 탐색
            if exist(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[2]/th') == True and driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[2]/th').text == '앨범':
                AL = driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[2]/td/a').text
                print('앨범:', AL)
                driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[2]/td/a').send_keys(Keys.ENTER)

            elif exist(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[3]/td/a') == True and driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[3]/th').text == '앨범':
                AL = driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[3]/td/a').text
                print('앨범:', AL)
                driver.find_element_by_xpath(
                    '//*[@id="container"]/section[1]/div/div[1]/table/tbody/tr[3]/td/a').send_keys(Keys.ENTER)


            driver.switch_to.window(driver.window_handles[1])   #벅스 초기화면으로
            driver.find_element_by_xpath('//*[@id="gnb"]/h1/a').send_keys(Keys.ENTER)
            time.sleep(1)

            searchbox = driver.find_element_by_xpath('//*[@id="top_search"]')
            searchbox.send_keys(name)
            searchbox.send_keys(Keys.RETURN)
            time.sleep(1)


            Iname = driver.find_element_by_xpath( '//*[@id="frm_searchSong"]/div/table/tbody/tr[1]/td[3]/div/div/a[2]').text  #멜론에 등록된 노래 제목
            driver.get('https://www.melon.com')
            searchbox = driver.find_element_by_xpath('//*[@id="top_search"]')

            searchbox.send_keys(AL)
            searchbox.send_keys(Keys.RETURN)

            driver.find_element_by_xpath('//*[@id="divCollection"]/ul/li[4]/a').send_keys(Keys.ENTER)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="frm"]/div/ul/li[1]/div/div/dl/dt/a').send_keys(Keys.ENTER)

            p = 1
            Track = 1

            while exist('//*[@id="frm"]/div/table/tbody/tr[' + str(p) + ']/td[4]/div/div/div[1]/span/a'):  #트랙 넘버 찾기 1번부터 n번까지...
                Track1 = driver.find_element_by_xpath(
                    '//*[@id="frm"]/div/table/tbody/tr[' + str(p) + ']/td[4]/div/div/div[1]/span/a').text
                if Track1 == Iname:
                    Track = p
                p = p + 1

            print('트랙정보', Track)

        else:
            time.sleep(1)

        audiofile = eyed3.load(path + '\\' + mp3)

        audiofile.tag.artist = arti #오류

        audiofile.tag.album = AL #앨범 입력
        audiofile.tag.title = Iname #제목 입력
        audiofile.tag.track_num = Track #트랙번호 입력
        audiofile.tag.save()
        i = i + 1
        print('-------------'+ mp3 +'입력 완료/다음곡-------------')

    except:
        i = i + 1
        print('------------------오류:\"' + mp3 + '\"의 입력을 수행할 수 없음. 다음곡으로 넘어감------------------')

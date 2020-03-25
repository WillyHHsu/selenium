import sys
import urllib.request

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options  
# from PIL import Image

try:
    loop_range = int(sys.argv[1])+1

except Exception as err:
    print(err)
    print('Insira um númeor inteiro') 


# chrome_options = Options()
# chrome_options.add_argument("--headless") 
# driver = webdriver.Chrome(options= chrome_options , executable_path='driver/chromedriver.exe')
# driver.get('https://cvmweb.cvm.gov.br/SWB//Sistemas/SCW/CPublica/RandomTxt.aspx?v1=0,846738362147817')

# for i in range(loop_range):
#     element = driver.find_element_by_xpath("/html/body/img")
#     location = element.location;
#     size = element.size
#     driver.save_screenshot("tmp/pageImage.png")

#     x = location['x'];
#     y = location['y'];
#     width = location['x']+size['width'];
#     height = location['y']+size['height'];
#     im = Image.open('tmp/pageImage.png')
#     im = im.crop((int(x), int(y), int(width), int(height)))
#     im.save(f'captcha/raw/element_{i}.png')
#     driver.refresh()
    
# driver.quit()



for i in range(loop_range):

    try:
        filename = "captcha/raw/" + str(i).zfill(5) + ".png"
        url = "https://cvmweb.cvm.gov.br/SWB//Sistemas/SCW/CPublica/RandomTxt.aspx?v1=0,846738362147817"
        urllib.request.urlretrieve(url, filename)
    except Exception as err:
        print(err)    
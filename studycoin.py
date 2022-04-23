#从教务系统中爬取每学期成绩
from selenium import webdriver
from time import sleep
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from lxml import etree

ro=webdriver.Edge(service=Service(r'C:\Python36\MicrosoftWebDriver.exe'))
ro.get('http://172.29.200.39/jwglxt/xtgl/login_slogin.html')
# sleep(5)
ro.implicitly_wait(10)
element=ro.find_element(By.NAME,'yhm').send_keys('学号')
element=ro.find_element(By.ID,'mm').send_keys('密码')
element=ro.find_element(By.ID,'dl').click()
sleep(8)
element=ro.find_element(By.ID,'btn_yd').click()
element=ro.find_element(By.XPATH,'/html/body/div[3]/div/nav/ul/li[4]/a').click()
element=ro.find_element(By.XPATH,'/html/body/div[3]/div/nav/ul/li[4]/ul/li[9]/a').click()

sleep(10)
ro.switch_to.window(ro.window_handles[-1])
# print(ro.title)
# for handle in ro.window_handles:
#     ro.switch_to.window(handle)
#     if '教学管理信息服务平台' in handle.title:
#         break
# fp=open('test2.html','w',encoding='utf-8')
# # sleep(10)
# fp.write(ro.page_source)
# fp.close()
# element=ro.find_element(By.XPATH,'/html/body/div[1]/div/div/form/div/div[1]/div/div/div/div/ul').click()
js = 'document.querySelectorAll("select")[0].style.display="block";'
ro.execute_script(js)
select = Select(ro.find_element(By.NAME, 'xnm'))
#/html/body/div[1]/div/div/form/div/div[1]/div/div/select/
#select.deselect_all()
select.select_by_value('2020')

# select=Select(ro.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div/div[2]/div/div/select'))
#select.deselect_all()
# select.select_by_index(1)
element=ro.find_element(By.ID,'search_go').click()
sleep(5)

tree=etree.HTML(ro.page_source)
fp=open('./爬虫/数据解析/selenium/score.txt','w',encoding='utf-8')
li_list=tree.xpath('/html/body/div[1]/div/div/div[3]/div[3]/div[4]/div/table/tbody/tr')
for i in li_list:
    result=i.xpath('./td/text()')
    for n in result:
        if n!='':
            fp.write(n+' ')
    fp.write('\n')
fp.close()
ro.quit()
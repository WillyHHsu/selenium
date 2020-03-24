from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Crawler():
    
    def __init__(self, driverpath = "driver\chromedriver.exe"):
        self.driverpath =  driverpath
    
    def open_browser(self):
        self.driver = webdriver.Chrome(self.driverpath)
    
    def insert_query(self, institution):
        """
        institution: aceita texto ou o CNPJ, sem pontos e traços
        """
        self.driver.get('https://cvmweb.cvm.gov.br/SWB//Sistemas/SCW/CPublica/CConsolFdo/FormBuscaParticFdo.aspx')
        self.driver.find_element_by_id("txtCNPJNome").send_keys(institution)
        ##insert CAPTCHA SOLVER
        self.driver.find_element_by_id("btnContinuar").click() 
    
    def get_all_funds(self):
        """
        return all names
        """
        _ = self.driver.find_element_by_id('ddlFundos').find_elements_by_tag_name('tr')

        c0 = []
        c1 = []
        c2 = []
        
        for i in _:
            c0.append([j.text for j in i.find_elements_by_tag_name('td')][0])
            c1.append([j.text for j in i.find_elements_by_tag_name('td')][1])
            c2.append([j.text for j in i.find_elements_by_tag_name('td')][2])

        return {"CNPJ":c0,"NOME":c1,"TIPO":c2}
    
    def get_dropdown(self):
        drop_down_list = [i.strip() for i in self.driver.find_element_by_name("ddComptc").text.split('\n')]
        return drop_down_list[:-1]

    def choose_document(self, doc):
        if doc == 1:
            self.driver.find_element_by_id('trInfDiar').click()

    def get_data(self, drop_down_list):
        
        drop_down_list = [i.strip() for i in self.driver.find_element_by_name("ddComptc").text.split('\n')]
        col0, col1, col2, col3,col4,col5,col6, col7, col8  = ([] for i in range(9))

        for k in range(len(drop_down_list)-1):
            Select(self.driver.find_element_by_id('ddComptc')).select_by_value(drop_down_list[k])
            for i in self.driver.find_element_by_id('dgDocDiario').find_elements_by_tag_name('tr')[1:]:
                a,b,c,d,e,f,g,h = [j.text for j in i.find_elements_by_tag_name('td')]

                col0.append(a)
                col1.append(b)
                col2.append(c)
                col3.append(d)
                col4.append(e)
                col5.append(f)
                col6.append(g)
                col7.append(h)
                col8.append(drop_down_list[k])
        
        return {'Dia':col0, 'Quota':col1, 'Captação_no_Dia':col2 
                ,'Resgate_no_Dia':col3,'Patrimônio_Líquido':col4,'Total da Carteira':col5
                ,'N°_Total_de_Cotistas':col6,'Data_da_próxima_informação_do_PL':col7
                ,'Data':[i+'/'+j for i,j in zip(col0,col8)]}
        
    def quit(self):
        self.driver.quit()
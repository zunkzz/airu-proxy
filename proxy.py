###########################
#       Meu Twitter       #
#       @Souichi285       #
###########################

import requests
from bs4 import BeautifulSoup
import os
os.system('clear')
print("""
#################################################################################
#                             aaaaaaaaaaaaaaaa               *                  #
#                         aaaaaaaaaaaaaaaaaaaaaaaa                              #
#                      aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                           #
#                    aaaaaaaaaaaaaaaaa           aaaaaa                         #
#                  aaaaaaaaaaaaaaaa                  aaaa                       #
#                 aaaaaaaaaaaaa aa                      aa                      #
#*               aaaaaaaa      aa                         a                     #
#                aaaaaaa aa aaaa                                                #
#          *    aaaaaaaaa     aaa                                               #
#               aaaaaaaaaaa aaaaaaa                               *             #
#               aaaaaaa    aaaaaaaaaa                                           #
#               aaaaaa a aaaaaa aaaaaa                                          #
#                aaaaaaa  aaaaaaa                                               #
#                aaaaaaaa                                 a                     #
#                 aaaaaaaaaa                            aa                      #
#                  aaaaaaaaaaaaaaaa                  aaaa                       #
#                    aaaaaaaaaaaaaaaaa           aaaaaa        *                #
#      *               aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                           #
#                         aaaaaaaaaaaaaaaaaaaaaaaa Airu Moonlight               #
#                      *      aaaaaaaaaaaaaaaa     放棄された Proxy               #
#################################################################################""")

resposta = requests.get('https://free-proxy-list.net/')
bs = BeautifulSoup(resposta.text, 'lxml')

table = bs.find('table')
linhas = bs.find_all('tr')

for linha in linhas:
    ip = linha.contents[0].text
    porta = linha.contents[1].text
    anonimo = linha.contents[4].text
    segundos = linha.contents[6].text

    if(segundos == 'yes' and (anonimo == 'anonymous' or anonimo == 'elite proxy')):
        airu = 'http://' + ip + ':' + porta
        proxies = {'http': airu, 'https': airu}

        try:
            testIP = requests.get('https://httpbin.org/ip', proxies = proxies , timeout = 3)
            print(testIP.text)
            resIP = testIP.json()['origin']
            origin = resIP.append(',')

            if origin[0] == ip:
                print('Proxy bom !!')
                count += 1

                if count == 5:
                    break

        except:
            print('Proxy queimado!')

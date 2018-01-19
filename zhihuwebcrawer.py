import requests
import json
import time
link = \"https://www.zhihu.com/api/v4/answers/261987577/voters?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cfollower_count%2Cgender%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=10&offset=\"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6', 'Host' : 'www.zhihu.com', 'authorization' : 'Bearer 2|1:0|10:1512711299|4:z_c0|92:Mi4xOWMxckFBQUFBQUFBWUVKeWI1TE1EQ2NBQUFDRUFsVk5nN0ZSV2dCa243MVppbFRNZnhrWFNrazN0V1h5WXlpb0hn|c9a040323654225d2d9c49537cb35e23c8ec097d5a1770632edc7c0ac1ac0743'}
link2 = \"https://www.zhihu.com/api/v4/members/\"
link3 = \"/followees?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&limit=20&offset=\"
diction = {}
diction2 = {}
outf = open('zhihuout.txt',\"r+\",encoding='utf-8')
def get_follower(eachPeople):
    link_people = link2 + eachPeople + link3
    flag2 = True
    i2 = 0
    diction2[eachPeople] = {}
    while flag2:
        r2 = requests.get(link_people + str(i2*20), headers = headers)
        json_data2 = json.loads(r2.text)
        try:
            if len(json_data2['data']) == 0 :
                flag2 = False
                break
            for eachData in json_data2['data']:
                diction2[eachPeople][eachData['url_token']] = eachData['name']
                outf.write(eachData['url_token']+\"^\")
                print (diction[eachPeople]+\" followed \"+eachData['name'])
        except:
            outf(\"an error occurred here with \"+ eachPeople + \" named \"+ diction[eachPeople] + \"\\n\")
            break
        i2 = i2 + 1
flag = True
i = 0
while flag:
    r = requests.get(link + str(i*10), headers = headers)
    #print (link + str(i) +'0')
    json_data = json.loads(r.text)
    #print (r.text)
    #print (len(json_data['data']))
    for eachData in json_data['data']:
        print (eachData['name'])
        if eachData['url_token'] == \"\":
            continue
        if (eachData['url_token'] in diction):
            flag = False
            break
        diction[eachData['url_token']] = eachData['name']
        outf.write(str(i)+\"^\"+eachData['url_token']+\"^\"+eachData['name']+\"^\")
        get_follower(eachData['url_token'])
        outf.write(\"\\n\")
    i = i + 1
    #print (len(diction))
    #time.sleep(3)
print (len(diction))
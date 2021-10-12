import requests
import json

def navigation(store, slug, content_no):
    while True:
        Next=content_no
        select=input("choose your navigations: \n you wanto to go up, next, back: ")
        if select=='up': 
            Next=Next-1
            R=requests.get("http://saral.navgurukul.org/api/courses/"+str(store)+"/exercise/getBySlug?slug="+str(slug[Next]))
            R_data=R.json()
            print(R_data['content'])
            print(Next)
        elif select=='next':
            Next=Next+1
            Rq=requests.get("http://saral.navgurukul.org/api/courses/"+str(store)+"/exercise/getBySlug?slug="+str(slug[Next-1]))
            Rq_data=Rq.json()
            print(Rq_data['content'])
            print(Next)
        elif select=='back':
            link=requests.get("https://saral.navgurukul.org/api/courses/"+str(store)+"/exercises")
            n_data=link.json()
            cnt=1
            for j in n_data['data']:
                print(cnt,j['name'])
                cnt+=1
        else:
            break
def all_courses ():
    a=requests.get('http://saral.navgurukul.org/api/courses')
    b=a.json()
    
    file=open('courses.json', "w")
    json.dump(b, file, indent = 6)
    file.close()
    
    with open('courses.json',"r") as f:
        data =json.load(f)
    f.close()
    empty=[]
    c=1
    for i in data["availableCourses"]:
        print(c,i['name'],i['id'])
        empty.append(i['id'])
        c+=1   
    num=int(input("enter a Course-id: "))    
    store=empty[num-1]
    m=requests.get("https://saral.navgurukul.org/api/courses/"+str(store)+"/exercises")
    new_data=m.json()
    count=1
    slug=[]
    for key in new_data['data']:
        print(count,key['name'])
        slug.append(key['slug'])
        count+=1
    content_no=int(input("enter content number: "))
    req=requests.get("http://saral.navgurukul.org/api/courses/"+str(store)+"/exercise/getBySlug?slug="+str(slug[content_no-1]))
    req_data=req.json()
    print(req_data['content'])
    navigation(store, slug, content_no)
all_courses()
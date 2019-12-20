from collections import deque

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()#새 큐를 생성
    search_queue += graph[name]
    searched = []#확인 한 사람 저장용

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:#확인 하지 않은 사람 확인 , 확인한 사람 나오면 무한루프
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)#끝에 m이 들어가지 않는 사람 저장  

    return False

search("you")
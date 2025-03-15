import json

def load_data() :
    try:
        with open("youtube.txt" , "r") as file:
            test = json.load(file)
            # print(test)
            # print(type(test))
            return test
    except FileNotFoundError :
        return []

def save_data_helper(videos) :
    with open('youtube.txt' , 'w') as file :
        json.dump(videos , file)
        
def list_all_videos(videos) :
    videos_data = enumerate(videos , start=1)
    print("\n")
    print("*" * 60 ,end="")
    print("\n")
    for index , video in videos_data:
        print(f"{index}: {video['name']}, Duration: {video['time']} ") 
    print("*" * 60 ,end="")

def add_video(videos) :
    name = input("Enter video name :- ")
    time = input("Enter video time :- ")
    videos.append({'name' : name , 'time' : time})
    save_data_helper(videos)
    

def update_videos(videos) :
    list_all_videos(videos)
    index = int(input("\nEnter the video number to update :- "))
    if 1 <= index <= len(videos):
        name = input("Enter new video name :- ")
        time = input("Enter new video time :- ")
        videos[index-1] = {'name' : name , 'time' : time}
        save_data_helper(videos)
    else :
        print("Invalid indes selected")
        if 1 <= index <= len(videos):
            del videos[index-1]
            save_data_helper(videos)
        else:
            print("invalid index selected")

def delete_videos(videos) :
    list_all_videos(videos)
    index = int(input("Enter the video number to be updated :- "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else :
        print("invalid index selected")
    

def main() :
    videos = load_data()
    # print(videos)
    while True :
        print("\n Youtube Manager | choose an option \n")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube videos ")
        print("4. Delete a youtube videos ")
        print("5. Exit the app ")
        choice = input("Enter your choice :- ")
        
        match choice :
            case '1':
                list_all_videos(videos)

            case '2' :
                add_video(videos)

            case '3' :
                update_videos(videos)

            case '4' :
                delete_videos(videos)

            case '5' :
                break
            case _:
                print("Invalid choice please enter the correct choice ")

if __name__ == "__main__" :
    main()
        
            
            
    
    
    
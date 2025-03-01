
import json


def load_data():
    try:
        with open("youtube.txt",'r') as file:
            test= json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(video):
    with open('youtube.txt','w') as file:
        json.dump(video,file)

def list_all_videos(video):
    print("\n")
    print("*" * 20)
    for index, videos in enumerate(video, start=1):
        print(f"{index}. {videos['name']},Duration: {videos['time']}")
    print("\n")
    print("*" * 20)

def add_video(video):
    name=input("Enter video name:")
    time=input("Enter video time:")
    video.append({'name': name, 'time':time})
    save_data_helper(video)

def update_video(video):
    list_all_videos(video)
    index=int(input("Enter the video to update"))
    if 1 <= index <= len(video):
        name=input("Enter the new video name")
        time=input("Enter the new video time")
        video[index-1] = {'name':name, 'time':time}
        save_data_helper(video)
    else:
        print("Invalid index selected")

def delete_video(video):
    list_all_videos(video)
    index = int(input("Enter the video number to be deleted"))
    if 1 <= index <= len(video):
        del video[index-1]
        save_data_helper(video)
    else:
        print("Invalid video index selected")
    

def main():
    video = load_data()
    

    while True:
        print("\n Youtube manager")
        print("1. List all youtube videos.")
        print("2. Add a youtube videos.")
        print("3. Update a youtube video details.")
        print("4. Delete a youtube video.")
        print("5. Exit the app.")
        choice = input("Enter your choice: ")
        # print(video)
        match choice:
            case '1':
                list_all_videos(video)
            case '2':
                add_video(video)
            case '3':
                update_video(video)
            case '4':
                delete_video(video)
            case '5':
                break
            case _:
                print("Invalid choice")
if __name__=="__main__":
    main() 

















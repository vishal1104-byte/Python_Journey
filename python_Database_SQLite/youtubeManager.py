import sqlite3            # This is the way to import sqlite

conn = sqlite3.connect('Youtube_Videos.db')         # With this we can connect with the database 

cursor = conn.cursor()    # This is the method to take conn as a variable which is used everytime

cursor.execute('''                                       
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TAXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time))
    conn.commit()

def Update_videos(videoId,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id = ?",(new_name,new_time,videoId))
    conn.commit()

def Delete_videos(videoId):
    cursor.execute("DELETE FROM videos where id = ?",(videoId,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager app with Database")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input('Enter Your choice: ')

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the Video name: ")
            time = input("Enter the Video time: ")
            add_videos(name,time)
        elif choice == "3":
            videoId = input("Enter a Video Id to Update: ")
            name = input("Enter the Video Name: ")
            time = input("Enter the Video time: ")
            Update_videos(videoId,name,time)
        elif choice == "4":
            videoId = input("Enter the Video Id to delete: ")
            Delete_videos(videoId)
        elif choice == "5":
            break
        else:
            print("Invalid Choice . Please choose the Valid Option")
    conn.close()

if __name__ == '__main__':
    main()
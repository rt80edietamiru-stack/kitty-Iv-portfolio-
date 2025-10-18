import os
from datatime import datetime


SYSTEM_NAME="Rheanova Task System"
VERSION = "Phase 1.0"
AUTHOR = "Alex"
 

 def log_event(event):
     log-dir = "logs"
     os .makedirs(log_dir, exist_ok=True)
     with open(os.path.join(log_dir, "system_log.txt"),"a") as log_file: timestamp = datetime.now
     ().strftime("%Y-%m-5d %H:%M:%S")
     log_file.write(f"[{timestamp}]{event}/n")


     def initialize_system():
         print(f"Initializing {SYSTEM_NAME}...")
         print(f"Version:{VERSION}")
         print(f"Created by: {AUTHOR}")
         log_event("System initialized successfully.")
           
           
    def main():
    inintialize_system()
    print("\nType 'help' to view available commands.\n")

    while True:
        user_input = input("Rheanova>").strip().lower()
        if user_input == "exit":
            print("System shutting down...")
            log_event("System shutdown by user.")
            break
        elif user_input == "help":
            print("Available commands: help, info, clear, exit")
        elif user_input == "info":
            print(f"{SYSTEM_NAME} - {VERSION}\nStatus: Online") 
        elif user_input == "clear":
            os.system("clear" if os.name == "posix" else "cls")
        elif print("Unknown command.") 
             log_event (f"Unknown command attempted: {user_input}")

if_name_ == "__main__":main()                                       
import os
import sys

# Function to display the ASCII text logo
def display_logo():
    print("    __    _  _    __    ____   ___  _   _  _  _    ____  _____  _  _  _  _ ")
    print("   /__\\  ( \\( )  /__\\  (  _ \\ / __)( )_( )( \\/ )  ( ___)(  _  )( \\/ )( \\/ )")
    print("  /(__)\\  )  (  /(__)\\  )   /( (__  ) _ (  \\  /    )__)  )(_)(  )  (  \\  / ")
    print(" (__)(__)(_)\\_)(__)(__)(_)\\_) \\___)(_) (_) (__)   (__)  (_____)(_/\\_) (__)  ")
    print("   ___  _   _  ____  __    __   ")
    print(" / __)( )_( )( ___)(  )  (  )  ")
    print(" \\__ \\ ) _ (  )__)  )(__  )(__ ")
    print(" (___/(_) (_)(____)(____)(____)")

# Function to parse the input command and arguments
def parse_command(input_str):
    args = input_str.split()
    command = args[0]
    arguments = args[1:]
    return command, arguments

# Function to execute a command with arguments
def execute_command(command, arguments):
    if command == "exit":
        print("Anarchy Foxy Says Goodbye!")
        sys.exit(0)

    try:
        pid = os.fork()

        if pid < 0:
            raise Exception("Fork error")
        elif pid == 0:
            # Child process executes the command
            os.execvp(command, [command] + arguments)
            raise Exception("Command execution error")
        else:
            # Parent process waits for the child to complete
            os.waitpid(pid, 0)
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)

def main():
    display_logo()

    while True:
        print("\nAnarchy Foxy Shell :> ", end="")
        input_str = input()

        command, arguments = parse_command(input_str)
        execute_command(command, arguments)

if __name__ == "__main__":
    main()

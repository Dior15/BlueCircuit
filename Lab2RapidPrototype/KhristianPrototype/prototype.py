import frontend

def main():
    """Main function to run the application."""
    frontend.print_intro()
    while True:
        frontend.menu()

if __name__ == "__main__":
    main()
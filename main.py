print("\nby codeTech\n")

# This project is to remove duplicate emails from a text file.
# The file needs to be txt and the emails need to be on a new line.
# The program will ask you for the file path and then it will remove the duplicates.
# It will also tell you how many duplicates it found and how many it removed.

def remove_duplicates(file_path):
    with open(file_path, 'r') as f:
        emails = [line.strip() for line in f]
    
    unique_emails = set()
    duplicate_emails = []
    for email in emails:
        if email in unique_emails:
            duplicate_emails.append(email)
        else:
            unique_emails.add(email)
    
    if not duplicate_emails:
        print("No duplicate emails found.")
        return
    
    print(f"{len(duplicate_emails)} duplicate email(s) found.")
    print(f"Duplicate emails: {duplicate_emails}")
    
    while True:
        print(f"\nEmail: {len(unique_emails)} - Duplicats - {len(duplicate_emails)} unique email(s) found.")
        remove = input(f"\nRemove duplicate emails? (Y/N): ")
        if remove.lower() == 'y':
            with open(file_path, 'w') as f:
                for email in emails:
                    if email in unique_emails:
                        f.write(email + "\n")
                        unique_emails.remove(email)
            print(f"{len(duplicate_emails)} duplicate email(s) removed.")
            break
        elif remove.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    
    print("Duplicate removal complete.")


if __name__ == "__main__":
    file_path = input("Enter file path: ")
    remove_duplicates(file_path)


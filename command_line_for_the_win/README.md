This is my README file

## File Transfer Using SFTP

This project involves using the SFTP (Secure File Transfer Protocol) command-line tool to move local screenshots to the sandbox environment. Below are the steps followed for the file transfer:

### Prerequisites

- Ensure you have access to the sandbox environment with the provided hostname, username, and password.
- SFTP command-line tool is installed on your local machine.

### Steps to Transfer Screenshots

1. **Take Screenshots:**
   - Complete the required levels as mentioned in the project instructions.
   - Take screenshots of the completed levels and save them in the `/root/alx-system_engineering-devops/command_line_for_the_win/` directory.

2. **Open Terminal or Command Prompt:**
   - Open a terminal or command prompt on your local machine.

3. **Establish SFTP Connection:**
   - Use the following command to establish an SFTP connection to the sandbox environment:
     ```bash
     sftp username@hostname
     ```
     Replace `username` and `hostname` with the provided credentials.

4. **Navigate to the Destination Directory:**
   - Once connected, navigate to the directory where you want to upload the screenshots in the sandbox environment.
     ```bash
     cd /path/to/sandbox/directory
     ```

5. **Upload Screenshots:**
   - Use the `put` command to upload the screenshots from your local machine to the sandbox environment.
     ```bash
     put /path/to/local/screenshots/*.png
     ```

6. **Confirm Transfer:**
   - Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
     ```bash
     ls -l
     ```

7. **Exit SFTP:**
   - Type `exit` to close the SFTP connection.

8. **Push Screenshots to GitHub:**
   - Push the screenshots to GitHub as mentioned in the initial requirements.

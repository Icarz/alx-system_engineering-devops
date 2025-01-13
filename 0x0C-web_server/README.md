0x0C. Web Server

Description

This project focuses on understanding and configuring web servers, specifically Nginx, and automating these tasks using Bash scripts. By the end of this project, you will understand:

The main role of a web server

What child processes are and why they are used in web servers

DNS concepts and record types (A, CNAME, TXT, MX)

Basic HTTP requests and responses

Learning Objectives

At the end of this project, you should be able to:

Explain the purpose of a web server and its role in serving web content.

Understand child processes and their role in web server architecture.

Configure DNS records for a domain.

Write Bash scripts to automate server configuration.

Requirements

General:

Use vi, vim, or emacs as your editor.

Scripts will run on Ubuntu 16.04 LTS.

All scripts must end with a new line.

Include a README.md file at the root of the project directory.

All Bash scripts must be executable.

Scripts must pass Shellcheck (version 0.3.7) without errors.

The first line of scripts must be #!/usr/bin/env bash.

The second line should be a comment explaining what the script does.

You cannot use systemctl for restarting processes.

Tasks

0. Transfer a file to your server

Write a Bash script 0-transfer_file that:

Transfers a file to a remote server using scp.

Accepts 4 arguments: file path, server IP, username, and SSH private key path.

Transfers the file to the user's home directory (~/).

Disables strict host key checking.

1. Install nginx web server

Write a Bash script 1-install_nginx_web_server that:

Installs the Nginx web server.

Configures Nginx to serve a page with the content Hello World! at its root.

Ensures Nginx is listening on port 80.

2. Setup a domain name

Register a .tech domain through the GitHub student pack.

Configure DNS records with an A entry pointing to your server's IP.

Save the domain name in a file 2-setup_a_domain_name.

3. Redirection

Write a Bash script 3-redirection that:

Configures Nginx to redirect /redirect_me to a different URL (e.g., YouTube).

Implements a 301 Moved Permanently redirection.

4. Not found page 404

Write a Bash script 4-not_found_page_404 that:

Configures Nginx with a custom 404 error page.

The page must return the text Ceci n'est pas une page and an HTTP 404 error code.

How to Use

Clone the repository:

git clone https://github.com/your-username/alx-system_engineering-devops.git

Navigate to the project directory:

cd 0x0C-web_server

Make scripts executable:

chmod +x 0-transfer_file 1-install_nginx_web_server 3-redirection 4-not_found_page_404

Execute the scripts as required:

./script_name arguments

Resources

How the Web Works

Nginx Documentation

HTTP Status Codes

DNS Basics

Author

Your Name - GitHub


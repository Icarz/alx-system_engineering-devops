# 0x0B. SSH

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Resources](#resources)
- [Tasks](#tasks)
  - [Task 0: Use a private key](#task-0-use-a-private-key)
  - [Task 1: Create an SSH key pair](#task-1-create-an-ssh-key-pair)
  - [Task 2: Client configuration file](#task-2-client-configuration-file)
  - [Task 3: Let me in!](#task-3-let-me-in)
- [Requirements](#requirements)

---

## Introduction
This project focuses on understanding the use of SSH (Secure Shell) to connect to remote servers securely. You will learn how to generate and manage SSH key pairs, configure SSH client settings, and connect to remote servers without using a password. These tasks are essential skills for DevOps, SysAdmin, and network security roles.

---

## Learning Objectives
By the end of this project, you should be able to:
- Explain what a server is and where servers usually reside.
- Understand SSH and how it secures remote connections.
- Create an SSH RSA key pair and use it to connect to a remote server.
- Configure an SSH client for passwordless authentication.
- Explain the advantages of using `#!/usr/bin/env bash` over `/bin/bash` in scripts.

---

## Resources
Refer to these resources to understand the concepts better:
- [What is a (physical) server - text](https://intranet.alxswe.com)
- [What is a (physical) server - video](https://intranet.alxswe.com)
- [SSH essentials](https://intranet.alxswe.com)
- [SSH Config File](https://intranet.alxswe.com)
- [Public Key Authentication for SSH](https://intranet.alxswe.com)
- [How Secure Shell Works](https://intranet.alxswe.com)
- [SSH Crash Course](https://intranet.alxswe.com)

Man pages:
- `man ssh`
- `man ssh-keygen`
- `man env`

---

## Tasks

### Task 0: Use a private key
Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

**Requirements:**
- Use single-character flags for `ssh`.
- Do not use `-l` for specifying the username.
- Ignore the case of passphrase-protected private keys.

**File:** `0-use_a_private_key`

---

### Task 1: Create an SSH key pair
Write a Bash script to create an RSA key pair with the following specifications:
- Private key name: `school`
- Key size: `4096 bits`
- Protected with passphrase: `betty`

**File:** `1-create_ssh_key_pair`

---

### Task 2: Client configuration file
Configure the SSH client to use the private key `~/.ssh/school` and disable password authentication. Save the configuration in the file `2-ssh_config`.

**Requirements:**
- Use the private key `~/.ssh/school`.
- Refuse password authentication.

**File:** `2-ssh_config`

---

### Task 3: Let me in!
Add the provided public key to your server's `authorized_keys` file to allow the ALX team to connect as the `ubuntu` user.

**Public Key:**
```plaintext
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN

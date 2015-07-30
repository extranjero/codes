#Genereate ssh key

Creates a new ssh key, using the provided email as a label
Generating public/private rsa key pair.

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Then when cmd prompts

```bash
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
```

Press enter

You'll be asked to enter a passphrase.

```bash
Enter passphrase (empty for no passphrase): [Type a passphrase]
Enter same passphrase again: [Type passphrase again]
```

Add your SSH key to the ssh-agent:

```bash
$ ssh-add ~/.ssh/id_rsa
```

Add your ssh key to your github account

```bash
cat ~/.ssh/id_rsa.pub
```

Copy to clipboard
Add the copied key to GitHub:

Profile Photo -> Settings -> Ssh keys -> add ssh key

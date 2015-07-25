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

AWS S3 and DynamoDb Management
===============================

# Environments
```
python:3.8.10
boto3[crt]:1.15.2
pip3:20.0.2
awscli:2.7.32
```

# Env Installation
## python3 and pip3
```bash
apt update && apt install python3.8 curl unzip -y && apt install python3-pip -y
```


## dependencies
```bash
pip3 install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

## awscli
```bash
# awscli installation
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
echo "export PATH=\$PATH:/usr/local/bin" >> ~/.profile
source ~/.profile

# aws configure
aws configure
## Input your aws credentials (aws_access_key_id、aws_secret_access_key and region)
## region=ap-southeast-2

```

# Running code
```bash
python3 main.py
```

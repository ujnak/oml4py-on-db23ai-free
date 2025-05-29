# oml4py-on-db23ai-free
Script to configure OML4Py on Oracle Database Free 23ai container.

```bash
git clone https://github.com/ujnak/oml4py-on-db23ai-free
cd oml4py-on-db23ai-free
```
## Step 1: download Python-3.12.6.tgz

```bash
curl -OL https://www.python.org/ftp/python/3.12.6/Python-3.12.6.tgz
```

## Step 2: download V1048628-01.zip

download OML4Py client 2.1 from 
https://www.oracle.com/database/technologies/oml4py-downloads.html

## Step 3: create and run Oracle Database Free 23ai container

download latest Oracle Database Free 23ai container image.
```bash
podman pull container-registry.oracle.com/database/free:latest
```
Create and run oracle database free container - oml4py-db

```bash
podman run -d --name oml4py-db -p 1521:1521 -v $PWD:/home/oracle/work container-registry.oracle.com/database/free:latest
```

Current directory is mounted on /home/oracle/work in the container.

## Step 4: connect to the running container

```bash
podman exec -it oml4py-db bash
```

## Step 5: run configuration script

1st argument is for the password of user oml_user.

```bash
sh work/config-oml4py.sh <password>
```

## Step 6: export all-MiniLM-L6-v2.onnx for test

```bash
. work/oml4py.env
python3 work/export-onnx-test.py
```

## Step 7: verify all-MiniLM-L6-v2.onnx is created.

within container, all-MiniLM-L6-v2.onnx can be found under ./work directory.
on host, all-MiniLM-L6-v2.onnx can be found in the current working directory.




# Running (without docker):

Requires:
  * Python 3.6

Optional (but preferred):
  * virtualenv (to create a virtual environment)

```shell
pip install -r requirements.txt
python update-windows-release-json.py https://download.docker.com 17.06.1-ee edge https://download.docker.com/components/engine/windows-server/17.03/docker-17.03.1-ee.zip
```

# Running (with docker):

```shell
make BASE_URL=https://download.docker.com RELEASE_NAME=17.06.1-ee-rc1 RELEASE_CHANNEL=test RELEASE_URL=https://download.docker.com/components/engine/windows-server/17.03/docker-17.03.1-ee.zip
```

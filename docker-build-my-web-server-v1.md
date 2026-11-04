Terminal transcript - 2026-11-04 20:21:27
PS> docker build -t my-web-server:v1 .
#0 building with "desktop-linux" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 377B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/nginx:latest
#2 ...

#3 [auth] library/nginx:pull token for registry-1.docker.io
#3 DONE 0.0s

#2 [internal] load metadata for docker.io/library/nginx:latest
#2 DONE 1.2s

#4 [internal] load .dockerignore
#4 transferring context: 2B done
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 360B done
#5 DONE 0.0s

#6 [1/2] FROM docker.io/library/nginx:latest@sha256:5ab5b0b01097420873a3f3330f44248e34a3c2a3e8d5ee30658aeae8cb7435da
#6 resolve docker.io/library/nginx:latest@sha256:5ab5b0b01097420873a3f3330f44248e34a3c2a3e8d5ee30658aeae8cb7435da 0.0s done
#6 CACHED

#7 [2/2] COPY index.html /usr/share/nginx/html/index.html
#7 DONE 0.0s

#8 exporting to image
#8 exporting layers 0.1s done
#8 exporting manifest sha256:b8bbb09bde673b6387e11fd61e9847fe47a82b3510b53fc8407b5774bb033c1c 0.0s done
#8 exporting config sha256:a8d35a5e5f1a7570c51a7021d59ab631beaf8198fbee6540bc244c0b0b95f4da 0.0s done
#8 exporting attestation manifest sha256:dcc37e3a425ac45917c22922a09f5f79c872245d9b5bc377ae3eaf3f5958e17c 0.0s done
#8 exporting manifest list sha256:28001100fea4f21369e688d6cccadea4d99885f71159baf6df1b7170f69689e1 0.0s done
#8 naming to docker.io/library/my-web-server:v1 done
#8 unpacking to docker.io/library/my-web-server:v1 0.0s done
#8 DONE 0.2s
Exit code: 0

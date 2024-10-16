# コンテナの確認 (master/worker共通)
```
$ docker ps

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

# ネットワークの確認(master/worker共通)
```
$ docker network ls

NETWORK ID     NAME      DRIVER    SCOPE
50269d80052b   bridge    bridge    local
e80bd3a263ec   host      host      local
93abcdf649c5   none      null      local
```

# Swarmの状態確認(master/worker共通)
Swarmが、inactive（非活性）になっていることを確認する

```
$ docker info

Cgroup Driver: systemd
Cgroup Version: 2
Plugins:
Volume: local
Network: bridge host ipvlan macvlan null overlay
Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
Swarm: inactive
Runtimes: io.containerd.runc.v2 runc
Default Runtime: runc
Init Binary: docker-init
containerd version: 2806fc1057397dbaeefbea0e4e17bddfbd388f38
runc version: v1.1.5-0-gf19387a
init version: de40ad0
Security Options:
```

# Swarmをactive（活性）化 (master)
Swarmを、activeにする。もう1回docker infoやるとactiveになってるはず。

## active（活性）化 正常系
```
$ docker swarm init

Swarm initialized: current node (5ot57w0pzpkqdecqjqewgdcmz) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1olupoxrddqtjgy1u6wa47fj0zq4skb1skx9vm3fkocwcvryai-97l5yntsy7i669bubomau2kcn 172.28.164.85:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

```

## active（活性）化 エラー１
以下のエラーが返って来たら、
```
$ docker swarm init

Error response from daemon: This node is already part of a swarm. Use "docker swarm leave" to leave this swarm and join another one.
```

以下のコマンドを打つ
```
$docker swarm leave --force

Node left the swarm.
```

# swarm に参加する (worker)
docker swarm join --token SWMTKN-1-1olupoxrddqtjgy1u6wa47fj0zq4skb1skx9vm3fkocwcvryai-97l5yntsy7i669bubomau2kcn 172.28.164.85:2377


# クラスタを確認する(master)
```
docker node ls
```

# swarmを無効化する(master)
```
docker swarm leave --force
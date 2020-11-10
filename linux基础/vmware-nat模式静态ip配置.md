---
title: vmware-nat模式静态ip配置
date: 2020-10-09 21:56:26
tags: linux
categories: 环境搭建
---



# vmware-nat模式静态ip配置

1. 在控制面板网络连接查看VMnet8属性，勾选如图两项

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009215000.png" alt="image-20201009215000595" style="zoom: 50%;" />

<!--more-->

打开tcp/ipv4属性，ip可自由设置，很多人机器ip都是`192.168.*.1`。设置子网掩码，网关

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009215127.png" alt="image-20201009215127048" style="zoom:50%;" />

2. 打开虚拟机网络编辑器，取消勾选DHCP，修改子网ip与1ip保持同一网段

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009214726.png" alt="image-20201009214726702" style="zoom:50%;" />

打开net,记住ip设置,网关同1

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009214827.png" alt="image-20201009214826977" style="zoom:50%;" />

3. 重启后，修改网络配置文件，改为静态，开机自启，设置ip，保持同一网段，网管一致，设置2个DNSip地址

```shell
#/etc/sysconfig/network-scripts/对应网口

TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static					##
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=76cc174a-6dc4-4bd6-98d5-aedc0458bf82
DEVICE=ens33
ONBOOT=yes									##
IPADDR=192.168.72.88				##
GATEWAY=192.168.72.2				##
DNS1=8.8.8.8								##
DNS2=8.8.4.4								##
```

4. 重启网络服务`service network restart`

`ping`下网站，看能否访问，ping不通可检查防火墙设置

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009220510.png" alt="image-20201009220510940" style="zoom:67%;" />

